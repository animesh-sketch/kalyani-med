"""
NoventIQ Sales Manager - Comprehensive Sales Planning Tool
Enhanced with detailed plans, budgets, resources, and PPT Export
"""

import streamlit as st
import json
from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict
import uuid

# ============== ALL DATA AND FUNCTIONS ==============
# (Including all previous content - products, plans, budgets, learning, KPIs, etc.)

PRODUCTS = {
    "AWS Cloud": {
        "description": "Amazon Web Services cloud infrastructure and services",
        "positioning": "Enterprise-grade cloud with most comprehensive services",
        "key_benefits": ["Scalability", "Pay-as-you-go", "Global presence", "500+ services"],
        "competitors": ["Azure", "Google Cloud"],
        "typical_deal_size": "₹50L - ₹5Cr",
        "sales_cycle": "3-9 months",
        "decision_makers": ["CTO", "IT Head", "CFO", "CEO"],
        "pain_points": ["Cost management", "Migration complexity", "Security", "Skill gap"]
    },
    "Gen AI": {
        "description": "Generative AI solutions for enterprise automation",
        "positioning": "AI-powered transformation with custom LLM solutions",
        "key_benefits": ["Productivity boost", "Cost reduction", "24/7 automation", "Custom models"],
        "competitors": ["OpenAI Enterprise", "Google AI", "Microsoft Copilot"],
        "typical_deal_size": "₹25L - ₹2Cr",
        "sales_cycle": "2-6 months",
        "decision_makers": ["CEO", "CDO", "CTO", "Business Heads"]
    },
    "Agentic AI": {
        "description": "Autonomous AI agents for business process automation",
        "positioning": "Next-gen autonomous agents for enterprise workflows",
        "key_benefits": ["Autonomous decision making", "End-to-end automation", "Self-learning"],
        "competitors": ["Salesforce AgentForce", "Microsoft AI Agent", "ServiceNow"],
        "typical_deal_size": "₹30L - ₹3Cr",
        "sales_cycle": "3-8 months"
    },
    "DMAL": {
        "description": "Digital Marketing Analytics & Lead Management",
        "positioning": "Data-driven marketing automation and analytics platform",
        "key_benefits": ["Lead scoring", "Campaign optimization", "ROI tracking"],
        "competitors": ["HubSpot", "Marketo", "Salesforce Marketing Cloud"],
        "typical_deal_size": "₹10L - ₹1Cr"
    },
    "Citrix": {
        "description": "Virtualization and digital workspace solutions",
        "positioning": "Secure remote work and workspace transformation",
        "key_benefits": ["Secure remote access", "VDI", "App virtualization"],
        "competitors": ["VMware Horizon", "Microsoft WVD"],
        "typical_deal_size": "₹20L - ₹2Cr"
    },
    "Managed Services": {
        "description": "Full-stack IT infrastructure and application management",
        "positioning": "24/7 managed services for seamless operations",
        "key_benefits": ["24/7 support", "Cost optimization", "Proactive monitoring"],
        "competitors": ["Accenture", "Infosys", "TCS"],
        "typical_deal_size": "₹30L - ₹10Cr",
        "sales_cycle": "4-12 months"
    },
    "Security Solutions": {
        "description": "Enterprise cybersecurity and compliance solutions",
        "positioning": "End-to-end security from endpoint to cloud",
        "key_benefits": ["Threat protection", "Compliance", "SOC services", "Zero trust"],
        "competitors": ["Palo Alto", "Fortinet", "CrowdStrike"],
        "typical_deal_size": "₹15L - ₹3Cr"
    },
    "Security Services": {
        "description": "Professional security consulting and implementation",
        "positioning": "Security advisory and implementation experts",
        "key_benefits": ["VAPT", "Compliance audits", "Incident response"],
        "competitors": ["KPMG", "Deloitte", "Quick Heal"],
        "typical_deal_size": "₹5L - ₹1Cr"
    }
}

