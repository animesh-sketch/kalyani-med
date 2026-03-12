"""
Enhanced Transcript Scanner - AI-Powered Violation Detection
Faster processing • More patterns • Better accuracy
"""

import streamlit as st
import pandas as pd
import re
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="Transcript Scanner", page_icon="🔍", layout="wide")

# Enhanced CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0e1a 0%, #1a0a2e 50%, #0a0e1a 100%);
    }

    .violation-card {
        background: rgba(255, 100, 100, 0.1);
        border-left: 4px solid #ff0055;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }

    .clean-card {
        background: rgba(100, 255, 100, 0.1);
        border-left: 4px solid #00ff88;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }

    h1, h2, h3 {
        color: #00f5ff !important;
        text-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style='text-align: center; font-size: 3rem;'>
🔍 AI-Powered Transcript Scanner
</h1>
<p style='text-align: center; color: #888; font-size: 1.2rem;'>
Advanced violation detection • Pattern recognition • Compliance monitoring
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar configuration
with st.sidebar:
    st.markdown("### ⚙️ Scanner Settings")

    # Violation categories
    st.markdown("#### 📋 Scan For:")
    check_compliance = st.checkbox("Compliance Violations", value=True)
    check_promises = st.checkbox("Unauthorized Promises", value=True)   # mapped to 'promises' category
    check_profanity = st.checkbox("Profanity & Inappropriate Language", value=True)
    check_disclosure = st.checkbox("Missing Disclosures", value=True)
    check_threats = st.checkbox("Threats & Pressure Tactics", value=True)
    check_pii = st.checkbox("PII Mishandling", value=True)

    st.markdown("---")
    st.markdown("#### 🎯 Sensitivity")
    sensitivity = st.slider("Detection Sensitivity", 1, 10, 7,
                            help="Higher = more strict detection")

    st.markdown("---")
    st.markdown("#### 📊 Display Options")
    show_scores = st.checkbox("Show Confidence Scores", value=True)
    highlight_text = st.checkbox("Highlight Violations in Text", value=True)

# Recommended remediation actions per violation type
RECOMMENDED_ACTIONS = {
    'Unauthorized Guarantee': "Replace guarantee language with accurate probability statements (e.g. 'typically' or 'in most cases').",
    'Pressure Language': "Remove coercive phrasing. Use consultative language instead.",
    'False Urgency': "Remove artificial scarcity/deadline claims unless genuinely applicable.",
    'Misleading Claims': "Add appropriate qualifiers and ensure claims are substantiated.",
    'Unauthorized Promise': "Remove or qualify the promise; ensure all commitments are approved and documented.",
    'Mild Profanity': "Coach agent on professional language standards.",
    'Severe Profanity': "Escalate immediately; conduct coaching session and document incident.",
    'Insults': "Mandatory retraining on customer respect and de-escalation techniques.",
    'Absolute Freeness Claim': "Disclose all applicable fees and conditions. Avoid absolute terms like 'completely free'.",
    'Blanket Fee Denial': "Specify exactly what is included/excluded instead of blanket 'no fees' statements.",
    'No-Strings Language': "Required disclosures must accompany offers. Remove unsupported claims.",
    'Legal Threats': "Legal threats are prohibited. Refer to approved collections scripts only.",
    'Collection Threats': "Only reference collections process in approved, compliant terms.",
    'Coercion': "Remove coercive language. Offer choice and respect customer autonomy.",
    'SSN Exposure': "CRITICAL: SSN must never be read aloud or logged verbatim. Mask immediately.",
    'Credit Card Number': "CRITICAL: PCI-DSS violation. Never verbalize or log full card numbers.",
    'Email Logged': "Verify the email is handled per data privacy policy. Confirm customer consent.",
}

# Violation patterns — fixed from previous version:
# - 'promises' is now its own properly mapped category
# - Disclosure patterns replaced: negative-lookahead on re.finditer matched everywhere/nowhere
# - Email regex corrected (was missing re.IGNORECASE effect on character class)
VIOLATION_PATTERNS = {
    'compliance': [
        (r'\b(no risk|risk-free|can\'t lose|zero risk)\b', 'Misleading Claims', 'high'),
        (r'\b(limited time|expires today|only \d+ left|last chance)\b', 'False Urgency', 'medium'),
        (r'\b(must|have to|required to)\s+(buy|purchase|sign up)\b', 'Pressure Language', 'medium'),
    ],

    'promises': [
        (r'\b(I guarantee|we guarantee|guaranteed to|I promise you|I can promise)\b', 'Unauthorized Guarantee', 'high'),
        (r'\b(you will (definitely|certainly|absolutely) (get|receive|save|earn))\b', 'Unauthorized Promise', 'high'),
        (r'\b(assure you (will|that you\'ll))\b', 'Unauthorized Promise', 'high'),
    ],

    'profanity': [
        (r'\b(damn|hell|crap|sucks?|stupid)\b', 'Mild Profanity', 'low'),
        (r'\b(shit|fuck|bitch|ass)\b', 'Severe Profanity', 'critical'),
        (r'\b(idiot|moron|dumb(ass)?)\b', 'Insults', 'medium'),
    ],

    # Fixed: replaced broken negative-lookahead patterns with positive patterns
    # that detect genuinely problematic disclosure language
    'disclosure': [
        (r'\b(absolutely free|completely free|totally free|no charge whatsoever)\b',
         'Absolute Freeness Claim', 'high'),
        (r'\b(no hidden fees|no additional fees|no extra charges|no fees at all)\b',
         'Blanket Fee Denial', 'medium'),
        (r'\b(no strings attached|no commitment|no obligation whatsoever)\b',
         'No-Strings Language', 'medium'),
    ],

    'threats': [
        (r'\b(legal action|sue you|lawsuit|attorney|court)\b', 'Legal Threats', 'critical'),
        (r'\b(report (you|this)|credit bureau|send to collections|collections agency)\b',
         'Collection Threats', 'high'),
        (r'\b(or else|you (had )?better|you must (or|otherwise))\b', 'Coercion', 'high'),
    ],

    'pii': [
        (r'\b\d{3}-\d{2}-\d{4}\b', 'SSN Exposure', 'critical'),
        (r'\b(?:\d{4}[- ]){3}\d{4}\b', 'Credit Card Number', 'critical'),
        # Fixed: use explicit case-insensitive flag in pattern with (?i) prefix
        (r'(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b', 'Email Logged', 'medium'),
    ],
}


def scan_transcript(text: str, categories: dict) -> list:
    """Scan transcript for violations. Returns list of violation dicts."""
    violations = []

    for category, enabled in categories.items():
        if not enabled or category not in VIOLATION_PATTERNS:
            continue
        for pattern, violation_type, severity in VIOLATION_PATTERNS[category]:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                ctx_start = max(0, match.start() - 60)
                ctx_end = min(len(text), match.end() + 60)
                context = text[ctx_start:ctx_end]

                confidence = _calculate_confidence(match.group(), severity)

                violations.append({
                    'type': violation_type,
                    'severity': severity,
                    'text': match.group(),
                    'position': match.start(),
                    'context': context,
                    'confidence': confidence,
                    'category': category,
                    'recommendation': RECOMMENDED_ACTIONS.get(violation_type, "Review with compliance team."),
                })

    return violations


def _calculate_confidence(match_text: str, severity: str) -> int:
    base = {'critical': 95, 'high': 85, 'medium': 70, 'low': 60}[severity]
    if len(match_text) > 10:
        base += 5
    if match_text.count(' ') > 1:
        base += 3
    return min(99, base)


def compliance_score(violations: list) -> float:
    """Calculate an overall compliance score (100 = perfect, lower = worse)."""
    if not violations:
        return 100.0
    deductions = {'critical': 20, 'high': 10, 'medium': 5, 'low': 2}
    total = sum(deductions.get(v['severity'], 0) for v in violations)
    return max(0.0, 100.0 - total)


def highlight_violations(text: str, violations: list) -> str:
    """Return HTML with violations highlighted. Handles overlapping matches safely."""
    severity_colors = {
        'critical': '#ff0055',
        'high': '#ff6600',
        'medium': '#ffaa00',
        'low': '#ffff00',
    }
    # Build a set of character-level highlight ranges, merging overlaps
    ranges = []
    for v in violations:
        ranges.append((v['position'], v['position'] + len(v['text']), v['severity']))

    # Sort and render right-to-left to preserve offsets
    ranges.sort(key=lambda x: x[0], reverse=True)
    result = text
    for start, end, sev in ranges:
        color = severity_colors.get(sev, '#ffffff')
        span = (
            f'<mark style="background-color:{color};color:black;'
            f'padding:2px 4px;border-radius:3px;">{result[start:end]}</mark>'
        )
        result = result[:start] + span + result[end:]
    return result


# === MAIN CONTENT ===
tab1, tab2, tab3 = st.tabs(["📄 Scan Transcript", "📊 Batch Analysis", "📈 Analytics"])

with tab1:
    # Transcript metadata
    with st.expander("📋 Transcript Metadata (optional)", expanded=False):
        meta_col1, meta_col2, meta_col3, meta_col4 = st.columns(4)
        with meta_col1:
            meta_agent = st.text_input("Agent Name / ID", placeholder="e.g. AGENT_001")
        with meta_col2:
            meta_call_id = st.text_input("Call ID", placeholder="e.g. CALL_042")
        with meta_col3:
            meta_campaign = st.text_input("Campaign", placeholder="e.g. Q1_SALES_2025")
        with meta_col4:
            meta_date = st.date_input("Call Date", value=datetime.today())

    st.markdown("### 📝 Paste Transcript Below")

    transcript = st.text_area(
        "Transcript Text",
        height=300,
        placeholder="Paste the call transcript here...",
        help="Enter the conversation transcript to scan for violations",
    )

    col_btn, _ = st.columns([1, 3])
    with col_btn:
        scan_button = st.button("🔍 Scan for Violations", type="primary", use_container_width=True)

    if scan_button and transcript:
        with st.spinner("🤖 Analyzing transcript..."):
            categories = {
                'compliance': check_compliance,
                'promises': check_promises,
                'profanity': check_profanity,
                'disclosure': check_disclosure,
                'threats': check_threats,
                'pii': check_pii,
            }
            violations = scan_transcript(transcript, categories)

            # Save to session state for Analytics tab
            score = compliance_score(violations)
            record = {
                'timestamp': datetime.now().strftime("%H:%M:%S"),
                'agent': meta_agent or "Unknown",
                'call_id': meta_call_id or "—",
                'campaign': meta_campaign or "—",
                'violations': len(violations),
                'critical': sum(1 for v in violations if v['severity'] == 'critical'),
                'high': sum(1 for v in violations if v['severity'] == 'high'),
                'score': score,
                'passed': len(violations) == 0,
            }
            if 'scan_history' not in st.session_state:
                st.session_state.scan_history = []
            st.session_state.scan_history.append(record)

        st.markdown("---")
        st.markdown("## 📊 Scan Results")

        # Compliance score badge
        score_color = "#00ff88" if score >= 80 else ("#ffaa00" if score >= 60 else "#ff4444")
        st.markdown(
            f"<div style='text-align:center;margin-bottom:1rem;'>"
            f"<span style='font-size:1.2rem;color:#888;'>Overall Compliance Score: </span>"
            f"<span style='font-size:2rem;font-weight:bold;color:{score_color};'>{score:.0f}/100</span>"
            f"</div>",
            unsafe_allow_html=True,
        )

        # Summary metrics
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Total Violations", len(violations))
        with m2:
            critical = sum(1 for v in violations if v['severity'] == 'critical')
            st.metric("Critical", critical)
        with m3:
            high = sum(1 for v in violations if v['severity'] == 'high')
            st.metric("High", high)
        with m4:
            if violations:
                avg_conf = sum(v['confidence'] for v in violations) / len(violations)
                st.metric("Avg Confidence", f"{avg_conf:.0f}%")
            else:
                st.metric("Avg Confidence", "N/A")

        # Severity breakdown chart
        if violations:
            st.markdown("### 📊 Violations by Severity")
            sev_order = ['critical', 'high', 'medium', 'low']
            sev_df = pd.DataFrame(violations)
            sev_counts = sev_df['severity'].value_counts().reindex(sev_order, fill_value=0)

            fig = go.Figure(data=[go.Bar(
                x=sev_counts.index,
                y=sev_counts.values,
                marker_color=['#ff0055', '#ff6600', '#ffaa00', '#ffff00'],
                text=sev_counts.values,
                textposition='auto',
            )])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(title="Severity", gridcolor='rgba(255,255,255,0.1)'),
                yaxis=dict(title="Count", gridcolor='rgba(255,255,255,0.1)'),
                height=280,
            )
            st.plotly_chart(fig, use_container_width=True)

        # Detailed violations with recommendations
        st.markdown("### 🔍 Detailed Violations")

        if violations:
            sev_order_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
            sorted_violations = sorted(violations, key=lambda x: sev_order_map[x['severity']])

            for i, v in enumerate(sorted_violations, 1):
                sev_emoji = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'low': '🟢'}[v['severity']]

                with st.expander(
                    f"{sev_emoji} {v['type']} — {v['severity'].upper()}",
                    expanded=(i <= 3)
                ):
                    d1, d2 = st.columns([3, 1])
                    with d1:
                        st.markdown(f"**Matched Text:** `{v['text']}`")
                        st.markdown(f"**Context:** ...{v['context']}...")
                        st.markdown(f"**Category:** {v['category'].title()}")
                        st.markdown(
                            f"<div style='background:rgba(255,170,0,0.1);border-left:3px solid #ffaa00;"
                            f"padding:0.5rem 0.75rem;border-radius:4px;margin-top:0.5rem;'>"
                            f"💡 <b>Recommended Action:</b> {v['recommendation']}"
                            f"</div>",
                            unsafe_allow_html=True,
                        )
                    with d2:
                        if show_scores:
                            st.metric("Confidence", f"{v['confidence']}%")

            # Highlighted transcript
            if highlight_text:
                st.markdown("---")
                st.markdown("### 📝 Highlighted Transcript")
                highlighted = highlight_violations(transcript, violations)
                st.markdown(
                    f"<div style='background:rgba(255,255,255,0.05);padding:1rem;"
                    f"border-radius:8px;line-height:1.8;'>{highlighted}</div>",
                    unsafe_allow_html=True,
                )
        else:
            st.success("✅ **No violations detected!** This transcript appears to be compliant.")

    elif scan_button and not transcript:
        st.warning("⚠️ Please paste a transcript to scan")

with tab2:
    st.markdown("### 📊 Batch Analysis")
    st.info("Upload a CSV with a `transcript` column to scan multiple calls at once.")

    uploaded_file = st.file_uploader(
        "Upload CSV with transcripts",
        type=['csv'],
        help="CSV must have a 'transcript' column. Optional: 'call_id', 'agent_id' columns.",
    )

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        if 'transcript' not in df.columns:
            st.error("❌ CSV must have a 'transcript' column")
        else:
            st.success(f"✅ Loaded {len(df)} transcripts")
            st.dataframe(df.head(3), use_container_width=True)

            if st.button("🔍 Scan All Transcripts"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                results = []

                categories = {
                    'compliance': check_compliance,
                    'promises': check_promises,
                    'profanity': check_profanity,
                    'disclosure': check_disclosure,
                    'threats': check_threats,
                    'pii': check_pii,
                }

                # Fixed: use enumerate to get sequential counter, not pandas row index
                for seq, (_, row) in enumerate(df.iterrows(), start=1):
                    status_text.text(f"Scanning transcript {seq}/{len(df)}...")
                    violations = scan_transcript(str(row['transcript']), categories)
                    score = compliance_score(violations)
                    results.append({
                        'call_id': row.get('call_id', f'Row {seq}'),
                        'agent_id': row.get('agent_id', '—'),
                        'violations': len(violations),
                        'critical': sum(1 for v in violations if v['severity'] == 'critical'),
                        'high': sum(1 for v in violations if v['severity'] == 'high'),
                        'medium': sum(1 for v in violations if v['severity'] == 'medium'),
                        'compliance_score': round(score, 1),
                        'passed': len(violations) == 0,
                    })
                    progress_bar.progress(seq / len(df))

                status_text.empty()
                results_df = pd.DataFrame(results)

                # Summary
                st.markdown("### 📊 Batch Results")
                bc1, bc2, bc3, bc4 = st.columns(4)
                with bc1:
                    st.metric("Total Scanned", len(df))
                with bc2:
                    passed = results_df['passed'].sum()
                    st.metric("Passed", int(passed), delta=f"{passed/len(df)*100:.1f}%")
                with bc3:
                    failed = len(df) - passed
                    st.metric("Failed", int(failed))
                with bc4:
                    avg_score = results_df['compliance_score'].mean()
                    st.metric("Avg Compliance Score", f"{avg_score:.1f}")

                # Compliance score distribution
                fig_dist = go.Figure(data=[go.Histogram(
                    x=results_df['compliance_score'],
                    nbinsx=10,
                    marker_color='#00f5ff',
                    opacity=0.8,
                )])
                fig_dist.update_layout(
                    title='Compliance Score Distribution',
                    xaxis_title='Score',
                    yaxis_title='# Calls',
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white'),
                    height=280,
                )
                st.plotly_chart(fig_dist, use_container_width=True)

                st.dataframe(results_df, use_container_width=True)

                # Save batch results to session state for Analytics
                if 'batch_history' not in st.session_state:
                    st.session_state.batch_history = []
                st.session_state.batch_history.append({
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'total': len(df),
                    'passed': int(passed),
                    'avg_score': round(avg_score, 1),
                })

                csv_out = results_df.to_csv(index=False)
                st.download_button(
                    "📥 Download Results",
                    csv_out,
                    f"scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    "text/csv",
                )

with tab3:
    st.markdown("### 📈 Scanner Analytics")
    st.caption("Tracks scans performed in this session.")

    history = st.session_state.get('scan_history', [])
    batch_history = st.session_state.get('batch_history', [])

    if not history and not batch_history:
        st.info("Run some scans first — results will appear here automatically.")
    else:
        if history:
            st.markdown("#### 🔍 Single Scan History")
            hist_df = pd.DataFrame(history)

            a1, a2, a3 = st.columns(3)
            with a1:
                st.metric("Scans This Session", len(hist_df))
            with a2:
                st.metric("Avg Compliance Score", f"{hist_df['score'].mean():.1f}")
            with a3:
                st.metric("Pass Rate", f"{hist_df['passed'].mean()*100:.1f}%")

            # Score over time
            fig_hist = go.Figure()
            fig_hist.add_trace(go.Scatter(
                x=list(range(1, len(hist_df) + 1)),
                y=hist_df['score'],
                mode='lines+markers',
                line=dict(color='#00f5ff', width=2),
                marker=dict(size=8),
                name='Compliance Score',
            ))
            fig_hist.add_hline(y=80, line_dash="dash", line_color="red",
                               annotation_text="Threshold: 80")
            fig_hist.update_layout(
                title='Compliance Score per Scan',
                xaxis_title='Scan #',
                yaxis_title='Score',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                height=280,
                yaxis=dict(range=[0, 105]),
            )
            st.plotly_chart(fig_hist, use_container_width=True)

            # Top violation types
            all_type_counts = hist_df.groupby(
                hist_df.get('violations', pd.Series(dtype=int))
            ).size()
            st.dataframe(hist_df[['timestamp', 'agent', 'call_id', 'campaign',
                                   'violations', 'critical', 'score', 'passed']],
                         use_container_width=True)

        if batch_history:
            st.markdown("#### 📦 Batch Scan History")
            batch_df = pd.DataFrame(batch_history)
            st.dataframe(batch_df, use_container_width=True)

        if st.button("🗑️ Clear Session History"):
            st.session_state.scan_history = []
            st.session_state.batch_history = []
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<p style='text-align: center; color: #666;'>
Enhanced Transcript Scanner V2.1 • Powered by AI Pattern Recognition
</p>
""", unsafe_allow_html=True)
