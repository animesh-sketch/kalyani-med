"""
NoventIQ Sales Manager - Complete Sales Tool
All-in-one CRM, Pipeline, Calendar, Analytics, Tasks, Reports
"""

import streamlit as st
import json
from datetime import datetime, date, timedelta
from typing import List, Dict
import uuid

# ============== ALL DATA ==============
PRODUCTS = {
    "AWS Cloud": {"deal_size": "₹50L - ₹5Cr", "cycle": "3-9 months"},
    "Gen AI": {"deal_size": "₹25L - ₹2Cr", "cycle": "2-6 months"},
    "Agentic AI": {"deal_size": "₹30L - ₹3Cr", "cycle": "3-8 months"},
    "DMAL": {"deal_size": "₹10L - ₹1Cr", "cycle": "2-5 months"},
    "Citrix": {"deal_size": "₹20L - ₹2Cr", "cycle": "3-6 months"},
    "Managed Services": {"deal_size": "₹30L - ₹10Cr", "cycle": "4-12 months"},
    "Security Solutions": {"deal_size": "₹15L - ₹3Cr", "cycle": "3-9 months"},
    "Security Services": {"deal_size": "₹5L - ₹1Cr", "cycle": "1-4 months"}
}

MONTHLY_PLANS = {
    "January": {"theme": "New Year New Beginnings", "focus": "Goal Setting", "budget": 300000},
    "February": {"theme": "Valentine Special", "focus": "Referral Generation", "budget": 250000},
    "March": {"theme": "Q1 Close", "focus": "Year-End Close", "budget": 400000},
    "April": {"theme": "Summer Kickoff", "focus": "Q2 Launch", "budget": 300000},
    "May": {"theme": "Tech Month", "focus": "Technical Workshops", "budget": 350000},
    "June": {"theme": "Mid-Year Assessment", "focus": "H1 Review", "budget": 300000},
    "July": {"theme": "Monsoon Productivity", "focus": "Monsoon Offers", "budget": 280000},
    "August": {"theme": "Back to Business", "focus": "Q3 Acceleration", "budget": 300000},
    "September": {"theme": "Festive Season", "focus": "Diwali Prep", "budget": 400000},
    "October": {"theme": "Diwali Dhamaka", "focus": "Maximum Sales", "budget": 500000},
    "November": {"theme": "Year End Rush", "focus": "Budget Utilization", "budget": 450000},
    "December": {"theme": "Year End Wrap", "focus": "2024 Review", "budget": 200000}
}

ANNUAL_BUDGET = {"total": 2500000, "breakdown": {"Digital Marketing": 1200000, "Events": 500000, "Travel": 400000, "Tools": 200000}}

DEAL_STAGES = ["Lead", "Qualified", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]
LEAD_SOURCES = ["LinkedIn", "Website", "Referral", "Cold Call", "Email", "Event", "Partner", "Other"]
COMPETITORS = ["Accenture", "AWS", "Azure", "Google Cloud", "TCS", "Infosys", "Wipro", " Deloitte", "KPMG", "Others"]

# ============== PPT TEMPLATES ==============
def generate_uuid():
    return str(uuid.uuid4())[:8]

def get_months():
    return list(MONTHLY_PLANS.keys())

