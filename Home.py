"""
Enhanced Dashboard - Quality Intelligence Engine V3.0
Modern analytics with AI-powered insights
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Enhanced CSS with animations (shimmer keyframe was missing before)
st.markdown("""
<style>
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #0a0e1a, #1a0a2e, #16213e, #0f3460);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Shimmer animation for title (was referenced but never defined) */
    @keyframes shimmer {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    /* Glowing metrics */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #00f5ff, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from { filter: brightness(1); }
        to { filter: brightness(1.3); }
    }

    /* Glassmorphism cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        border-color: rgba(0, 245, 255, 0.5);
        box-shadow: 0 12px 40px rgba(0, 245, 255, 0.3);
    }

    /* Neon headers */
    h1, h2, h3 {
        color: #00f5ff !important;
        text-shadow: 0 0 20px rgba(0, 245, 255, 0.5),
                     0 0 40px rgba(0, 245, 255, 0.3);
        font-weight: 800;
    }

    /* Enhanced buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00f5ff, #ff00ff);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        box-shadow: 0 4px 20px rgba(0, 245, 255, 0.4);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 30px rgba(0, 245, 255, 0.6);
    }

    /* Alert boxes */
    .stAlert {
        background: rgba(255, 100, 100, 0.1);
        border-left: 4px solid #ff00ff;
        border-radius: 8px;
    }

    /* Leaderboard table */
    .leaderboard-row {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 0.5rem 1rem;
        margin: 0.25rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title with shimmer animation (now properly defined above)
st.markdown("""
<h1 style='
    font-size: 3.5rem;
    text-align: center;
    background: linear-gradient(90deg, #00f5ff 0%, #ff00ff 50%, #00f5ff 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s linear infinite;
    margin-bottom: 0;
'>
🎯 Quality Intelligence Dashboard
</h1>
<p style='text-align: center; color: #888; font-size: 1.3rem; margin-top: 0;'>
Real-time Analytics • AI-Powered Insights • Performance Monitoring
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar with enhanced controls
with st.sidebar:
    st.markdown("### ⚙️ Dashboard Controls")

    # Date range selector
    date_range = st.selectbox(
        "📅 Time Period",
        ["Last 7 Days", "Last 14 Days", "Last 30 Days", "Last Quarter"]
    )

    days_map = {
        "Last 7 Days": 7,
        "Last 14 Days": 14,
        "Last 30 Days": 30,
        "Last Quarter": 90,
    }
    selected_days = days_map[date_range]

    # Metric selector — these now actually control visibility below
    st.markdown("### 📊 Metrics to Display")
    show_quality = st.checkbox("Quality Score", value=True)
    show_compliance = st.checkbox("Compliance Rate", value=True)
    show_sentiment = st.checkbox("Sentiment Analysis", value=True)
    show_escalation = st.checkbox("Escalation Rate", value=True)
    show_trends = st.checkbox("Trend Charts", value=True)

    # Refresh button
    st.markdown("---")
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

    # Auto-refresh — use HTML meta refresh instead of time.sleep (which blocked UI)
    auto_refresh = st.checkbox("⚡ Auto-refresh (30s)", value=False)
    if auto_refresh:
        st.markdown('<meta http-equiv="refresh" content="30">', unsafe_allow_html=True)
        st.caption("🔄 Page refreshes every 30 seconds")

# Generate sample data filtered by the selected date range
@st.cache_data(ttl=300)
def load_dashboard_data(days: int):
    """Load dashboard metrics filtered to the selected number of days."""
    np.random.seed(42)

    data = {
        'total_calls': np.random.randint(800, 1200),
        'quality_score': np.random.uniform(75, 95),
        'compliance_rate': np.random.uniform(85, 98),
        'avg_sentiment': np.random.uniform(0.6, 0.9),
        'escalation_rate': np.random.uniform(5, 15),
        'resolution_rate': np.random.uniform(80, 95),
    }

    # Trend data filtered to selected period
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    trends = pd.DataFrame({
        'date': dates,
        'quality_score': np.random.uniform(70, 95, days) + np.linspace(0, 10, days),
        'calls': np.random.randint(20, 50, days),
        'compliance': np.random.uniform(85, 98, days),
        'escalation_rate': np.random.uniform(5, 15, days),
    })

    # Agent leaderboard data
    agents = [f"Agent {i:03d}" for i in range(1, 11)]
    agent_data = pd.DataFrame({
        'Agent': agents,
        'Calls': np.random.randint(50, 150, 10),
        'Quality': np.round(np.random.uniform(70, 98, 10), 1),
        'Compliance': np.round(np.random.uniform(80, 99, 10), 1),
        'Sentiment': np.round(np.random.uniform(0.5, 0.95, 10), 2),
    }).sort_values('Quality', ascending=False).reset_index(drop=True)
    agent_data.index += 1  # Rank starts at 1

    return data, trends, agent_data

data, trends, agent_data = load_dashboard_data(selected_days)

# === TOP METRICS ROW ===
st.markdown("## 📈 Key Performance Indicators")

# Build visible metrics list based on sidebar checkboxes
visible_metrics = []
if show_quality:
    visible_metrics.append(("⭐ Quality Score", f"{data['quality_score']:.1f}%", "+2.3%", "Average quality score"))
if show_compliance:
    visible_metrics.append(("✅ Compliance", f"{data['compliance_rate']:.1f}%", "+0.8%", "Compliance rate"))
if show_sentiment:
    visible_metrics.append(("😊 Sentiment", f"{data['avg_sentiment']:.2f}", "+0.05", "Average customer sentiment"))
if show_escalation:
    delta_esc = f"+{data['escalation_rate']:.1f}%" if data['escalation_rate'] > 10 else f"-{10 - data['escalation_rate']:.1f}%"
    visible_metrics.append(("🔺 Escalation Rate", f"{data['escalation_rate']:.1f}%", delta_esc, "% of calls escalated"))

# Always show total calls
all_metrics = [("📞 Total Calls", f"{data['total_calls']:,}", "+12.5%", "Total calls processed")] + visible_metrics

cols = st.columns(len(all_metrics)) if all_metrics else []
for col, (label, value, delta, help_text) in zip(cols, all_metrics):
    with col:
        st.metric(label, value, delta=delta, help=help_text)

st.markdown("---")

# === CHARTS ROW (only if trends enabled) ===
if show_trends:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Quality Score Trend")

        fig_quality = go.Figure()
        fig_quality.add_trace(go.Scatter(
            x=trends['date'],
            y=trends['quality_score'],
            mode='lines+markers',
            name='Quality Score',
            line=dict(color='#00f5ff', width=3),
            fill='tozeroy',
            fillcolor='rgba(0, 245, 255, 0.2)',
            marker=dict(size=8, color='#00f5ff', line=dict(color='white', width=2))
        ))
        fig_quality.add_hline(
            y=85,
            line_dash="dash",
            line_color="red",
            annotation_text="Target: 85%",
            annotation_position="right"
        )
        fig_quality.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', range=[60, 100]),
            height=350,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig_quality, use_container_width=True)

    with col2:
        st.markdown("### 📞 Daily Call Volume")

        fig_calls = go.Figure()
        fig_calls.add_trace(go.Bar(
            x=trends['date'],
            y=trends['calls'],
            name='Calls',
            marker=dict(
                color=trends['calls'],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Calls")
            )
        ))
        fig_calls.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            height=350,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig_calls, use_container_width=True)

    st.markdown("---")

# === PERFORMANCE BREAKDOWN ===
st.markdown("## 🎯 Performance Breakdown")

gauge_cols = []
gauge_configs = []

if show_quality:
    gauge_configs.append(("Quality Score", data['quality_score'], "#00f5ff", 85,
                          [{'range': [0, 60], 'color': 'rgba(255,0,0,0.3)'},
                           {'range': [60, 85], 'color': 'rgba(255,255,0,0.3)'},
                           {'range': [85, 100], 'color': 'rgba(0,255,0,0.3)'}]))
if show_compliance:
    gauge_configs.append(("Compliance Rate", data['compliance_rate'], "#ff00ff", 95,
                          [{'range': [0, 80], 'color': 'rgba(255,0,0,0.3)'},
                           {'range': [80, 95], 'color': 'rgba(255,255,0,0.3)'},
                           {'range': [95, 100], 'color': 'rgba(0,255,0,0.3)'}]))
# Resolution rate gauge always shown
gauge_configs.append(("Resolution Rate", data['resolution_rate'], "#00ff00", None, []))

if gauge_configs:
    gauge_cols = st.columns(len(gauge_configs))
    for col, (title, value, color, threshold, steps) in zip(gauge_cols, gauge_configs):
        fig_g = go.Figure(go.Indicator(
            mode="gauge+number+delta" if threshold else "gauge+number",
            value=value,
            delta={'reference': threshold, 'increasing': {'color': color}} if threshold else None,
            title={'text': title, 'font': {'color': 'white'}},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': 'white'},
                'bar': {'color': color},
                'bgcolor': 'rgba(255,255,255,0.1)',
                'bordercolor': 'white',
                'steps': steps,
                'threshold': {
                    'line': {'color': 'white', 'width': 4},
                    'thickness': 0.75,
                    'value': threshold
                } if threshold else {}
            }
        ))
        fig_g.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'}, height=250)
        with col:
            st.plotly_chart(fig_g, use_container_width=True)

st.markdown("---")

# === AGENT LEADERBOARD ===
st.markdown("## 🏆 Agent Leaderboard")

leader_col1, leader_col2 = st.columns([2, 1])

with leader_col1:
    # Color-code Quality column
    def quality_color(val):
        if val >= 90:
            return 'color: #00ff88'
        elif val >= 80:
            return 'color: #ffaa00'
        else:
            return 'color: #ff4444'

    styled = (
        agent_data.style
        .applymap(quality_color, subset=['Quality'])
        .format({'Quality': '{:.1f}%', 'Compliance': '{:.1f}%', 'Sentiment': '{:.2f}'})
        .set_table_styles([
            {'selector': 'th', 'props': [('color', '#00f5ff'), ('background-color', 'rgba(0,0,0,0)')]},
        ])
    )
    st.dataframe(styled, use_container_width=True, height=320)

with leader_col2:
    # Top vs bottom performers mini chart
    top5 = agent_data.head(5)
    bot5 = agent_data.tail(5)

    fig_lb = go.Figure()
    fig_lb.add_trace(go.Bar(
        name='Top 5',
        x=top5['Agent'],
        y=top5['Quality'],
        marker_color='#00f5ff'
    ))
    fig_lb.add_trace(go.Bar(
        name='Bottom 5',
        x=bot5['Agent'],
        y=bot5['Quality'],
        marker_color='#ff00ff'
    ))
    fig_lb.update_layout(
        title='Top vs Bottom Performers',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=11),
        height=300,
        barmode='group',
        margin=dict(l=0, r=0, t=30, b=0),
        legend=dict(font=dict(color='white'))
    )
    st.plotly_chart(fig_lb, use_container_width=True)

st.markdown("---")

# === AI INSIGHTS ===
st.markdown("## 🤖 AI-Powered Insights")

insights_col1, insights_col2 = st.columns(2)

with insights_col1:
    st.success("""
    **📈 Trending Upward**
    - Quality scores improved by 2.3% this week
    - Compliance rate exceeded target (98% vs 95%)
    - Customer sentiment showing positive trend
    """)

    st.info("""
    **💡 Optimization Opportunities**
    - Peak call times: 2–4 PM (prepare more agents)
    - Top performing agents available for training sessions
    - Script version A performing 15% better than B
    """)

with insights_col2:
    st.warning("""
    **⚠️ Attention Required**
    - Escalation rate slightly elevated (12% vs target 10%)
    - Average handle time increased by 30 seconds
    - 3 agents below quality threshold
    """)

    st.error("""
    **🚨 Critical Alerts**
    - Compliance violation detected in Campaign XYZ
    - System downtime: 15 minutes on Feb 22
    - Missing data for 2 agents today
    """)

st.markdown("---")

# === QUICK ACTIONS ===
st.markdown("## ⚡ Quick Actions")

action_col1, action_col2, action_col3, action_col4 = st.columns(4)

with action_col1:
    # Generate a full CSV report immediately on click
    report_df = pd.DataFrame({
        'Metric': ['Total Calls', 'Quality Score', 'Compliance Rate',
                   'Avg Sentiment', 'Escalation Rate', 'Resolution Rate'],
        'Value': [
            data['total_calls'],
            f"{data['quality_score']:.1f}%",
            f"{data['compliance_rate']:.1f}%",
            f"{data['avg_sentiment']:.2f}",
            f"{data['escalation_rate']:.1f}%",
            f"{data['resolution_rate']:.1f}%",
        ],
        'Period': [date_range] * 6,
        'Generated': [datetime.now().strftime("%Y-%m-%d %H:%M")] * 6,
    })
    csv_report = report_df.to_csv(index=False)
    st.download_button(
        "📊 Download Report",
        csv_report,
        f"quality_report_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
        "text/csv",
        use_container_width=True
    )

with action_col2:
    if st.button("📧 Email Summary", use_container_width=True):
        st.info("📬 Configure an email integration in settings to enable this.")

with action_col3:
    with st.popover("🔔 Set Alert", use_container_width=True):
        st.markdown("**Configure Threshold Alert**")
        alert_metric = st.selectbox("Metric", ["Quality Score", "Compliance Rate", "Escalation Rate"])
        alert_threshold = st.number_input("Threshold (%)", min_value=0.0, max_value=100.0, value=85.0)
        alert_direction = st.radio("Alert when", ["Below threshold", "Above threshold"])
        if st.button("✅ Save Alert"):
            st.success(f"Alert set: notify when {alert_metric} is {alert_direction.lower()} {alert_threshold}%")

with action_col4:
    # Export full trend data
    trend_csv = trends.to_csv(index=False)
    st.download_button(
        "💾 Export Trend Data",
        trend_csv,
        f"trend_data_{datetime.now().strftime('%Y%m%d')}.csv",
        "text/csv",
        use_container_width=True
    )

# Footer
st.markdown("---")
st.markdown("""
<p style='text-align: center; color: #666; font-size: 0.9rem;'>
Quality Intelligence Engine V3.0 • Last updated: {} • Period: {} • Auto-refresh: {}
</p>
""".format(
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    date_range,
    "ON" if auto_refresh else "OFF"
), unsafe_allow_html=True)
