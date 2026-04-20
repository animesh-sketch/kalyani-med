import streamlit as st
import json
import base64
from datetime import datetime, date
from data import PRODUCTS, MONTHLY_PLANS, ANNUAL_BUDGET, DEAL_STAGES, LEAD_SOURCES, generate_uuid, get_months

st.set_page_config(page_title="💼 NoventIQ Sales Suite", page_icon="💼", layout="wide", initial_sidebar_state="expanded")

# ============== PREMIUM CSS ==============
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    * { font-family: 'Inter', sans-serif; }
    
    .hero-header { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%); padding: 2rem; border-radius: 16px; color: white; text-align: center; margin-bottom: 1.5rem; }
    .hero-header h1 { font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem; }
    .hero-header h3 { font-size: 1.1rem; font-weight: 400; opacity: 0.9; }
    .hero-header p { font-size: 0.85rem; opacity: 0.7; margin-top: 0.5rem; }
    
    .glass-card { background: white; border-radius: 14px; padding: 1.25rem; box-shadow: 0 3px 15px rgba(0,0,0,0.08); }
    .metric-tile { background: linear-gradient(145deg, #f1f5f9, #e2e8f0); border-radius: 10px; padding: 1rem; text-align: center; }
    .metric-value { font-size: 1.5rem; font-weight: 700; color: #0f172a; }
    .metric-label { font-size: 0.65rem; color: #64748b; text-transform: uppercase; }
    
    .stButton > button { background: linear-gradient(135deg, #0f172a, #334155); color: white; border: none; padding: 0.5rem 1rem; border-radius: 8px; font-weight: 600; }
    .stButton > button:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
    
    .section-title { font-size: 1.1rem; font-weight: 600; color: #0f172a; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem; }
    .form-section { background: white; border-radius: 14px; padding: 1.25rem; box-shadow: 0 2px 12px rgba(0,0,0,0.06); }
    
    .status-lead { background: #dbeafe; color: #1d4ed8; }
    .status-qualified { background: #fef3c7; color: #b45309; }
    .status-proposal { background: #dbeafe; color: #1d4ed8; }
    .status-negotiation { background: #ede9fe; color: #7c3aed; }
    .status-won { background: #dcfce7; color: #15803d; }
    .status-lost { background: #fee2e2; color: #dc2626; }
    
    .insight-card { background: linear-gradient(135deg, #f0f9ff, #e0f2fe); border-left: 4px solid #0284c7; padding: 0.75rem; border-radius: 8px; margin: 0.5rem 0; }
    .alert-card { background: #fef2f2; border-left: 4px solid #dc2626; padding: 0.75rem; border-radius: 8px; }
    .success-card { background: #f0fdf4; border-left: 4px solid #16a34a; padding: 0.75rem; border-radius: 8px; }
    
    .script-box { background: #1e293b; color: #e2e8f0; padding: 0.75rem; border-radius: 8px; font-family: monospace; font-size: 0.8rem; }
    .objection-card { background: #fffbeb; border-left: 4px solid #f59e0b; padding: 0.75rem; border-radius: 8px; margin: 0.5rem 0; }
    
    .pa-user { text-align: right; background: #dbeafe; padding: 0.5rem 0.75rem; border-radius: 10px; margin: 0.25rem 0; }
    .pa-assistant { text-align: left; background: white; padding: 0.5rem 0.75rem; border-radius: 10px; margin: 0.25rem 0; }
    
    .kpi-good { background: #dcfce7; color: #166534; }
    .kpi-medium { background: #fef3c7; color: #92400e; }
    .kpi-bad { background: #fee2e2; color: #991b1b; }
    
    .sidebar-stat { background: white; padding: 0.75rem; border-radius: 8px; margin-bottom: 0.5rem; }
    
    .nav-button { width: 100%; padding: 0.75rem; margin: 0.25rem 0; border-radius: 8px; text-align: left; }
    .nav-button-active { background: linear-gradient(135deg, #0f172a, #334155); color: white; }
    .nav-button-inactive { background: white; color: #0f172a; }
</style>
""", unsafe_allow_html=True)

# ============== DATA INITIALIZATION ==============
if 'accounts' not in st.session_state: st.session_state['accounts'] = []
if 'campaigns' not in st.session_state: st.session_state['campaigns'] = []
if 'events' not in st.session_state: st.session_state['events'] = []
if 'tasks' not in st.session_state: st.session_state['tasks'] = []
if 'notifications' not in st.session_state: st.session_state['notifications'] = []
if 'chat_history' not in st.session_state: st.session_state['chat_history'] = []
if 'meeting_notes' not in st.session_state: st.session_state['meeting_notes'] = []
if 'competitors' not in st.session_state: st.session_state['competitors'] = []
if 'products' not in st.session_state: st.session_state['products'] = []
if 'current_page' not in st.session_state: st.session_state['current_page'] = "AI Assistant"

# ============== OBJECTIONS DATA ==============
OBJECTIONS = {
    "expensive": {"question": "Too expensive", "script": "I understand. Our ROI shows 3x value in Year 1. Want me to show TCO comparison?", "positioning": "Show ROI, not price"},
    "not_interested": {"question": "Not interested", "script": "What would need to change? I'll send resources for when timing is right.", "positioning": "Timing & education"},
    "already_vendor": {"question": "Have vendor", "script": "Great you've solution. We complement for specific workloads. Compare?", "positioning": "Complement not replace"},
    "security": {"question": "Security concerns", "script": "We're SOC 2 Type II certified. Connect with security team?", "positioning": "Certifications"},
    "need_approval": {"question": "Need approval", "script": "Let's build business case together. What's approval process?", "positioning": "Enable champion"},
    "no_rush": {"question": "No urgency", "script": "Risks of waiting? Q4 pricing ends soon. What's driving delay?", "positioning": "Create urgency"}
}

# ============== SALES SCRIPTS ==============
SCRIPTS = {
    "cold_call": "Hi {name}, {your_name} from NoventIQ. Got 30 seconds?\n\nWhat's your biggest tech challenge right now?\n\nBased on that, we might help. Quick 15-min no-commitment?",
    "discovery": "1. Current state vs goal?\n2. Who else in decision?\n3. What's driving now?\n4. Timeline?\n5. What does success look like?",
    "demo_close": "✓ Solves {problem}\n✓ ROI {months} months\n✓ Implementation {weeks} weeks\n\nNext: Pilot next {date}. Ready to proceed?",
    "objection": "1. Listen\n2. Acknowledge\n3. Validate\n4. Probe why\n5. Reframe\n6. Evidence\n7. Confirm resolved"
}

# ============== EMAIL TEMPLATES ==============
EMAILS = {
    "follow_up": "Hi {name},\n\nGreat meeting! Summary:\n- Action: {action}\n- Next: {next_step}\n\n{resources}\n\nBest,\n{your_name}",
    "value_prop": "Hi {name},\n\nHelped {similar_company} achieve {result}. Brief: {summary}\n\n15-min call to explore fit?\n\nBest,\n{your_name}",
    "proposal": "Hi {name},\n\nProposal attached:\n- Solution: {solution}\n- Investment: {price}\n- Timeline: {timeline}\n- ROI: {roi}\n\nWalk through? This week?\n\nBest,\n{your_name}"
}

# ============== SIDEBAR - NAVIGATION ==============
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    
    # Page selection
    page = st.radio("Select View", ["🤖 AI Assistant", "📊 Sales Head Dashboard"], 
                   index=0 if st.session_state['current_page'] == "AI Assistant" else 1)
    
    st.session_state['current_page'] = "AI Assistant" if "AI" in page else "Sales Head"
    
    st.markdown("---")
    
    accounts = st.session_state.get('accounts', [])
    total_pipe = sum([a.get('potential', 0) for a in accounts])
    weighted_pipe = sum([a.get('potential', 0) * a.get('probability', 50)/100 for a in accounts])
    
    st.markdown("### 💼 Quick Stats")
    c1, c2, c3 = st.columns(3)
    c1.metric("📁", len(accounts))
    c2.metric("💰", f"{total_pipe/10000000:.1f}Cr")
    c3.metric("📢", len(st.session_state.get('campaigns', [])))
    
    st.markdown("---")
    st.markdown("### 🔔 Reminders")
    for n in st.session_state.get('notifications', [])[-3:]:
        st.info(n)

# ============== RENDER BASED ON SELECTED PAGE ==============

ASSISTANT_NAME = "Nova"
ASSISTANT_AVATAR = "👩‍💼"

if st.session_state['current_page'] == "AI Assistant":
    st.markdown(f"""
    <div class="hero-header">
        <h1>{ASSISTANT_AVATAR} {ASSISTANT_NAME} - Your Sales Partner</h1>
        <h3>AI-Powered Sales Assistant | Scripts, Objections, Deals, Strategies</h3>
        <p>AWS | Gen AI | Agentic AI | DMAL | Citrix | Managed Services | Security</p>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs([
        f"💬 Chat with {ASSISTANT_NAME}", "📞 Scripts", "⚠️ Objections", "📧 Emails", 
        "🎯 Deal Prep", "📊 Analytics", "📋 Notes", "🛠️ Tools"
    ])
    
    # TAB 1: CHAT
    with tabs[0]:
        col_ai1, col_ai2 = st.columns([1, 3])
        
        with col_ai1:
            st.markdown(f"#### 💡 Quick Actions with {ASSISTANT_NAME}")
            quick_actions = [
                ("📞 Cold Call", "cold call"),
                ("🔍 Discovery", "discovery"),
                ("⚠️ Handle Objection", "objection"),
                ("🎯 Close Deal", "close"),
                ("📧 Follow Up", "follow up"),
                ("💰 Commission", "commission"),
                ("🎤 Meeting Prep", "meeting prep"),
                ("📈 Pipeline Review", "pipeline review")
            ]
            for label, action in quick_actions:
                if st.button(label, use_container_width=True):
                    st.session_state['chat_history'].append({"role": "user", "content": action})
        
        with col_ai2:
            st.markdown(f"#### 💬 Chat with {ASSISTANT_NAME}")
            question = st.text_input(f"Ask {ASSISTANT_NAME} anything...", placeholder="e.g., How do I handle 'too expensive'?")
            if st.button(f"Ask {ASSISTANT_NAME}", use_container_width=True) and question:
                q = question.lower()
                response = ""
                
                if "close" in q or "closing" in q:
                    response = SCRIPTS.get('demo_close', '').format(problem="your challenge", months=3, weeks=4, date="month")
                elif "objection" in q:
                    response = "**7-Step Objection Handling:**\n1. Listen\n2. Acknowledge\n3. Validate\n4. Probe why\n5. Reframe\n6. Evidence\n7. Confirm resolved"
                elif "discovery" in q:
                    response = SCRIPTS.get('discovery', '')
                elif "cold call" in q or "call script" in q:
                    response = SCRIPTS.get('cold_call', '').format(name="there", your_name="Animesh")
                elif "follow up" in q or "email template" in q:
                    response = EMAILS.get('follow_up', '').format(name="Contact", action="Discussed pricing", next_step="Demo next week", resources="Attached case study", your_name="Animesh")
                elif "commission" in q or "commission" in q:
                    response = "I'll calculate your commission! Use the Tools tab or tell me your deal value and quota attainment."
                elif "meeting prep" in q:
                    response = "**Meeting Prep Checklist:**\n\n1. Review account history & previous conversations\n2. Check their company news/press releases\n3. Prepare 3 discovery questions\n4. Have objection responses ready\n5. Set meeting agenda & goals\n6. Prepare relevant case studies"
                elif "pipeline review" in q or "pipeline" in q:
                    accs = st.session_state.get('accounts', [])
                    total = sum([a.get('potential', 0) for a in accs])
                    weighted = sum([a.get('potential', 0) * a.get('probability', 50)/100 for a in accs])
                    response = f"**Pipeline Summary:**\n- Total: ₹{total/10000000:.1f}Cr\n- Weighted: ₹{weighted/10000000:.1f}Cr\n- Deals: {len(accs)}\n- Avg Deal: ₹{total/max(len(accs),1)/100000:.0f}L"
                elif "product" in q or "recommend" in q:
                    response = "**Product Recommendations:**\n\n- **AWS Cloud**: Enterprise workloads, migration\n- **Gen AI**: Innovation, automation\n- **Agentic AI**: Autonomous workflows\n- **DMAL**: Data & marketing\n- **Citrix**: Remote work, virtualization\n- **Security**: Zero trust, compliance"
                else:
                    response = f"Hi! I'm {ASSISTANT_NAME}, your sales partner. I can help with:\n\n📞 Cold call & discovery scripts\n⚠️ Objection handling\n📧 Email templates\n🎯 Closing techniques\n💰 Commission calculator\n🎤 Meeting preparation\n📈 Pipeline analysis\n\nWhat would you like help with?"
                
                st.session_state['chat_history'].append({"role": "user", "content": question})
                st.session_state['chat_history'].append({"role": "assistant", "content": response})
            
            st.markdown("---")
            for chat in st.session_state.get('chat_history', [])[-6:]:
                if chat['role'] == 'user':
                    st.markdown(f"""<div class="pa-user"><strong>You:</strong> {chat['content']}</div>""", unsafe_allow_html=True)
                else:
                    st.markdown(f"""<div class="pa-assistant"><strong>{ASSISTANT_AVATAR} {ASSISTANT_NAME}:</strong> {chat['content'][:200]}{'...' if len(chat['content']) > 200 else ''}</div>""", unsafe_allow_html=True)
            
            if st.button("🗑️ Clear Chat"):
                st.session_state['chat_history'] = []
    
    # TAB 2: SCRIPTS
    with tabs[1]:
        st.markdown("### 📞 Sales Scripts")
        
        script_tabs = st.tabs(["Cold Call", "Discovery", "Demo Close", "Objection"])
        
        with script_tabs[0]:
            st.markdown("#### 📞 Cold Call Script")
            st.code(SCRIPTS['cold_call'].format(name="[Name]", your_name="[Your Name]"), language="text")
        
        with script_tabs[1]:
            st.markdown("#### 🔍 Discovery Questions")
            st.code(SCRIPTS['discovery'], language="text")
        
        with script_tabs[2]:
            st.markdown("#### 🎯 Demo Close Script")
            st.code(SCRIPTS['demo_close'].format(problem="your challenge", months=3, weeks=4, date="Friday"), language="text")
        
        with script_tabs[3]:
            st.markdown("#### ⚠️ Objection Response")
            st.code(SCRIPTS['objection'], language="text")
    
    # TAB 3: OBJECTIONS
    with tabs[2]:
        st.markdown("### ⚠️ Objection Handling")
        
        col_obj1, col_obj2 = st.columns(2)
        
        with col_obj1:
            for key, obj in list(OBJECTIONS.items())[:3]:
                with st.expander(f"⚠️ {obj.get('question')}"):
                    st.markdown(f"**Script:** {obj.get('script')}")
                    st.markdown(f"*Positioning: {obj.get('positioning')}*")
        
        with col_obj2:
            for key, obj in list(OBJECTIONS.items())[3:]:
                with st.expander(f"⚠️ {obj.get('question')}"):
                    st.markdown(f"**Script:** {obj.get('script')}")
                    st.markdown(f"*Positioning: {obj.get('positioning')}*")
    
    # TAB 4: EMAILS
    with tabs[3]:
        st.markdown("### 📧 Email Templates")
        
        email_tabs = st.tabs(["Follow Up", "Value Prop", "Proposal"])
        
        with email_tabs[0]:
            st.markdown("#### 📤 Follow Up Email")
            st.code(EMAILS['follow_up'].format(name="[Name]", action="[action]", next_step="[next step]", resources="[resources]", your_name="[Your Name]"), language="text")
        
        with email_tabs[1]:
            st.markdown("#### 💎 Value Proposition")
            st.code(EMAILS['value_prop'].format(name="[Name]", similar_company="[Company]", result="[result]", summary="[summary]", your_name="[Your Name]"), language="text")
        
        with email_tabs[2]:
            st.markdown("#### 📄 Proposal Email")
            st.code(EMAILS['proposal'].format(name="[Name]", solution="[solution]", price="[price]", timeline="[timeline]", roi="[roi]", your_name="[Your Name]"), language="text")
    
    # TAB 5: DEAL PREP
    with tabs[4]:
        st.markdown("### 🎯 Deal Preparation")
        
        col_dp1, col_dp2 = st.columns(2)
        
        with col_dp1:
            st.markdown("#### 📋 Pre-Meeting Checklist")
            checklist = [
                "✓ Research company & recent news",
                "✓ Review past interactions",
                "✓ Prepare discovery questions",
                "✓ Anticipate objections",
                "✓ Prepare relevant case studies",
                "✓ Set clear meeting objective",
                "✓ Prepare demo/overview"
            ]
            for item in checklist:
                st.checkbox(item, value=True)
            
            st.markdown("---")
            st.markdown("#### 💡 Sales Strategies")
            strategies = [
                ("🔍 Needs Discovery", "Ask open-ended questions first"),
                ("📊 ROI First", "Lead with business value"),
                ("⏰ Create Urgency", "Use timing strategically"),
                ("👥 Map the Account", "Identify all stakeholders")
            ]
            for title, desc in strategies:
                st.markdown(f"""<div class="insight-card">{title} - {desc}</div>""", unsafe_allow_html=True)
        
        with col_dp2:
            st.markdown("#### 🏆 Winning Tactics")
            tactics = [
                "Always ask 'why now?' to create urgency",
                "Get executive sponsorship early",
                "Quantify value with customer metrics",
                "Address objections as opportunities",
                "Ask for the business twice",
                "Follow up within 24 hours"
            ]
            for t in tactics:
                st.info(t)
    
    # TAB 6: ANALYTICS
    with tabs[5]:
        st.markdown("### 📊 Sales Analytics")
        
        accounts = st.session_state.get('accounts', [])
        total = sum([a.get('potential', 0) for a in accounts])
        weighted = sum([a.get('potential', 0) * a.get('probability', 50)/100 for a in accounts])
        
        cols = st.columns(4)
        with cols[0]: st.metric("Total Pipeline", f"₹{total/10000000:.1f}Cr")
        with cols[1]: st.metric("Weighted", f"₹{weighted/10000000:.1f}Cr")
        with cols[2]: st.metric("Deals", len(accounts))
        with cols[3]: st.metric("Win Rate", f"{len([a for a in accounts if a.get('stage')=='Closed Won'])/max(len(accounts),1)*100:.0f}%")
        
        st.markdown("#### 📈 By Stage")
        for stage in DEAL_STAGES:
            stage_deals = [a for a in accounts if a.get('stage') == stage]
            if stage_deals:
                val = sum([d.get('potential', 0) for d in stage_deals])/10000000
                st.write(f"**{stage}:** {len(stage_deals)} deals - ₹{val:.1f}Cr")
        
        st.markdown("#### 📦 By Product")
        for p in PRODUCTS:
            p_deals = [a for a in accounts if p in a.get('products', [])]
            if p_deals:
                val = sum([d.get('potential', 0) for d in p_deals])/10000000
                st.write(f"**{p}:** {len(p_deals)} deals - ₹{val:.1f}Cr")
    
    # TAB 7: NOTES
    with tabs[6]:
        st.markdown("### 📋 Meeting Notes")
        
        col_n1, col_n2 = st.columns([1, 2])
        
        with col_n1:
            with st.form("add_note"):
                st.markdown(f"#### 📝 New Note for {ASSISTANT_NAME}")
                note_title = st.text_input("Title")
                note_account = st.selectbox("Account", [""] + [a.get('name', '') for a in accounts])
                note_content = st.text_area("Notes", height=100)
                note_tags = st.multiselect("Tags", ["Call", "Meeting", "Follow-up", "Important", "Action Item"])
                
                if st.form_submit_button("Save Note"):
                    st.session_state['meeting_notes'].append({
                        "id": generate_uuid(),
                        "title": note_title,
                        "account": note_account,
                        "content": note_content,
                        "tags": note_tags,
                        "date": str(date.today())
                    })
                    st.success("Saved!")
        
        with col_n2:
            st.markdown("#### 📚 Recent Notes")
            for note in st.session_state.get('meeting_notes', [])[-10:]:
                with st.expander(f"📝 {note.get('title')} - {note.get('date')}"):
                    st.write(f"**Account:** {note.get('account')}")
                    st.write(f"**Content:** {note.get('content')}")
                    st.write(f"**Tags:** {', '.join(note.get('tags', []))}")
    
    # TAB 8: TOOLS
    with tabs[7]:
        st.markdown(f"### 🛠️ Tools & {ASSISTANT_NAME}'s Resources")
        
        col_t1, col_t2 = st.columns(2)
        
        with col_t1:
            st.markdown("#### 💰 Commission Calculator")
            deal = st.number_input("Deal Value (₹)", value=1000000, key="comm_deal")
            attainment = st.slider("Quota Attainment %", 0, 200, 100, key="comm_attainment")
            
            rate = 5
            if attainment > 100: rate = 10
            elif attainment >= 80: rate = 7
            
            commission = deal * rate / 100
            st.metric("Commission", f"₹{commission:,.0f}")
            st.caption(f"Rate: {rate}% (attainment: {attainment}%)")
            
            st.markdown("---")
            
            st.markdown("#### ⚔️ Competitor Analysis")
            with st.form("competitor"):
                c_name = st.text_input("Competitor")
                c_strength = st.text_area("Strengths")
                c_weakness = st.text_area("Weaknesses")
                if st.form_submit_button("Add"):
                    st.session_state['competitors'].append({
                        "name": c_name, "strengths": c_strength, "weaknesses": c_weakness
                    })
                    st.success("Added!")
            
            for comp in st.session_state.get('competitors', []):
                with st.expander(f"⚔️ {comp.get('name')}"):
                    st.write(f"**Strengths:** {comp.get('strengths')}")
                    st.write(f"**Weaknesses:** {comp.get('weaknesses')}")
        
        with col_t2:
            st.markdown("#### 💡 Daily Tips")
            tips = [
                "Always lead with questions, not solutions",
                "Know the customer's budget before demonstrating",
                "Handle objections as opportunities",
                "Ask for the business at least twice",
                "Follow up within 24 hours of any meeting",
                "Record every meeting for later review"
            ]
            for tip in tips:
                st.info(tip)
            
            st.markdown("---")
            
            st.markdown("#### 📋 Product Positioning")
            for p, info in PRODUCTS.items():
                with st.expander(f"{p}"):
                    st.write(f"**Deal Size:** {info.get('deal_size', 'Various')}")
                    st.write(f"**Target:** {info.get('target_segment', 'All')}")

else:
    # ========== SALES HEAD DASHBOARD PAGE ==========
    st.markdown("""
    <div class="hero-header">
        <h1>📊 Sales Head Dashboard</h1>
        <h3>CRM | Pipeline | Campaigns | Events | Planning | Analytics</h3>
        <p>AWS | Gen AI | Agentic AI | DMAL | Citrix | Managed Services | Security</p>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs(["📊 Dashboard", "🏢 Accounts", "💰 Pipeline", "📢 Campaigns", "🎪 Events", "📅 Calendar", "✅ Tasks", "📋 Planning", "📈 Reports"])
    
    accounts = st.session_state.get('accounts', [])
    total_pipe = sum([a.get('potential', 0) for a in accounts])
    weighted_pipe = sum([a.get('potential', 0) * a.get('probability', 50)/100 for a in accounts])
    
    # TAB 1: DASHBOARD
    with tabs[0]:
        st.markdown("## 📊 Executive Dashboard")
        
        cols = st.columns(4)
        with cols[0]: st.markdown("""<div class="metric-tile"><div class="metric-value">{}</div><div class="metric-label">Accounts</div></div>""".format(len(accounts)), unsafe_allow_html=True)
        with cols[1]: st.markdown("""<div class="metric-tile"><div class="metric-value">₹{:.1f}Cr</div><div class="metric-label">Pipeline</div></div>""".format(total_pipe/10000000), unsafe_allow_html=True)
        with cols[2]: st.markdown("""<div class="metric-tile"><div class="metric-value">₹{:.1f}Cr</div><div class="metric-label">Weighted</div></div>""".format(weighted_pipe/10000000), unsafe_allow_html=True)
        with cols[3]: st.markdown("""<div class="metric-tile"><div class="metric-value">{}</div><div class="metric-label">Tasks</div></div>""".format(len(st.session_state.get('tasks', []))), unsafe_allow_html=True)
        
        col_i1, col_i2 = st.columns(2)
        with col_i1:
            st.markdown("### 💡 Top Insights")
            if accounts:
                prods = {}
                for a in accounts:
                    for p in a.get('products', []):
                        prods[p] = prods.get(p, 0) + 1
                if prods:
                    top = max(prods.items(), key=lambda x: x[1])
                    st.markdown(f"""<div class="insight-card">🔥 Top: {top[0]} ({top[1]} deals)</div>""", unsafe_allow_html=True)
                st.markdown(f"""<div class="insight-card">📊 Avg Deal: ₹{total_pipe/max(len(accounts),1)/100000:.0f}L</div>""", unsafe_allow_html=True)
        with col_i2:
            st.markdown("### ⚠️ Action Items")
            overdue = [t for t in st.session_state.get('tasks', []) if t.get('due_date') and t.get('due_date') < str(date.today())]
            if overdue: st.markdown(f"""<div class="alert-card">⚠️ {len(overdue)} overdue tasks</div>""", unsafe_allow_html=True)
            else: st.markdown("""<div class="success-card">✅ All on track!</div>""", unsafe_allow_html=True)
    
    # TAB 2: ACCOUNTS
    with tabs[1]:
        st.markdown("## 🏢 Customer Accounts")
        
        col_a1, col_a2 = st.columns([1, 2])
        
        with col_a1:
            with st.form("new_account"):
                st.markdown("### ➕ Add Account")
                name = st.text_input("Company *")
                contact = st.text_input("Contact *")
                email = st.text_input("Email")
                phone = st.text_input("Phone")
                company_size = st.selectbox("Size", ["Startup", "SMB", "Mid-Market", "Enterprise"])
                industry = st.selectbox("Industry", ["IT", "Finance", "Healthcare", "Manufacturing", "Retail", "Other"])
                products = st.multiselect("Products", list(PRODUCTS.keys()))
                potential = st.number_input("Value (₹)", value=1000000)
                probability = st.slider("Probability %", 0, 100, 50)
                stage = st.selectbox("Stage", DEAL_STAGES)
                
                if st.form_submit_button("Save"):
                    if name:
                        st.session_state['accounts'].append({
                            "id": generate_uuid(), "name": name, "contact": contact,
                            "email": email, "phone": phone, "company_size": company_size,
                            "industry": industry, "products": products, "potential": potential,
                            "probability": probability, "stage": stage, "created": str(date.today())
                        })
                        st.success(f"✅ {name} added!")
        
        with col_a2:
            search = st.text_input("🔍 Search accounts...")
            for acc in accounts:
                if search and search.lower() not in acc.get('name', '').lower(): continue
                stage_class = f"status-{acc.get('stage', 'lead').lower().replace(' ', '-')}"
                with st.expander(f"{acc.get('name')} - ₹{acc.get('potential', 0)/100000:.0f}L"):
                    c1, c2 = st.columns(2)
                    c1.write(f"**Contact:** {acc.get('contact')}")
                    c1.write(f"**Email:** {acc.get('email', '-')}")
                    c2.write(f"**Stage:** {acc.get('stage')}")
                    c2.write(f"**Products:** {', '.join(acc.get('products', []))}")
    
    # TAB 3: PIPELINE
    with tabs[2]:
        st.markdown("## 💰 Pipeline Management")
        
        for stage in DEAL_STAGES:
            stage_deals = [a for a in accounts if a.get('stage') == stage]
            if stage_deals:
                with st.expander(f"{stage} ({len(stage_deals)}) - ₹{sum([d.get('potential', 0) for d in stage_deals])/10000000:.1f}Cr"):
                    for d in stage_deals:
                        st.write(f"• {d.get('name')} - ₹{d.get('potential', 0)/100000:.0f}L ({d.get('probability', 0)}%)")
    
    # TAB 4: CAMPAIGNS
    with tabs[3]:
        st.markdown("## 📢 Marketing Campaigns")
        
        col_c1, col_c2 = st.columns([1, 2])
        
        with col_c1:
            with st.form("new_campaign"):
                st.markdown("### ➕ Create Campaign")
                name = st.text_input("Name *")
                product = st.selectbox("Product", list(PRODUCTS.keys()))
                platform = st.selectbox("Platform", ["LinkedIn", "Email", "Webinar", "Facebook", "Instagram", "Cold"])
                month = st.selectbox("Month", get_months())
                objective = st.selectbox("Objective", ["Lead Gen", "Awareness", "Conversion"])
                budget = st.number_input("Budget (₹)", value=50000)
                
                if st.form_submit_button("Create"):
                    st.session_state['campaigns'].append({
                        "id": generate_uuid(), "name": name, "product": product,
                        "platform": platform, "month": month, "objective": objective,
                        "budget": budget, "leads": 0, "status": "planned"
                    })
                    st.success("Created!")
        
        with col_c2:
            for c in st.session_state.get('campaigns', []):
                st.write(f"📢 **{c.get('name')}** - {c.get('product')} ({c.get('platform')}) - {c.get('month')}")
    
    # TAB 5: EVENTS
    with tabs[4]:
        st.markdown("## 🎪 Customer Events")
        
        col_e1, col_e2 = st.columns([1, 2])
        
        with col_e1:
            with st.form("new_event"):
                st.markdown("### ➕ Create Event")
                name = st.text_input("Name *")
                event_type = st.selectbox("Type", ["Customer Meet", "Webinar", "Workshop", "Launch", "Roundtable"])
                month = st.selectbox("Month", get_months())
                venue = st.text_input("Venue")
                budget = st.number_input("Budget (₹)", value=100000)
                expected = st.number_input("Expected Leads", value=20)
                
                if st.form_submit_button("Create"):
                    st.session_state['events'].append({
                        "id": generate_uuid(), "name": name, "type": event_type,
                        "month": month, "venue": venue, "budget": budget,
                        "expected_leads": expected, "actual_leads": 0
                    })
                    st.success("Created!")
        
        with col_e2:
            for e in st.session_state.get('events', []):
                st.write(f"🎪 **{e.get('name')}** - {e.get('type')} ({e.get('month')})")
    
    # TAB 6: CALENDAR
    with tabs[5]:
        st.markdown("## 📅 Sales Calendar")
        
        selected = st.selectbox("View Month", get_months())
        st.markdown(f"### 📅 {selected} Plan")
        
        plan = MONTHLY_PLANS.get(selected, {})
        st.info(f"**Theme:** {plan.get('theme', 'N/A')}")
        st.info(f"**Focus:** {plan.get('focus', 'N/A')}")
        st.info(f"**Budget:** ₹{plan.get('budget', 0):,}")
        
        campaigns = [c for c in st.session_state.get('campaigns', []) if c.get('month') == selected]
        events = [e for e in st.session_state.get('events', []) if e.get('month') == selected]
        
        st.markdown(f"### This Month: {len(campaigns)} campaigns, {len(events)} events")
    
    # TAB 7: TASKS
    with tabs[6]:
        st.markdown("## ✅ Task Manager")
        
        col_t1, col_t2 = st.columns([1, 2])
        
        with col_t1:
            with st.form("new_task"):
                st.markdown("### ➕ Add Task")
                title = st.text_input("Title *")
                due = st.date_input("Due Date")
                priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
                
                if st.form_submit_button("Add"):
                    st.session_state['tasks'].append({
                        "id": generate_uuid(), "title": title,
                        "due_date": str(due), "priority": priority,
                        "status": "pending"
                    })
                    st.success("Added!")
        
        with col_t2:
            for t in st.session_state.get('tasks', []):
                color = "🔴" if t.get('priority') == "Critical" else "🟡" if t.get('priority') == "High" else "🟢"
                st.write(f"{color} {t.get('title')} - {t.get('due_date', 'N/A')}")
    
    # TAB 8: PLANNING
    with tabs[7]:
        st.markdown("## 📋 Sales Planning")
        
        col_p1, col_p2 = st.columns(2)
        
        with col_p1:
            st.markdown("### 📅 Monthly Plans")
            for month, plan in MONTHLY_PLANS.items():
                with st.expander(f"{month}: {plan.get('theme')}"):
                    st.write(f"**Focus:** {plan.get('focus')}")
                    st.write(f"**Budget:** ₹{plan.get('budget'):,}")
        
        with col_p2:
            st.markdown("### 💰 Budget Allocation")
            for category, amount in ANNUAL_BUDGET.get('breakdown', {}).items():
                st.progress(amount/ANNUAL_BUDGET['total'])
                st.caption(f"{category}: ₹{amount:,} ({amount/ANNUAL_BUDGET['total']*100:.0f}%)")
            st.metric("Total", f"₹{ANNUAL_BUDGET['total']:,}")
    
    # TAB 9: REPORTS
    with tabs[8]:
        st.markdown("## 📈 Reports & Analytics")
        
        total = sum([a.get('potential', 0) for a in accounts])
        weighted = sum([a.get('potential', 0) * a.get('probability', 50)/100 for a in accounts])
        
        cols = st.columns(4)
        with cols[0]: st.metric("Total Pipeline", f"₹{total/10000000:.1f}Cr")
        with cols[1]: st.metric("Weighted", f"₹{weighted/10000000:.1f}Cr")
        with cols[2]: st.metric("Avg Deal", f"₹{total/max(len(accounts),1)/100000:.0f}L")
        with cols[3]: st.metric("Win Rate", f"{len([a for a in accounts if a.get('stage')=='Closed Won'])/max(len(accounts),1)*100:.0f}%")
        
        st.markdown("### 📊 By Product")
        for p in PRODUCTS:
            p_deals = [a for a in accounts if p in a.get('products', [])]
            if p_deals:
                st.write(f"**{p}:** {len(p_deals)} deals - ₹{sum([d.get('potential', 0) for d in p_deals])/10000000:.1f}Cr")
        
        # Export
        st.markdown("---")
        data = {"accounts": accounts, "campaigns": st.session_state.get('campaigns', []), "events": st.session_state.get('events', [])}
        b64 = base64.b64encode(json.dumps(data).encode()).decode()
        st.markdown(f'<a href="data:application/json;base64,{b64}" download="sales_data.json">📥 Export Data</a>', unsafe_allow_html=True)

# ============== FOOTER ==============
st.markdown("---")
st.caption("💼 NoventIQ Sales Suite | Navigate between AI Assistant and Sales Head Dashboard using sidebar")