PPT_TEMPLATES = {
    "title": '''<div style="text-align:center;padding:80px;background:linear-gradient(135deg,#0e1446,#1a237e,#283593);color:white;">
        <h1 style="font-size:48px;">{title}</h1>
        <h2 style="font-size:28px;opacity:0.9;margin:20px 0;">{subtitle}</h2>
        <p style="font-size:18px;opacity:0.8;margin-top:60px;">{date} | NoventIQ Sales Plan</p>
    </div>''',
    
    "agenda": '''<div style="padding:40px;">
        <h2 style="color:#1a237e;font-size:32px;margin-bottom:30px;">📋 Agenda</h2>
        <ul style="font-size:22px;line-height:2.5;">
            <li>💼 Account Overview</li><li>💰 Pipeline Status</li>
            <li>📢 Marketing Campaigns</li><li>📅 Events Calendar</li>
            <li>💵 Budget & Resources</li><li>🎯 Go-to-Market Strategy</li>
        </ul>
    </div>''',
    
    "products": '''<div style="padding:40px;">
        <h2 style="color:#1a237e;font-size:32px;margin-bottom:30px;">📦 Product Portfolio</h2>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">
            {products}
        </div>
    </div>''',
    
    "dashboard": '''<div style="padding:40px;">
        <h2 style="color:#1a237e;font-size:32px;margin-bottom:30px;">📊 Dashboard Highlights</h2>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:30px;text-align:center;">
            {metrics}
        </div>
    </div>''',
    
    "thankyou": '''<div style="text-align:center;padding:80px;background:linear-gradient(135deg,#1a237e,#283593);color:white;">
        <h1 style="font-size:48px;">🙏 Thank You!</h1>
        <h2 style="font-size:28px;margin:20px 0;">Let's Build Together</h2>
        <p style="font-size:20px;">📧 sales@noventiq.com | 📞 +91 98765 43210</p>
    </div>'''
}

def generate_ppt(accounts, campaigns, events, targets):
    slides = []
    
    # Title
    slides.append({"num":1,"title":title,"content":PPT_TEMPLATES["title"].format(title="NoventIQ Sales Plan",subtitle="FY 2024-25 Strategy",date=datetime.now().strftime("%B %Y"))})
    
    # Agenda
    slides.append({"num":2,"title":"Agenda","content":PPT_TEMPLATES["agenda"]})
    
    # Products
    p_html = ""
    for p,i in PRODUCTS.items():
        p_html += f'<div style="background:white;padding:20px;border-radius:10px;box-shadow:0 2px10px rgba(0,0,0,0.1);"><h4>{p}</h4><p style="color:#666">{i["deal_size"]}</p></div>'
    slides.append({"num":3,"title":"Products","content":PPT_TEMPLATES["products"].format(products=p_html)})
    
    # Dashboard
    m_html = f'''
    <div style="background:#e3f2fd;padding:30px;border-radius:15px;"><h3 style="font-size:36px;color:#1976d2;">{len(accounts)}</h3><p>Accounts</p></div>
    <div style="background:#e8f5e9;padding:30px;border-radius:15px;"><h3 style="font-size:36px;color:#388e3c;">₹{sum([a.get("potential",0) for a in accounts])/10000000:.1f}Cr</h3><p>Pipeline</p></div>
    <div style="background:#fff3e0;padding:30px;border-radius:15px;"><h3 style="font-size:36px;color:#f57c00;">{len(campaigns)}</h3><p>Campaigns</p></div>
    <div style="background:#fce4ec;padding:30px;border-radius:15px;"><h3 style="font-size:36px;color:#c2185b;">{len(events)}</h3><p>Events</p></div>
    '''
    slides.append({"num":4,"title":"Dashboard","content":PPT_TEMPLATES["dashboard"].format(metrics=m_html)})
    
    # Thank You
    slides.append({"num":5,"title":"Thank You","content":PPT_TEMPLATES["thankyou"]})
    
    return slides

# Session state initialization
if 'accounts' not in st.session_state: st.session_state['accounts'] = []
if 'campaigns' not in st.session_state: st.session_state['campaigns'] = []
if 'events' not in st.session_state: st.session_state['events'] = []
if 'activities' not in st.session_state: st.session_state['activities'] = []
if 'tasks' not in st.session_state: st.session_state['tasks'] = []
if 'competitors' not in st.session_state: st.session_state['competitors'] = []
if 'notes' not in st.session_state: st.session_state['notes'] = []
if 'notifications' not in st.session_state: st.session_state['notifications'] = []