MONTHLY_PLANS = {
    "January": {
        "theme": "New Year New Beginnings",
        "focus": ["Goal Setting", "Account Planning", "Q1 Pipeline Building"],
        "activities": {"Week 1": ["Review past year", "Set Q1 targets"], "Week 2": ["Key account outreach"], "Week 3": ["New product presentations"], "Week 4": ["Pipeline review"]},
        "budget": 300000, "kpis": ["Pipeline created", "Meetings booked"]
    },
    "February": {
        "theme": "Valentine Special - Relationship Building",
        "focus": ["Customer Appreciation", "Referral Generation"],
        "activities": {"Week 1": ["Customer thank you calls"], "Week 2": ["Referral program"], "Week 3": ["Webinar"], "Week 4": ["Mid-month review"]},
        "budget": 250000, "kpis": ["Referrals", "Renewal rate"]
    },
    "March": {
        "theme": "Q1 Close - End of Financial Year",
        "focus": ["Q1 Close", "Budget Utilization"],
        "activities": {"Week 1": ["Push for closures"], "Week 2": ["Last chance proposals"], "Week 3": ["Q1 review"], "Week 4": ["Q2 planning"]},
        "budget": 400000, "kpis": ["Q1 Revenue", "Close rate"]
    },
    "April": {"theme": "Summer Kickoff", "focus": ["Q2 Launch"], "budget": 300000, "kpis": ["New opportunities"]},
    "May": {"theme": "Tech Month", "focus": ["Technical Workshops"], "budget": 350000, "kpis": ["Technical meetings"]},
    "June": {"theme": "Mid-Year Assessment", "focus": ["H1 Review", "H2 Planning"], "budget": 300000, "kpis": ["H1 achievement"]},
    "July": {"theme": "Monsoon Productivity", "focus": ["Monsoon Offers"], "budget": 280000, "kpis": ["Cloud migrations"]},
    "August": {"theme": "Back to Business", "focus": ["Q3 Acceleration"], "budget": 300000, "kpis": ["Executive meetings"]},
    "September": {"theme": "Festive Season Kickoff", "focus": ["Diwali Preparation"], "budget": 400000, "kpis": ["Year-end commits"]},
    "October": {"theme": "Diwali Dhamaka", "focus": ["Diwali Sales"], "budget": 500000, "kpis": ["Diwali revenue"]},
    "November": {"theme": "Year End Rush", "focus": ["Budget Utilization"], "budget": 450000, "kpis": ["Year-end revenue"]},
    "December": {"theme": "Year End Wrap", "focus": ["2024 Review", "2025 Planning"], "budget": 200000, "kpis": ["Annual revenue"]}
}

ANNUAL_BUDGET = {
    "total": 2500000,
    "breakdown": {
        "Digital Marketing": 1200000,
        "Events & Conferences": 500000,
        "Travel & Accommodation": 400000,
        "Sales Tools & Software": 200000,
        "Collateral & Materials": 100000,
        "Miscellaneous": 100000
    }
}

EMAIL_TEMPLATES = {
    "initial_outreach": "Hi {name},\n\nI came across {company} and wanted to reach out about {topic}.\n\nBest regards,\n{your_name}",
    "follow_up": "Following up on our conversation - attached {document}",
    "proposal": "Proposal for {company} - {project_name}"
}

SOCIAL_CONTENT = {
    "linkedin": {
        "post_types": ["Case Study", "Tips", "Industry News", "Thought Leadership"],
        "best_times": ["Tuesday 9am", "Wednesday 10am", "Thursday 9am"],
        "hashtags": ["#DigitalTransformation", "#CloudComputing", "#AI", "#NoventIQ"]
    }
}

LEARNING = {
    "first_week": [
        {"task": "Learn about all products", "resource": "Product training deck"},
        {"task": "Understand pricing and packages", "resource": "Price list"},
        {"task": "Set up all tools", "resource": "IT support"}
    ],
    "first_month": [
        {"task": "Shadow 5 senior sales calls", "resource": "Recording library"},
        {"task": "Complete product certifications", "resource": "Internal training"},
        {"task": "Meet 10 existing customers", "resource": "Customer list"}
    ],
    "first_quarter": [
        {"task": "Close first deal", "goal": "Revenue target: ₹10L"},
        {"task": "Build pipeline of ₹50L", "goal": "Pipeline target"}
    ]
}

KPIS = {
    "pipeline": {"formula": "Open Deals × Probability", "target": "3-4x of revenue target"},
    "conversion_rate": {"formula": "Closed Won / Total Opportunities", "target": "20-30%"},
    "avg_deal_size": {"formula": "Total Revenue / Number of Deals", "target": "₹15-20L"},
    "sales_cycle": {"formula": "Average days from lead to close", "target": "90-120 days"},
    "call_connect_rate": {"formula": "Connected Calls / Total Calls", "target": "15-20%"},
    "meeting_rate": {"formula": "Meetings Booked / Leads Contacted", "target": "10-15%"},
    "proposal_to_close": {"formula": "Closed Won / Proposals Sent", "target": "30-40%"}
}

LEARNING = {
    "first_week": [
        {"task": "Learn about all products", "resource": "Product training deck"},
        {"task": "Understand pricing and packages", "resource": "Price list"},
        {"task": "Set up all tools", "resource": "IT support"}
    ],
    "first_month": [
        {"task": "Shadow 5 senior sales calls", "resource": "Recording library"},
        {"task": "Complete product certifications", "resource": "Internal training"},
        {"task": "Meet 10 existing customers", "resource": "Customer list"}
    ],
    "first_quarter": [
        {"task": "Close first deal", "goal": "Revenue target: ₹10L"},
        {"task": "Build pipeline of ₹50L", "goal": "Pipeline target"}
    ]
}

