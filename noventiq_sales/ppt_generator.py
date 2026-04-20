"""
PPT Presentation Generator - Enhanced with professional templates
"""

def generate_uuid():
    import uuid
    return str(uuid.uuid4())[:8]

def get_months():
    return ["January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]

PRODUCTS = {
    "AWS Cloud": {
        "description": "Amazon Web Services cloud infrastructure and services",
        "positioning": "Enterprise-grade cloud with most comprehensive services",
        "key_benefits": ["Scalability", "Pay-as-you-go", "Global presence", "500+ services"],
        "competitors": ["Azure", "Google Cloud"],
        "typical_deal_size": "₹50L - ₹5Cr",
        "sales_cycle": "3-9 months"
    },
    "Gen AI": {
        "description": "Generative AI solutions for enterprise automation",
        "positioning": "AI-powered transformation with custom LLM solutions",
        "key_benefits": ["Productivity boost", "Cost reduction", "24/7 automation"],
        "competitors": ["OpenAI Enterprise", "Google AI"],
        "typical_deal_size": "₹25L - ₹2Cr"
    },
    "Agentic AI": {
        "description": "Autonomous AI agents for business process automation",
        "positioning": "Next-gen autonomous agents",
        "key_benefits": ["Autonomous decision making", "End-to-end automation"],
        "typical_deal_size": "₹30L - ₹3Cr"
    },
    "DMAL": {
        "description": "Digital Marketing Analytics & Lead Management",
        "key_benefits": ["Lead scoring", "Campaign optimization"],
        "typical_deal_size": "₹10L - ₹1Cr"
    },
    "Citrix": {
        "description": "Virtualization and digital workspace",
        "key_benefits": ["Secure remote access", "VDI"],
        "typical_deal_size": "₹20L - ₹2Cr"
    },
    "Managed Services": {
        "description": "Full-stack IT management",
        "key_benefits": ["24/7 support", "Cost optimization"],
        "typical_deal_size": "₹30L - ₹10Cr"
    },
    "Security Solutions": {
        "description": "Enterprise cybersecurity",
        "key_benefits": ["Threat protection", "Compliance"],
        "typical_deal_size": "₹15L - ₹3Cr"
    },
    "Security Services": {
        "description": "Security consulting",
        "key_benefits": ["VAPT", "Compliance audits"],
        "typical_deal_size": "₹5L - ₹1Cr"
    }
}

MONTHLY_PLANS = {
    "January": {"theme": "New Year New Beginnings", "focus": ["Goal Setting", "Account Planning"], "budget": 300000, "kpis": ["Pipeline", "Meetings"]},
    "February": {"theme": "Valentine Special", "focus": ["Referral Generation"], "budget": 250000, "kpis": ["Referrals"]},
    "March": {"theme": "Q1 Close", "focus": ["Year-End Close"], "budget": 400000, "kpis": ["Revenue"]},
    "April": {"theme": "Summer Kickoff", "focus": ["Q2 Launch"], "budget": 300000, "kpis": ["Opportunities"]},
    "May": {"theme": "Tech Month", "focus": ["Technical Workshops"], "budget": 350000, "kpis": ["Demos"]},
    "June": {"theme": "Mid-Year Assessment", "focus": ["H1 Review"], "budget": 300000, "kpis": ["Achievement"]},
    "July": {"theme": "Monsoon Productivity", "focus": ["Monsoon Offers"], "budget": 280000, "kpis": ["Cloud"]},
    "August": {"theme": "Back to Business", "focus": ["Q3 Acceleration"], "budget": 300000, "kpis": ["Meetings"]},
    "September": {"theme": "Festive Season", "focus": ["Diwali Prep"], "budget": 400000, "kpis": ["Year-end"]},
    "October": {"theme": "Diwali Dhamaka", "focus": ["Maximum Sales"], "budget": 500000, "kpis": ["Revenue"]},
    "November": {"theme": "Year End Rush", "focus": ["Budget Utilization"], "budget": 450000, "kpis": ["Closures"]},
    "December": {"theme": "Year End Wrap", "focus": ["2024 Review"], "budget": 200000, "kpis": ["Achievement"]}
}

ANNUAL_BUDGET = {"total": 2500000, "breakdown": {"Digital Marketing": 1200000, "Events": 500000, "Travel": 400000, "Tools": 200000, "Materials": 100000, "Misc": 100000}}

# ============== PPT TEMPLATES ==============
PPT_TEMPLATES = {
    "title_slide": """
        <div style="text-align: center; padding: 80px 40px; background: linear-gradient(135deg, #0e1446 0%, #1a237e 50%, #283593 100%); color: white; height: 100%;">
            <h1 style="font-size: 48px; margin-bottom: 20px;">{title}</h1>
            <h2 style="font-size: 28px; opacity: 0.9; margin-bottom: 40px;">{subtitle}</h2>
            <div style="font-size: 18px; opacity: 0.8; margin-top: 60px;">
                <p>📅 {date}</p>
                <p>💼 Prepared by: Sales Team</p>
            </div>
        </div>
    """,
    
    "agenda_slide": """
        <div style="padding: 40px;">
            <h2 style="color: #1a237e; font-size: 32px; margin-bottom: 30px;">📋 Agenda</h2>
            <ul style="font-size: 20px; line-height: 2;">
                <li>🏢 Account Overview</li>
                <li>📊 Pipeline & Targets</li>
                <li>📢 Marketing Campaigns</li>
                <li>🎪 Events Plan</li>
                <li>💰 Budget Allocation</li>
                <li>📈 Next Steps</li>
            </ul>
        </div>
    """,
    
    "products_slide": """
        <div style="padding: 40px;">
            <h2 style="color: #1a237e; font-size: 32px; margin-bottom: 30px;">📦 Our Product Portfolio</h2>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
                {products_grid}
            </div>
        </div>
    """,
    
    "pipeline_slide": """
        <div style="padding: 40px;">
            <h2 style="color: #1a237e; font-size: 32px; margin-bottom: 30px;">💰 Pipeline Overview</h2>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; text-align: center;">
                <div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); padding: 30px; border-radius: 15px;">
                    <h3 style="font-size: 40px; color: #1976d2;">{total_accts}</h3>
                    <p>Accounts</p>
                </div>
                <div style="background: linear-gradient(135deg, #e8f5e9, #a5d6a7); padding: 30px; border-radius: 15px;">
                    <h3 style="font-size: 40px; color: #388e3c;">{pipeline_value}</h3>
                    <p>Pipeline Value</p>
                </div>
                <div style="background: linear-gradient(135deg, #fff3e0, #ffcc80); padding: 30px; border-radius: 15px;">
                    <h3 style="font-size: 40px; color: #f57c00;">{target_value}</h3>
                    <p>Annual Target</p>
                </div>
            </div>
        </div>
    """,
    
    "campaign_slide": """
        <div style="padding: 40px;">
            <h2 style="color: #1a237e; font-size: 32px; margin-bottom: 30px;">📢 Marketing Campaigns</h2>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: #1a237e; color: white;">
                    <th style="padding: 15px; text-align: left;">Campaign</th>
                    <th style="padding: 15px; text-align: left;">Product</th>
                    <th style="padding: 15px; text-align: left;">Platform</th>
                    <th style="padding: 15px; text-align: left;">Month</th>
                </tr>
                {campaign_rows}
            </table>
        </div>
    """,
    
    "budget_slide": """
        <div style="padding: 40px;">
            <h2 style="color: #1a237e; font-size: 32px; margin-bottom: 30px;">💰 Budget Allocation</h2>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
                {budget_items}
            </div>
            <div style="margin-top: 30px; text-align: center; padding: 20px; background: #1a237e; color: white; border-radius: 10px;">
                <h3>Total Budget: ₹{total_budget}</h3>
            </div>
        </div>
    """,
    
    "timeline_slide": """
        <div style="padding: 40px;">
            <h2 style="color: #1a237e; font-size: 32px; margin-bottom: 30px;">📅 Annual Timeline</h2>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
                <div>
                    <h3 style="color: #1976d2; background: #e3f2fd; padding: 15px; text-align: center; border-radius: 10px 10px 0 0;">Q1</h3>
                    <div style="background: #f5f5f5; padding: 15px; border-radius: 0 0 10px 10px;">
                        <p>Jan - Mar</p>
                        <p style="font-size: 14px;">{q1_theme}</p>
                    </div>
                </div>
                <div>
                    <h3 style="color: #388e3c; background: #e8f5e9; padding: 15px; text-align: center; border-radius: 10px 10px 0 0;">Q2</h3>
                    <div style="background: #f5f5f5; padding: 15px; border-radius: 0 0 10px 10px;">
                        <p>Apr - Jun</p>
                        <p style="font-size: 14px;">{q2_theme}</p>
                    </div>
                </div>
                <div>
                    <h3 style="color: #f57c00; background: #fff3e0; padding: 15px; text-align: center; border-radius: 10px 10px 0 0;">Q3</h3>
                    <div style="background: #f5f5f5; padding: 15px; border-radius: 0 0 10px 10px;">
                        <p>Jul - Sep</p>
                        <p style="font-size: 14px;">{q3_theme}</p>
                    </div>
                </div>
                <div>
                    <h3 style="color: #d32f2f; background: #ffebee; padding: 15px; text-align: center; border-radius: 10px 10px 0 0;">Q4</h3>
                    <div style="background: #f5f5f5; padding: 15px; border-radius: 0 0 10px 10px;">
                        <p>Oct - Dec</p>
                        <p style="font-size: 14px;">{q4_theme}</p>
                    </div>
                </div>
            </div>
        </div>
    """,
    
    "thankyou_slide": """
        <div style="text-align: center; padding: 80px 40px; background: linear-gradient(135deg, #1a237e, #283593); color: white;">
            <h1 style="font-size: 48px; margin-bottom: 20px;">🙏 Thank You!</h1>
            <h2 style="font-size: 28px; margin-bottom: 40px;">Let's Build Together</h2>
            <div style="font-size: 20px;">
                <p>📧 sales@noventiq.com</p>
                <p>📞 +91 98765 43210</p>
                <p>🌐 www.noventiq.com</p>
            </div>
        </div>
    """
}

def generate_ppt_slides(accounts, campaigns, events, targets, month=None, title="NoventIQ Sales Plan"):
    """Generate professional PPT slides"""
    
    import html
    from datetime import datetime
    
    slides = []
    
    # Slide 1: Title
    slides.append({
        "num": 1,
        "title": title,
        "template": "title",
        "content": PPT_TEMPLATES["title_slide"].format(
            title=title,
            subtitle="Comprehensive Sales Strategy FY 2024-25",
            date=datetime.now().strftime("%B %Y")
        )
    })
    
    # Slide 2: Agenda
    slides.append({
        "num": 2,
        "title": "Agenda",
        "template": "agenda",
        "content": PPT_TEMPLATES["agenda_slide"]
    })
    
    # Slide 3: Products
    products_html = ""
    for product, info in PRODUCTS.items():
        products_html += f"""
        <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h4 style="color: #1a237e; margin-bottom: 10px;">{product}</h4>
            <p style="font-size: 14px; color: #666;">{info['typical_deal_size']}</p>
            <p style="font-size: 14px;">{info['key_benefits'][0]}, {info['key_benefits'][1]}</p>
        </div>
        """
    
    slides.append({
        "num": 3,
        "title": "Products & Solutions",
        "template": "products",
        "content": PPT_TEMPLATES["products_slide"].format(products_grid=products_html)
    })
    
    # Slide 4: Pipeline
    total_pipeline = sum([a.get('potential', 0) for a in accounts])
    total_target = sum([t.get('target_amount', 0) for t in targets])
    
    slides.append({
        "num": 4,
        "title": "Pipeline Overview",
        "template": "pipeline",
        "content": PPT_TEMPLATES["pipeline_slide"].format(
            total_accts=str(len(accounts)),
            pipeline_value=f"₹{total_pipeline/10000000:.1f}Cr",
            target_value=f"₹{total_target/10000000:.1f}Cr"
        )
    })
    
    # Slide 5: Campaigns
    campaign_rows = ""
    for i, camp in enumerate(campaigns[:8] if campaigns else []):
        bg = "#f5f5f5" if i % 2 == 0 else "white"
        campaign_rows += f"""
        <tr style="background: {bg};">
            <td style="padding: 12px;">{camp.get('name', 'N/A')}</td>
            <td style="padding: 12px;">{camp.get('product', 'N/A')}</td>
            <td style="padding: 12px;">{camp.get('platform', 'N/A')}</td>
            <td style="padding: 12px;">{camp.get('month', 'N/A')}</td>
        </tr>
        """
    
    if not campaign_rows:
        campaign_rows = "<tr><td colspan='4' style='padding: 20px; text-align: center;'>No campaigns added yet</td></tr>"
    
    slides.append({
        "num": 5,
        "title": "Marketing Campaigns",
        "template": "campaign",
        "content": PPT_TEMPLATES["campaign_slide"].format(campaign_rows=campaign_rows)
    })
    
    # Slide 6: Budget
    budget_items = ""
    for category, amount in ANNUAL_BUDGET['breakdown'].items():
        budget_items += f"""
        <div style="background: white; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h4 style="color: #1a237e; margin-bottom: 5px;">{category}</h4>
            <p style="font-size: 24px; color: #388e3c;">₹{amount/100000:.0f}L</p>
            <p style="font-size: 12px; color: #666;">{amount/ANNUAL_BUDGET['total']*100:.0f}%</p>
        </div>
        """
    
    slides.append({
        "num": 6,
        "title": "Budget Allocation",
        "template": "budget",
        "content": PPT_TEMPLATES["budget_slide"].format(
            budget_items=budget_items,
            total_budget=f"₹{ANNUAL_BUDGET['total']/100000:.0f}L"
        )
    })
    
    # Slide 7: Timeline
    slides.append({
        "num": 7,
        "title": "Annual Timeline",
        "template": "timeline",
        "content": PPT_TEMPLATES["timeline_slide"].format(
            q1_theme="Q1 Close & New Year",
            q2_theme="Summer & Tech",
            q3_theme="Festive Prep",
            q4_theme="Diwali & Year End"
        )
    })
    
    # Slide 8: Thank You
    slides.append({
        "num": 8,
        "title": "Thank You",
        "template": "thankyou",
        "content": PPT_TEMPLATES["thankyou_slide"]
    })
    
    return slides


def generate_html_presentation(slides, title="NoventIQ Sales Presentation"):
    """Generate complete HTML presentation"""
    
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{ 
            font-family: 'Segoe UI', Arial, sans-serif; 
            background: #f5f5f5;
        }}
        
        .slide {{
            width: 100%;
            max-width: 1200px;
            min-height: 675px;
            margin: 20px auto;
            background: white;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            border-radius: 15px;
            overflow: hidden;
        }}
        
        .slide-content {{
            width: 100%;
            height: 100%;
        }}
        
        .navigation {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
            background: white;
            padding: 15px 25px;
            border-radius: 30px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }}
        
        .nav-btn {{
            padding: 10px 20px;
            background: #1a237e;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
        }}
        
        .nav-btn:hover {{
            background: #3949ab;
        }}
        
        .slide-num {{
            position: fixed;
            bottom: 20px;
            right: 30px;
            background: #1a237e;
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 14px;
        }}
        
        .progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            height: 5px;
            background: linear-gradient(90deg, #1a237e, #4caf50);
            transition: width 0.3s;
        }}
        
        @media print {{
            .slide {{
                margin: 0;
                box-shadow: none;
            }}
            .navigation, .slide-num, .progress-bar {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="progress-bar" id="progress" style="width: 12.5%;"></div>
    
    {''.join([f'''
    <div class="slide" id="slide-{slide['num']}" style="display: {'block' if slide['num'] == 1 else 'none'};">
        <div class="slide-content">
            {slide['content']}
        </div>
    </div>
    ''' for slide in slides])}
    
    <div class="navigation">
        <button class="nav-btn" onclick="changeSlide(-1)">◀ Previous</button>
        <button class="nav-btn" onclick="goToSlide(1)">🏠 Home</button>
        <button class="nav-btn" onclick="changeSlide(1)">Next ▶</button>
    </div>
    
    <div class="slide-num">
        Slide <span id="current-slide">1</span> of {len(slides)}
    </div>
    
    <script>
        let currentSlide = 1;
        const totalSlides = {len(slides)};
        
        function showSlide(n) {{
            if (n < 1) n = 1;
            if (n > totalSlides) n = totalSlides;
            
            for (let i = 1; i <= totalSlides; i++) {{
                document.getElementById('slide-' + i).style.display = (i === n) ? 'block' : 'none';
            }}
            
            currentSlide = n;
            document.getElementById('current-slide').textContent = n;
            document.getElementById('progress').style.width = (n / totalSlides * 100) + '%';
        }}
        
        function changeSlide(direction) {{
            showSlide(currentSlide + direction);
        }}
        
        function goToSlide(n) {{
            showSlide(n);
        }}
        
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'ArrowRight' || e.key === ' ') {{
                changeSlide(1);
            }} else if (e.key === 'ArrowLeft') {{
                changeSlide(-1);
            }}
        }});
    </script>
</body>
</html>
    """
    
    return html_content