import streamlit as st
from datetime import datetime

st.set_page_config(page_title="ShaadiZone - Love Blooms Here", page_icon="💖", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Poppins:wght@300;400;500;600&display=swap');

    * { margin: 0; padding: 0; box-sizing: border-box; }

    .stApp {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(160deg, #fff0f3 0%, #fde8ee 40%, #fff5f7 100%);
        min-height: 100vh;
    }

    h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

    /* ─── TOP NAVBAR ─── */
    .navbar {
        position: sticky;
        top: 0;
        z-index: 999;
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(233, 30, 99, 0.12);
        padding: 0 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 64px;
        box-shadow: 0 2px 20px rgba(233, 30, 99, 0.08);
    }

    .navbar-brand {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #c2185b;
        letter-spacing: -0.3px;
    }

    .navbar-links {
        display: flex;
        gap: 8px;
    }

    .nav-link {
        padding: 8px 20px;
        border-radius: 24px;
        font-size: 0.9rem;
        font-weight: 500;
        cursor: pointer;
        border: 1.5px solid transparent;
        text-decoration: none;
        transition: all 0.25s ease;
        color: #555;
    }

    .nav-link:hover {
        background: rgba(233, 30, 99, 0.06);
        color: #e91e63;
        border-color: rgba(233, 30, 99, 0.15);
    }

    .nav-link.active {
        background: linear-gradient(135deg, #e91e63, #c2185b);
        color: white !important;
        border-color: transparent;
        box-shadow: 0 4px 14px rgba(233, 30, 99, 0.3);
    }

    /* ─── HERO ─── */
    .hero {
        background: linear-gradient(135deg, #e91e63 0%, #c2185b 30%, #ad1457 70%, #e91e63 100%);
        background-size: 400% 400%;
        animation: gradientBG 14s ease infinite;
        padding: 100px 40px 80px;
        text-align: center;
        color: white;
        margin-bottom: 0;
        position: relative;
        overflow: hidden;
    }

    @keyframes gradientBG {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .hero::before {
        content: '';
        position: absolute;
        inset: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        opacity: 0.4;
    }

    .flower {
        position: absolute;
        font-size: 2rem;
        opacity: 0.14;
        animation: floatFlower 12s ease-in-out infinite;
    }

    .flower:nth-child(1) { top: 8%;  left: 3%;  }
    .flower:nth-child(2) { top: 15%; right: 8%;  font-size: 1.5rem; animation-delay: 2s; }
    .flower:nth-child(3) { bottom: 18%; left: 10%; animation-delay: 4s; }
    .flower:nth-child(4) { bottom: 8%;  right: 15%; font-size: 1.8rem; animation-delay: 6s; }
    .flower:nth-child(5) { top: 40%;  left: 2%;  animation-delay: 8s; }

    @keyframes floatFlower {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50%       { transform: translateY(-18px) rotate(10deg); }
    }

    .hero h1 {
        font-size: 4.8rem;
        margin-bottom: 14px;
        font-weight: 700;
        text-shadow: 0 4px 16px rgba(0,0,0,0.18);
        position: relative;
        z-index: 2;
        letter-spacing: -1px;
    }

    .hero-subtitle { font-size: 1.4rem; margin-bottom: 10px; position: relative; z-index: 2; opacity: 0.95; }
    .hero-tagline  { font-size: 1.05rem; opacity: 0.85; position: relative; z-index: 2; }

    .stats-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 36px;
        position: relative;
        z-index: 2;
        flex-wrap: wrap;
    }

    .stat-box {
        background: rgba(255,255,255,0.18);
        backdrop-filter: blur(10px);
        padding: 20px 36px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.28);
        min-width: 150px;
        transition: transform 0.3s ease;
    }

    .stat-box:hover { transform: translateY(-4px); }

    .stat-number { font-size: 2.1rem; font-weight: 700; letter-spacing: -0.5px; }
    .stat-label  { font-size: 0.82rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.88; margin-top: 2px; }

    /* ─── WAVE DIVIDER ─── */
    .wave-divider {
        background: linear-gradient(135deg, #e91e63, #c2185b);
        position: relative;
        height: 60px;
        overflow: hidden;
        margin-bottom: 0;
    }
    .wave-divider::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 60px;
        background: linear-gradient(160deg, #fff0f3 0%, #fde8ee 40%, #fff5f7 100%);
        clip-path: ellipse(55% 100% at 50% 100%);
    }

    /* ─── SECTION CONTAINERS ─── */
    .section-pad { padding: 60px 0 20px; }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        text-align: center;
        margin-bottom: 8px;
        color: #c2185b;
        letter-spacing: -0.5px;
    }

    .section-subtitle {
        text-align: center;
        color: #999;
        font-size: 1rem;
        margin-bottom: 44px;
    }

    .section-title::after {
        content: '💖';
        display: block;
        font-size: 1.2rem;
        margin-top: 6px;
    }

    /* ─── MISSION BOX ─── */
    .mission-box {
        background: white;
        padding: 52px 60px;
        border-radius: 28px;
        border: 1.5px solid rgba(233, 30, 99, 0.12);
        margin: 48px auto;
        max-width: 860px;
        text-align: center;
        box-shadow: 0 16px 48px rgba(233, 30, 99, 0.08);
        position: relative;
        overflow: hidden;
    }

    .mission-box::before {
        content: '💖';
        position: absolute;
        font-size: 8rem;
        opacity: 0.03;
        top: -10px;
        right: 20px;
    }

    /* ─── FEATURE CARDS ─── */
    .elegant-card {
        background: white;
        padding: 36px 24px;
        border-radius: 24px;
        box-shadow: 0 8px 28px rgba(233, 30, 99, 0.08);
        text-align: center;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1.5px solid rgba(233, 30, 99, 0.08);
        height: 100%;
    }

    .elegant-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 50px rgba(233, 30, 99, 0.18);
        border-color: #e91e63;
    }

    .card-icon {
        font-size: 3rem;
        margin-bottom: 16px;
        display: block;
    }

    /* ─── PROFILE CARDS ─── */
    .profile-card {
        background: white;
        border-radius: 24px;
        overflow: hidden;
        box-shadow: 0 8px 28px rgba(233, 30, 99, 0.09);
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1.5px solid rgba(233, 30, 99, 0.07);
        margin-bottom: 8px;
    }

    .profile-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 50px rgba(233, 30, 99, 0.18);
        border-color: rgba(233, 30, 99, 0.3);
    }

    .profile-image-area {
        background: linear-gradient(135deg, #e91e63 0%, #c2185b 60%, #ad1457 100%);
        padding: 36px;
        text-align: center;
        position: relative;
    }

    .profile-image-area .avatar {
        font-size: 4.5rem;
        display: block;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
    }

    .verified-pill {
        position: absolute;
        top: 12px;
        right: 12px;
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(8px);
        color: white;
        font-size: 0.68rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        letter-spacing: 0.5px;
    }

    .profile-body { padding: 20px 22px 16px; }
    .profile-name  { color: #c2185b; font-family: 'Playfair Display', serif; font-size: 1.35rem; margin-bottom: 3px; font-weight: 600; }
    .profile-meta  { color: #777; font-size: 0.9rem; margin-bottom: 4px; }
    .profile-job   { color: #555; font-size: 0.85rem; margin-bottom: 12px; }

    .disability-badge {
        background: linear-gradient(135deg, #fff0f3, #ffe4e9);
        border: 1.5px solid #f8bbd0;
        color: #c2185b;
        padding: 5px 12px;
        border-radius: 16px;
        font-weight: 500;
        font-size: 0.78rem;
        display: inline-block;
    }

    /* ─── DETAIL PAGE ─── */
    .detail-header {
        background: linear-gradient(135deg, #e91e63, #c2185b);
        padding: 48px 52px;
        border-radius: 24px;
        margin-bottom: 24px;
        box-shadow: 0 16px 48px rgba(233, 30, 99, 0.25);
    }

    .detail-card {
        background: white;
        padding: 32px;
        border-radius: 22px;
        box-shadow: 0 8px 28px rgba(233, 30, 99, 0.08);
        border: 1.5px solid rgba(233, 30, 99, 0.07);
        height: 100%;
    }

    .preference-item {
        background: linear-gradient(135deg, #fff0f3, #ffe4e9);
        padding: 20px 16px;
        border-radius: 18px;
        text-align: center;
        border: 1.5px solid #f8bbd0;
    }

    /* ─── TESTIMONIAL ─── */
    .testimonial-card {
        background: white;
        padding: 32px 28px;
        border-radius: 24px;
        box-shadow: 0 8px 28px rgba(233, 30, 99, 0.08);
        border: 1.5px solid rgba(233, 30, 99, 0.07);
        position: relative;
    }

    .testimonial-card::before {
        content: '"';
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        color: #f8bbd0;
        position: absolute;
        top: -10px;
        left: 18px;
        line-height: 1;
    }

    .testimonial-text { color: #666; font-style: italic; line-height: 1.7; font-size: 0.97rem; margin-top: 20px; }
    .testimonial-author { color: #e91e63; font-weight: 600; margin-top: 16px; font-size: 0.92rem; }

    /* ─── FORM ─── */
    .form-container {
        background: white;
        padding: 44px 48px;
        border-radius: 28px;
        box-shadow: 0 16px 48px rgba(233, 30, 99, 0.10);
        border: 1.5px solid rgba(233, 30, 99, 0.08);
        max-width: 800px;
        margin: 0 auto;
    }

    .info-box {
        background: linear-gradient(135deg, #fff0f3, #ffe4e9);
        padding: 16px 20px;
        border-radius: 14px;
        border-left: 4px solid #e91e63;
    }

    /* ─── BUTTONS ─── */
    .stButton > button {
        border-radius: 24px !important;
        font-weight: 600 !important;
        transition: all 0.25s ease !important;
        letter-spacing: 0.2px;
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #e91e63, #c2185b) !important;
        border: none !important;
        box-shadow: 0 6px 18px rgba(233, 30, 99, 0.28) !important;
    }

    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 28px rgba(233, 30, 99, 0.38) !important;
    }

    .stButton > button:not([kind="primary"]) {
        border: 1.5px solid rgba(233, 30, 99, 0.25) !important;
        color: #c2185b !important;
        background: white !important;
    }

    .stButton > button:not([kind="primary"]):hover {
        background: #fff0f3 !important;
        border-color: #e91e63 !important;
    }

    /* ─── FOOTER ─── */
    .footer {
        background: linear-gradient(135deg, #c2185b, #e91e63);
        color: white;
        padding: 52px 0 28px;
        margin-top: 80px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .footer::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 52px;
        background: linear-gradient(160deg, #fff0f3 0%, #fde8ee 40%, #fff5f7 100%);
        clip-path: ellipse(55% 100% at 50% 0%);
    }

    .footer-inner { position: relative; z-index: 1; }
    .footer-title { font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 6px; }

    /* ─── DECORATIVE DIVIDER ─── */
    .flower-divider { text-align: center; font-size: 1.3rem; margin: 40px 0; color: #e91e63; letter-spacing: 10px; opacity: 0.7; }

    /* ─── FILTER BAR ─── */
    .filter-bar {
        background: white;
        border-radius: 20px;
        padding: 20px 24px;
        box-shadow: 0 4px 20px rgba(233, 30, 99, 0.07);
        border: 1.5px solid rgba(233, 30, 99, 0.07);
        margin-bottom: 32px;
    }

    /* ─── RESULT COUNT BADGE ─── */
    .result-count {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: linear-gradient(135deg, #fff0f3, #ffe4e9);
        border: 1.5px solid #f8bbd0;
        color: #c2185b;
        padding: 6px 18px;
        border-radius: 20px;
        font-size: 0.88rem;
        font-weight: 500;
    }

    /* ─── MATCH CARDS ─── */
    .match-card {
        background: white;
        border-radius: 24px;
        padding: 24px 28px;
        box-shadow: 0 8px 28px rgba(233, 30, 99, 0.09);
        border: 1.5px solid rgba(233, 30, 99, 0.08);
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 16px;
        display: flex;
        gap: 24px;
        align-items: flex-start;
    }

    .match-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 44px rgba(233, 30, 99, 0.16);
        border-color: rgba(233, 30, 99, 0.25);
    }

    .match-rank {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #f8bbd0;
        min-width: 36px;
        line-height: 1;
        margin-top: 4px;
    }

    .match-avatar {
        font-size: 3.2rem;
        background: linear-gradient(135deg, #e91e63, #c2185b);
        border-radius: 18px;
        width: 70px;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .match-info { flex: 1; min-width: 0; }
    .match-name { color: #c2185b; font-family: 'Playfair Display', serif; font-size: 1.25rem; font-weight: 600; margin-bottom: 3px; }
    .match-meta { color: #888; font-size: 0.87rem; margin-bottom: 8px; }

    .match-score-block { text-align: center; flex-shrink: 0; min-width: 110px; }

    .score-ring {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1.35rem;
        font-weight: 700;
        color: white;
        margin-bottom: 6px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    }

    .score-label { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; }

    .factor-row {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 5px;
        font-size: 0.78rem;
    }

    .factor-bar-wrap {
        flex: 1;
        background: #f5f5f5;
        border-radius: 6px;
        height: 6px;
        overflow: hidden;
    }

    .factor-bar {
        height: 100%;
        border-radius: 6px;
        transition: width 0.6s ease;
    }

    .factor-name { color: #999; min-width: 80px; }
    .factor-pct  { color: #bbb; min-width: 34px; text-align: right; }

    .match-tag {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 600;
        margin-top: 8px;
    }

    .tag-strong  { background: #e8f5e9; color: #2e7d32; }
    .tag-good    { background: #fff8e1; color: #f57f17; }
    .tag-possible{ background: #fce4ec; color: #c2185b; }

    .prefs-panel {
        background: white;
        border-radius: 22px;
        padding: 28px 32px;
        box-shadow: 0 8px 28px rgba(233, 30, 99, 0.07);
        border: 1.5px solid rgba(233, 30, 99, 0.08);
        margin-bottom: 36px;
    }

    /* Hide Streamlit chrome */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stDeployButton { display: none; }
    .block-container { padding-top: 0 !important; padding-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── DATA ───────────────────────────────────────────────────────────────────
if 'profiles' not in st.session_state:
    st.session_state.profiles = [
        {"id": 1, "name": "Ananya Sharma",  "age": 26, "profession": "Software Engineer", "location": "Mumbai",    "education": "B.Tech",    "religion": "Hindu", "image": "👩‍💻", "verified": True,  "about": "I use a wheelchair but that doesn't stop me from dreaming big!",          "disability": "Wheelchair User",  "disability_type": "Physical", "income": "8-10 LPA"},
        {"id": 2, "name": "Raj Verma",       "age": 28, "profession": "Doctor",            "location": "Delhi",     "education": "MBBS",      "religion": "Hindu", "image": "👨‍⚕️", "verified": True,  "about": "Born blind but I see the world with my heart.",                           "disability": "Visually Impaired","disability_type": "Visual",    "income": "15-20 LPA"},
        {"id": 3, "name": "Diya Patel",      "age": 24, "profession": "Teacher",           "location": "Ahmedabad", "education": "M.A. B.Ed", "religion": "Hindu", "image": "👩‍🏫", "verified": True,  "about": "I can't hear but I can feel love!",                                       "disability": "Deaf & Mute",      "disability_type": "Hearing",   "income": "5-6 LPA"},
        {"id": 4, "name": "Aditya Singh",    "age": 30, "profession": "Business Owner",    "location": "Jaipur",    "education": "MBA",       "religion": "Hindu", "image": "👨‍💼", "verified": True,  "about": "Lost my leg but gained perspective!",                                     "disability": "Amputee",          "disability_type": "Physical",  "income": "25-30 LPA"},
        {"id": 5, "name": "Myra Nair",       "age": 27, "profession": "Fashion Designer",  "location": "Bangalore", "education": "B.Des",     "religion": "Hindu", "image": "👩‍🎨", "verified": True,  "about": "Creating beautiful designs and seeking love!",                            "disability": "Hearing Impaired", "disability_type": "Hearing",   "income": "6-8 LPA"},
        {"id": 6, "name": "Karan Menon",     "age": 29, "profession": "Engineer",          "location": "Kochi",     "education": "B.Tech",    "religion": "Hindu", "image": "👨‍💻", "verified": True,  "about": "Born with cerebral palsy but I'm an engineer!",                          "disability": "Cerebral Palsy",   "disability_type": "Physical",  "income": "12-15 LPA"},
    ]

if 'page' not in st.session_state:
    st.session_state.page = "home"

if 'selected_profile' not in st.session_state:
    st.session_state.selected_profile = None

profile_images  = ["👩‍💻", "👨‍💻", "👩‍⚕️", "👨‍⚕️", "👩‍🏫", "👨‍🏫", "👩‍🎨", "👨‍🎨", "👩‍💼", "👨‍💼", "💖", "💕", "🌸", "🌷", "🦋", "💗"]
locations       = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Jaipur', 'Ahmedabad', 'Kochi', 'Kolkata', 'Lucknow', 'Chandigarh']
religions       = ['Hindu', 'Muslim', 'Christian', 'Sikh', 'Buddhist', 'Jain', 'Other']
professions     = ['Software Engineer', 'Doctor', 'Business Owner', 'Fashion Designer', 'Engineer', 'Architect', 'Lawyer', 'Banker', 'Artist', 'Writer', 'Other']
disability_types= ['Physical Disability (Wheelchair)', 'Physical Disability (Amputee)', 'Physical Disability (Cerebral Palsy)', 'Visually Impaired', 'Deaf', 'Hearing Impaired', 'Deaf & Mute', 'Speech Impairment', 'Other']
income_ranges   = ['Below 5 LPA', '5-10 LPA', '10-15 LPA', '15-20 LPA', '20-30 LPA', '30+ LPA', 'Prefer not to say']

def nav_to(page):
    st.session_state.page = page
    st.rerun()

# ─── NAVBAR ─────────────────────────────────────────────────────────────────
page = st.session_state.page
active_home     = "active" if page == "home"     else ""
active_profiles = "active" if page == "profiles" else ""
active_create   = "active" if page == "create"   else ""

st.markdown(f"""
<div class="navbar">
    <div class="navbar-brand">💖 ShaadiZone</div>
    <div class="navbar-links" id="nav-links"></div>
</div>
""", unsafe_allow_html=True)

nav_cols = st.columns([4, 1, 1, 1, 1, 2])
with nav_cols[1]:
    if st.button("🏠 Home",        key="nav_home",     use_container_width=True,
                 type="primary" if page == "home"     else "secondary"):
        nav_to("home")
with nav_cols[2]:
    if st.button("💖 Members",     key="nav_profiles", use_container_width=True,
                 type="primary" if page == "profiles" else "secondary"):
        nav_to("profiles")
with nav_cols[3]:
    if st.button("💝 Matches",     key="nav_matches",  use_container_width=True,
                 type="primary" if page == "matches"  else "secondary"):
        nav_to("matches")
with nav_cols[4]:
    if st.button("📝 Join Free",   key="nav_create",   use_container_width=True,
                 type="primary" if page == "create"   else "secondary"):
        nav_to("create")

# ─── HOME PAGE ───────────────────────────────────────────────────────────────
def show_home():
    # Hero
    st.markdown(f"""
    <div class="hero">
        <span class="flower">🌸</span>
        <span class="flower">🌷</span>
        <span class="flower">🌺</span>
        <span class="flower">🌹</span>
        <span class="flower">🌻</span>

        <h1>💖 ShaadiZone 💖</h1>
        <p class="hero-subtitle">Inclusive Matrimony for Specially-Abled</p>
        <p class="hero-tagline">Where Every Heart Deserves Love 💕</p>

        <div class="stats-container">
            <div class="stat-box">
                <div class="stat-number">10,000+</div>
                <div class="stat-label">Special Members</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">500+</div>
                <div class="stat-label">Love Stories</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">200+</div>
                <div class="stat-label">Happy Couples</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Support</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CTA strip
    cta_col = st.columns([3, 2, 3])
    with cta_col[1]:
        st.markdown("<div style='margin-top:28px;'>", unsafe_allow_html=True)
        if st.button("💖 Create Free Profile", type="primary", use_container_width=True):
            nav_to("create")
        st.markdown("</div>", unsafe_allow_html=True)

    # Mission
    st.markdown("""
    <div class="mission-box">
        <h2 style="font-family:'Playfair Display',serif; color:#c2185b; font-size:2rem; margin-bottom:14px;">
            Our Beautiful Mission
        </h2>
        <p style="font-size:1.08rem; color:#666; line-height:1.85; max-width:660px; margin:0 auto;">
            ShaadiZone is a loving home for <strong>specially-abled individuals</strong>.
            We believe true love has no boundaries — every heart deserves its happily ever after,
            filled with understanding, respect, and joy.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Why join
    st.markdown('<h2 class="section-title">Why Join ShaadiZone?</h2>', unsafe_allow_html=True)

    cols = st.columns(4)
    features = [
        ("🌷", "Inclusive Platform",    "Built exclusively for specially-abled individuals — you belong here."),
        ("✅", "Verified Profiles",     "Every profile is reviewed and verified for a safe, genuine experience."),
        ("💕", "Loving Community",      "A warm, supportive space where compassion comes first."),
        ("🎉", "Free to Join",          "No hidden charges — love shouldn't have a price tag."),
    ]
    for i, (icon, title, desc) in enumerate(features):
        with cols[i]:
            st.markdown(f"""
            <div class="elegant-card">
                <span class="card-icon">{icon}</span>
                <h4 style="color:#c2185b; margin-bottom:8px; font-size:1rem;">{title}</h4>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="flower-divider">🌸 🌷 🌹 🌺 🌻</div>', unsafe_allow_html=True)

    # Who can join
    st.markdown('<h2 class="section-title">Who Can Join?</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Open to all specially-abled individuals across India</p>', unsafe_allow_html=True)

    cols = st.columns(4)
    categories = [
        ("🦽", "Wheelchair Users",   "#e91e63"),
        ("👁️", "Visually Impaired",  "#c2185b"),
        ("👂", "Hearing Impaired",   "#ad1457"),
        ("💪", "Physically Challenged", "#880e4f"),
    ]
    for i, (icon, title, color) in enumerate(categories):
        with cols[i]:
            st.markdown(f"""
            <div class="elegant-card">
                <span class="card-icon">{icon}</span>
                <h4 style="color:{color}; font-size:0.95rem;">{title}</h4>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="flower-divider">🌸 🌷 🌹 🌺 🌻</div>', unsafe_allow_html=True)

    # Success stories
    st.markdown('<h2 class="section-title">Love Stories</h2>', unsafe_allow_html=True)

    cols = st.columns(3)
    stories = [
        ("Found love beyond my disability! My wife accepts me completely and I couldn't be happier.",     "Ananya & Raj",   "Mumbai"),
        ("As a blind person, I found someone who truly sees my heart. ShaadiZone made it possible!",      "Raj & Priya",    "Delhi"),
        ("Despite being deaf, I heard the wedding bells! Thank you ShaadiZone for this miracle.",         "Diya & Aditya",  "Ahmedabad"),
    ]
    for i, (quote, names, city) in enumerate(stories):
        with cols[i]:
            st.markdown(f"""
            <div class="testimonial-card">
                <p class="testimonial-text">{quote}</p>
                <p class="testimonial-author">— {names} · {city} 💖</p>
            </div>
            """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <div class="footer-inner">
            <p class="footer-title">💖 ShaadiZone 💖</p>
            <p style="opacity:0.9; font-size:1rem; margin-top:4px;">Inclusive Matrimony for Specially-Abled</p>
            <div style="margin:20px 0; opacity:0.5; letter-spacing:8px; font-size:1.1rem;">🌸 🌷 🌹</div>
            <p style="opacity:0.75; font-size:0.8rem;">© 2026 ShaadiZone · Founded by Animesh · Made with 💖</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── PROFILES PAGE ───────────────────────────────────────────────────────────
def show_profiles():
    st.markdown('<h1 class="section-title" style="margin-top:32px;">Find Your Perfect Match</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Browse verified profiles from across India</p>', unsafe_allow_html=True)

    # Filter bar
    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
    with col1: search    = st.text_input("🔍 Search by name or city", placeholder="e.g. Priya, Mumbai…", label_visibility="collapsed")
    with col2: age_filter = st.selectbox("Age Range",  ["All Ages", "21–25", "26–30", "31–35", "35+"], label_visibility="collapsed")
    with col3: loc_filter = st.selectbox("📍 City",   ["All Cities"] + locations,       label_visibility="collapsed")
    with col4: dis_filter = st.selectbox("♿ Type",   ["All Types"] + disability_types,  label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    profiles = list(st.session_state.profiles)

    if search:
        profiles = [p for p in profiles if search.lower() in p['name'].lower() or search.lower() in p['location'].lower()]
    if age_filter != "All Ages":
        if age_filter == "21–25":   profiles = [p for p in profiles if p['age'] <= 25]
        elif age_filter == "26–30": profiles = [p for p in profiles if 25 < p['age'] <= 30]
        elif age_filter == "31–35": profiles = [p for p in profiles if 30 < p['age'] <= 35]
        else:                        profiles = [p for p in profiles if p['age'] > 35]
    if loc_filter != "All Cities":  profiles = [p for p in profiles if p['location'] == loc_filter]
    if dis_filter != "All Types":   profiles = [p for p in profiles if dis_filter in p.get('disability', '')]

    # Result count
    count_col = st.columns([1, 2, 1])
    with count_col[1]:
        st.markdown(f"<div style='text-align:center; margin-bottom:28px;'><span class='result-count'>💖 {len(profiles)} beautiful soul{'s' if len(profiles) != 1 else ''} found</span></div>", unsafe_allow_html=True)

    if not profiles:
        st.markdown("""
        <div style="text-align:center; padding:60px 20px; color:#bbb;">
            <div style="font-size:3rem; margin-bottom:16px;">🔍</div>
            <h3 style="color:#ccc; font-family:'Playfair Display',serif;">No profiles match your filters</h3>
            <p style="font-size:0.9rem; margin-top:8px;">Try adjusting the search criteria above</p>
        </div>
        """, unsafe_allow_html=True)
        return

    cols = st.columns(3)
    for i, profile in enumerate(profiles):
        with cols[i % 3]:
            verified_html = '<span class="verified-pill">✓ Verified</span>' if profile['verified'] else ''
            st.markdown(f"""
            <div class="profile-card">
                <div class="profile-image-area">
                    {verified_html}
                    <span class="avatar">{profile['image']}</span>
                </div>
                <div class="profile-body">
                    <div class="profile-name">{profile['name']}</div>
                    <div class="profile-meta">{profile['age']} yrs &nbsp;·&nbsp; {profile['location']}</div>
                    <div class="profile-job">{profile['profession']} &nbsp;·&nbsp; {profile['education']}</div>
                    <span class="disability-badge">♿ {profile.get('disability', 'N/A')}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("View Profile", key=f"view_{profile['id']}", use_container_width=True):
                st.session_state.selected_profile = profile
                st.session_state.page = "detail"
                st.rerun()


# ─── PROFILE DETAIL ──────────────────────────────────────────────────────────
def show_profile_detail():
    profile = st.session_state.selected_profile

    if st.button("← Back to Profiles"):
        st.session_state.page = "profiles"
        st.rerun()

    st.markdown(f"""
    <div class="detail-header">
        <div style="display:flex; align-items:center; gap:36px; flex-wrap:wrap;">
            <div style="background:rgba(255,255,255,0.2); padding:24px; border-radius:22px; font-size:5rem; line-height:1; backdrop-filter:blur(8px);">
                {profile['image']}
            </div>
            <div>
                <h1 style="color:white; font-family:'Playfair Display',serif; font-size:2.5rem; margin-bottom:6px;">{profile['name']}</h1>
                <p style="color:rgba(255,255,255,0.9); font-size:1.1rem; margin-bottom:4px;">
                    {profile['age']} years &nbsp;·&nbsp; {profile['location']}
                </p>
                <p style="color:rgba(255,255,255,0.8); font-size:0.95rem; margin-bottom:14px;">
                    {profile['profession']} &nbsp;·&nbsp; {profile['education']}
                </p>
                <span class="disability-badge" style="background:rgba(255,255,255,0.25); border-color:rgba(255,255,255,0.35); color:white;">
                    ♿ {profile.get('disability', 'N/A')}
                </span>
                {"&nbsp; <span style='background:rgba(255,255,255,0.2); color:white; padding:4px 12px; border-radius:14px; font-size:0.75rem; font-weight:700;'>✓ Verified</span>" if profile['verified'] else ""}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="detail-card">', unsafe_allow_html=True)
        st.markdown("#### 💖 Personal Details")
        details = [
            ("Profession",  profile['profession']),
            ("Location",    profile['location']),
            ("Education",   profile['education']),
            ("Religion",    profile['religion']),
            ("Disability",  profile.get('disability', 'N/A')),
            ("Income",      profile.get('income', 'Private')),
        ]
        for label, value in details:
            st.markdown(f"<div style='display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #fff0f3;'><span style='color:#999; font-size:0.88rem;'>{label}</span><span style='color:#444; font-weight:500; font-size:0.9rem;'>{value}</span></div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="detail-card">', unsafe_allow_html=True)
        st.markdown("#### 💕 My Story")
        st.markdown(f"<p style='color:#555; line-height:1.8; font-size:0.97rem;'>{profile.get('about', 'A beautiful soul looking for love.')}</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 🎯 Looking For")
        pref_cols = st.columns(2)
        prefs = [("Age", "21–35"), ("Religion", "Any"), ("Career", "Any"), ("Location", "Flexible")]
        for j, (label, value) in enumerate(prefs):
            with pref_cols[j % 2]:
                st.markdown(f"""<div class="preference-item" style="margin-bottom:10px;">
                    <p style="color:#bbb; margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">{label}</p>
                    <p style="color:#c2185b; font-weight:600; margin:4px 0 0 0; font-size:0.95rem;">{value}</p>
                </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="flower-divider">💖 💕 💗 💓 💕</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💌 Send Interest", type="primary", use_container_width=True):
            st.success("💖 Interest sent! They'll be notified.")
    with col2:
        if st.button("💗 Shortlist", use_container_width=True):
            st.success("Added to your favourites!")
    with col3:
        if st.button("📞 Request Contact", use_container_width=True):
            st.info("Contact request sent successfully!")


# ─── CREATE PROFILE ──────────────────────────────────────────────────────────
def show_create_profile():
    st.markdown('<h1 class="section-title" style="margin-top:32px;">Create Your Profile</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Join thousands of specially-abled members looking for love</p>', unsafe_allow_html=True)

    with st.form("create_profile"):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

        st.markdown("#### 👤 Basic Information")
        col1, col2 = st.columns(2)
        with col1:
            name       = st.text_input("Full Name *",   placeholder="Your full name")
            age        = st.number_input("Age *",        min_value=18, max_value=55, value=25)
            profession = st.selectbox("Profession *",   ["Select"] + professions)
            location   = st.selectbox("City *",         ["Select"] + locations)
        with col2:
            education  = st.text_input("Education *",   placeholder="e.g. B.Tech, MBA…")
            religion   = st.selectbox("Religion *",     religions)
            income     = st.selectbox("Income Range",   ["Prefer not to say"] + income_ranges)
            image      = st.selectbox("Profile Avatar", profile_images)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### ♿ Disability Information")

        col1, col2 = st.columns(2)
        with col1: disability_type   = st.selectbox("Disability Type *", ["Select"] + disability_types)
        with col2: disability_detail = st.text_input("Additional Details", placeholder="Brief description (optional)")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 💬 About You")
        about = st.text_area("Your Story *", placeholder="Tell potential matches about yourself — your personality, hobbies, and what you're looking for…", height=130)

        st.markdown("""
        <div class="info-box" style="margin-top:16px;">
            <p style="margin:0; color:#c2185b; font-weight:500; font-size:0.92rem;">
                💖 Your profile will be reviewed and verified within 24 hours of submission.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: submit = st.form_submit_button("💖 Create My Profile", type="primary", use_container_width=True)
        with col2: cancel = st.form_submit_button("Cancel",               use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

        if submit:
            if name and age and profession != "Select" and location != "Select" and education and about and disability_type != "Select":
                new_profile = {
                    "id": len(st.session_state.profiles) + 1,
                    "name": name, "age": age, "profession": profession,
                    "location": location, "education": education, "religion": religion,
                    "image": image, "verified": False, "about": about,
                    "disability": disability_detail if disability_detail else disability_type,
                    "disability_type": disability_type, "income": income,
                }
                st.session_state.profiles.insert(0, new_profile)
                st.success("💖 Profile created successfully! We'll verify it within 24 hours.")
                nav_to("profiles")
            else:
                st.error("Please fill in all required fields marked with *")

        if cancel:
            nav_to("home")


# ─── MATCHING ALGORITHM ──────────────────────────────────────────────────────
_EDU_RANK = {
    'below 10th': 1, '10th': 2, '12th': 3, 'diploma': 4,
    'b.a': 5, 'b.com': 5, 'b.sc': 5, 'b.ed': 5,
    'b.tech': 6, 'b.des': 6, 'b.arch': 6,
    'm.a': 7, 'm.sc': 7, 'm.tech': 8, 'mba': 8, 'mbbs': 9, 'phd': 10,
}

def _edu_rank(edu: str) -> int:
    edu = edu.lower()
    for key, rank in _EDU_RANK.items():
        if key in edu:
            return rank
    return 5

def compute_match_score(prefs: dict, candidate: dict) -> tuple[int, dict]:
    """
    Weighted compatibility score (0–100) with per-factor breakdown.
    Returns (score, {factor: (earned, max)}).
    """
    total = 0
    breakdown = {}

    # ── Age  (25 pts) ─────────────────────────────────────────────────────
    lo, hi = prefs['age_min'], prefs['age_max']
    age = candidate['age']
    if lo <= age <= hi:
        mid  = (lo + hi) / 2
        half = max((hi - lo) / 2, 1)
        pts  = max(15, int(25 * (1 - 0.5 * abs(age - mid) / half)))
    else:
        dist = min(abs(age - lo), abs(age - hi))
        pts  = max(0, 10 - dist * 3)
    total += pts;  breakdown['Age'] = (pts, 25)

    # ── Religion  (20 pts) ────────────────────────────────────────────────
    pts = 20 if prefs['religion'] in ('Any', candidate['religion']) else 0
    total += pts;  breakdown['Religion'] = (pts, 20)

    # ── Location  (20 pts) ────────────────────────────────────────────────
    pts = 20 if prefs['location'] in ('Any City', candidate['location']) else 6
    total += pts;  breakdown['Location'] = (pts, 20)

    # ── Disability type  (20 pts) ─────────────────────────────────────────
    pref_dis  = prefs.get('disability_pref', 'Any')
    cand_type = candidate.get('disability_type', '').lower()
    if pref_dis == 'Any':
        pts = 20
    elif pref_dis.lower() in cand_type or cand_type in pref_dis.lower():
        pts = 20
    else:
        pts = 10          # different disability type — still compatible
    total += pts;  breakdown['Disability'] = (pts, 20)

    # ── Education  (15 pts) ───────────────────────────────────────────────
    my_rank   = _edu_rank(prefs.get('education', ''))
    cand_rank = _edu_rank(candidate['education'])
    pts       = max(0, 15 - abs(my_rank - cand_rank) * 3)
    total += pts;  breakdown['Education'] = (pts, 15)

    return min(100, total), breakdown


def match_label(score: int) -> tuple[str, str, str]:
    """Returns (tag_class, emoji, text)."""
    if score >= 80:
        return 'tag-strong',   '💚', 'Strong Match'
    elif score >= 60:
        return 'tag-good',     '💛', 'Good Match'
    else:
        return 'tag-possible', '🩷', 'Possible Match'


def score_color(score: int) -> str:
    if score >= 80: return 'linear-gradient(135deg,#43a047,#66bb6a)'
    if score >= 60: return 'linear-gradient(135deg,#fb8c00,#ffa726)'
    return         'linear-gradient(135deg,#e91e63,#c2185b)'


# ─── MATCHES PAGE ────────────────────────────────────────────────────────────
def show_matches():
    st.markdown('<h1 class="section-title" style="margin-top:32px;">Your Matches 💖</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Tell us about yourself and we\'ll rank the best profiles for you</p>', unsafe_allow_html=True)

    # ── Preferences panel ────────────────────────────────────────────────
    st.markdown('<div class="prefs-panel">', unsafe_allow_html=True)
    st.markdown("#### ⚙️ Your Preferences")

    pc1, pc2, pc3 = st.columns(3)
    with pc1:
        age_min = st.number_input("Partner Age — Min", min_value=18, max_value=55, value=22)
        religion_pref = st.selectbox("Religion", ["Any"] + religions)
    with pc2:
        age_max = st.number_input("Partner Age — Max", min_value=18, max_value=55, value=32)
        location_pref = st.selectbox("Preferred City", ["Any City"] + locations)
    with pc3:
        disability_pref = st.selectbox("Disability Type", ["Any"] + [
            'Physical', 'Visual', 'Hearing', 'Speech', 'Other'
        ])
        my_education = st.text_input("Your Education", placeholder="e.g. B.Tech, MBA…")

    st.markdown('</div>', unsafe_allow_html=True)

    prefs = {
        'age_min':        age_min,
        'age_max':        age_max,
        'religion':       religion_pref,
        'location':       location_pref,
        'disability_pref':disability_pref,
        'education':      my_education or 'B.Tech',
    }

    # ── Score all profiles ────────────────────────────────────────────────
    scored = []
    for p in st.session_state.profiles:
        score, breakdown = compute_match_score(prefs, p)
        scored.append((score, breakdown, p))
    scored.sort(key=lambda x: x[0], reverse=True)

    # ── Summary strip ─────────────────────────────────────────────────────
    strong  = sum(1 for s, _, _ in scored if s >= 80)
    good    = sum(1 for s, _, _ in scored if 60 <= s < 80)
    possible= sum(1 for s, _, _ in scored if s < 60)

    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1: st.metric("Total Profiles", len(scored))
    with sc2: st.metric("💚 Strong Matches",   strong)
    with sc3: st.metric("💛 Good Matches",      good)
    with sc4: st.metric("🩷 Possible Matches",  possible)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Match cards ───────────────────────────────────────────────────────
    for rank, (score, breakdown, profile) in enumerate(scored, 1):
        tag_cls, tag_emoji, tag_text = match_label(score)
        ring_bg = score_color(score)

        # Build factor bars HTML
        factor_html = ""
        for factor, (earned, max_pts) in breakdown.items():
            pct   = int(earned / max_pts * 100)
            bar_c = '#4caf50' if pct >= 80 else '#fb8c00' if pct >= 50 else '#e91e63'
            factor_html += f"""
            <div class="factor-row">
                <span class="factor-name">{factor}</span>
                <div class="factor-bar-wrap">
                    <div class="factor-bar" style="width:{pct}%; background:{bar_c};"></div>
                </div>
                <span class="factor-pct">{pct}%</span>
            </div>"""

        verified_badge = '<span style="background:#e8f5e9;color:#2e7d32;padding:2px 8px;border-radius:10px;font-size:0.7rem;font-weight:700;">✓ Verified</span>' if profile['verified'] else ''

        st.markdown(f"""
        <div class="match-card">
            <div class="match-rank">#{rank}</div>
            <div class="match-avatar">{profile['image']}</div>
            <div class="match-info">
                <div class="match-name">{profile['name']}
                    &nbsp;{verified_badge}
                </div>
                <div class="match-meta">
                    {profile['age']} yrs &nbsp;·&nbsp; {profile['location']} &nbsp;·&nbsp;
                    {profile['profession']} &nbsp;·&nbsp; {profile['education']}
                </div>
                <span class="disability-badge">♿ {profile.get('disability','N/A')}</span>
                <span class="match-tag {tag_cls}">&nbsp;{tag_emoji} {tag_text}&nbsp;</span>
                <div style="margin-top:14px;">{factor_html}</div>
            </div>
            <div class="match-score-block">
                <div class="score-ring" style="background:{ring_bg};">{score}%</div>
                <div class="score-label" style="color:{'#2e7d32' if score>=80 else '#f57f17' if score>=60 else '#c2185b'};">
                    {tag_text}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Action buttons under each card
        b1, b2, b3, _ = st.columns([1, 1, 1, 3])
        with b1:
            if st.button("💌 Interest", key=f"int_{profile['id']}", use_container_width=True, type="primary"):
                st.success(f"Interest sent to {profile['name']}!")
        with b2:
            if st.button("👤 Profile",  key=f"mp_{profile['id']}",  use_container_width=True):
                st.session_state.selected_profile = profile
                st.session_state.page = "detail"
                st.rerun()
        with b3:
            if st.button("💗 Shortlist", key=f"sl_{profile['id']}", use_container_width=True):
                st.success(f"{profile['name']} added to favourites!")


# ─── ROUTER ─────────────────────────────────────────────────────────────────
if   st.session_state.page == "home":     show_home()
elif st.session_state.page == "profiles": show_profiles()
elif st.session_state.page == "detail":   show_profile_detail()
elif st.session_state.page == "create":   show_create_profile()
elif st.session_state.page == "matches":  show_matches()