def generate_uuid():
    return str(uuid.uuid4())[:8]

def get_months():
    return list(MONTHLY_PLANS.keys())

# NOTE: Session state should be initialized in app.py, not here
# This file contains only data and functions


# ============== PPTX GENERATOR ==============
def generate_pptx_content(accounts, campaigns, events, targets, month_plan=None):
    """Generate PPT content for presentation"""
    
    slides = []
    
    # Slide 1: Title
    slides.append({
        "title": "NoventIQ Sales Plan",
        "subtitle": "Comprehensive Sales Strategy & Execution Plan",
        "content": f"Prepared by: Sales Team\nDate: {datetime.now().strftime('%B %d, %Y')}",
        "layout": "title"
    })
    
    # Slide 2: Executive Summary
    total_pipeline = sum([a.get('potential', 0) for a in accounts])
    total_targets = sum([t.get('target_amount', 0) for t in targets])
    
    slides.append({
        "title": "Executive Summary",
        "content": f"""
• Total Accounts: {len(accounts)}
• Total Pipeline Value: ₹{total_pipeline/10000000:.1f} Cr
• Annual Target: ₹{total_targets/10000000:.1f} Cr
• Active Campaigns: {len(campaigns)}
• Planned Events: {len(events)}
• Budget for FY: ₹{ANNUAL_BUDGET['total']/100000:.0f} Lakh
        """,
        "layout": "bullet"
    })
    
    # Slide 3: Products Overview
    products_content = ""
    for product, info in PRODUCTS.items():
        products_content += f"• {product}: {info['typical_deal_size']}\n"
    
    slides.append({
        "title": "Our Product Portfolio",
        "content": products_content,
        "layout": "bullet"
    })
    
    # Slide 4: Monthly Plan
    if month_plan:
        plan = MONTHLY_PLANS.get(month_plan, {})
        slides.append({
            "title": f"📅 {month_plan} Plan - {plan.get('theme', '')}",
            "content": f"""
Focus Areas: {', '.join(plan.get('focus', []))}

Budget: ₹{plan.get('budget', 0)/100000:.0f} Lakh

KPIs: {', '.join(plan.get('kpis', []))}
            """,
            "layout": "bullet"
        })
    
    # Slide 5: Budget Breakdown
    budget_content = ""
    for category, amount in ANNUAL_BUDGET['breakdown'].items():
        budget_content += f"• {category}: ₹{amount/100000:.0f} Lakh ({amount/ANNUAL_BUDGET['total']*100:.0f}%)\n"
    
    slides.append({
        "title": "Annual Budget Breakdown",
        "content": budget_content,
        "layout": "bullet"
    })
    
    # Slide 6: Account Pipeline
    if accounts:
        account_content = ""
        for acc in accounts[:10]:
            account_content += f"• {acc.get('name', 'N/A')}: ₹{acc.get('potential', 0)/100000:.0f}L ({acc.get('probability', 0)}%)\n"
        
        slides.append({
            "title": "Top Accounts & Pipeline",
            "content": account_content,
            "layout": "bullet"
        })
    
    # Slide 7: Campaigns
    if campaigns:
        campaign_content = ""
        for camp in campaigns[:8]:
            campaign_content += f"• {camp.get('name', 'N/A')} ({camp.get('platform', '')}) - {camp.get('month', '')}\n"
        
        slides.append({
            "title": "Marketing Campaigns",
            "content": campaign_content,
            "layout": "bullet"
        })
    
    # Slide 8: Events
    if events:
        event_content = ""
        for evt in events:
            event_content += f"• {evt.get('name', 'N/A')} - {evt.get('month', '')}\n"
        
        slides.append({
            "title": "Customer Events",
            "content": event_content,
            "layout": "bullet"
        })
    
    # Slide 9: KPIs & Targets
    kpi_content = """
• Pipeline Coverage: Target 3-4x revenue
• Conversion Rate: Target 20-30%
• Average Deal Size: ₹15-20 Lakh
• Sales Cycle: 90-120 days
• Meeting Rate: Target 10-15%
    """
    
    slides.append({
        "title": "KPIs & Targets",
        "content": kpi_content,
        "layout": "bullet"
    })
    
    # Slide 10: Next Steps
    slides.append({
        "title": "Next Steps & Action Items",
        "content": """
1. Finalize monthly campaign calendar
2. Confirm event dates and venues
3. Brief the sales team
4. Set up CRM dashboards
5. Schedule weekly review meetings
        """,
        "layout": "bullet"
    })
    
    return slides
