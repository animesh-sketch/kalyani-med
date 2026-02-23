import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="ShaadiZone", page_icon="💍", layout="wide")

if 'profiles' not in st.session_state:
    st.session_state.profiles = [
        {"id": 1, "name": "Priya Sharma", "age": 26, "profession": "Software Engineer", "location": "Mumbai", "height": "5'6\"", "education": "B.Tech", "religion": "Hindu", "image": "👩‍💻", "verified": True, "about": "Software engineer passionate about technology and travel."},
        {"id": 2, "name": "Rahul Verma", "age": 28, "profession": "Doctor", "location": "Delhi", "height": "5'10\"", "education": "MBBS", "religion": "Hindu", "image": "👨‍⚕️", "verified": True, "about": "Doctor by profession, explorer by heart."},
        {"id": 3, "name": "Anjali Patel", "age": 24, "profession": "Teacher", "location": "Ahmedabad", "height": "5'3\"", "education": "M.A. B.Ed", "religion": "Hindu", "image": "👩‍🏫", "verified": False, "about": "Teaching is my passion, kids are my joy."},
        {"id": 4, "name": "Vikram Singh", "age": 30, "profession": "Business Owner", "location": "Jaipur", "height": "5'11\"", "education": "MBA", "religion": "Hindu", "image": "👨‍💼", "verified": True, "about": "Entrepreneur building dreams."},
        {"id": 5, "name": "Meera Nair", "age": 27, "profession": "Designer", "location": "Bangalore", "height": "5'4\"", "education": "B.Des", "religion": "Hindu", "image": "👩‍🎨", "verified": True, "about": "Designing beautiful experiences."},
        {"id": 6, "name": "Arjun Menon", "age": 29, "profession": "Engineer", "location": "Kochi", "height": "5'9\"", "education": "B.Tech", "religion": "Hindu", "image": "👨‍🔧", "verified": False, "about": "Engineer with a creative side."},
        {"id": 7, "name": "Kavya Reddy", "age": 25, "profession": "Marketing Manager", "location": "Hyderabad", "height": "5'5\"", "education": "MBA", "religion": "Hindu", "image": "👩‍💼", "verified": True, "about": "Marketing professional who loves storytelling."},
        {"id": 8, "name": "Dev Kapoor", "age": 31, "profession": "CA", "location": "Mumbai", "height": "5'8\"", "education": "CA", "religion": "Hindu", "image": "👨‍💼", "verified": True, "about": "Chartered Accountant with a balanced life."},
    ]

if 'page' not in st.session_state:
    st.session_state.page = "home"

if 'selected_profile' not in st.session_state:
    st.session_state.selected_profile = None

profile_images = ["👨‍💼", "👩‍💼", "👨‍💻", "👩‍💻", "👨‍⚕️", "👩‍⚕️", "👨‍🎓", "👩‍🎓", "👨‍🔬", "👩‍🔬", "👨‍🏫", "👩‍🏫", "👨‍🎨", "👩‍🎨"]
locations = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Jaipur', 'Ahmedabad', 'Kochi', 'Kolkata']
religions = ['Hindu', 'Muslim', 'Christian', 'Sikh', 'Buddhist', 'Jain', 'Other']
professions = ['Software Engineer', 'Doctor', 'Teacher', 'Engineer', 'Business Owner', 'Designer', 'Marketing Manager', 'CA', 'Banker', 'Architect', 'Data Scientist', 'Lawyer', 'Other']

def nav_to(page):
    st.session_state.page = page
    st.rerun()

def show_home():
    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 60px 20px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 40px;
    }
    .hero h1 { font-size: 3rem; margin-bottom: 10px; }
    .hero p { font-size: 1.3rem; opacity: 0.9; }
    .stats { display: flex; justify-content: center; gap: 40px; margin-top: 30px; }
    .stat-item { text-align: center; }
    .stat-number { font-size: 2rem; font-weight: bold; }
    .feature-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    .success-story {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero">
        <h1>💍 Find Your Perfect Partner</h1>
        <p>Join 2+ million happy couples who found their soulmate on ShaadiZone</p>
        <div class="stats">
            <div class="stat-item">
                <div class="stat-number">2M+</div>
                <div>Members</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">50K+</div>
                <div>Success Stories</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">1000+</div>
                <div>Daily Matches</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 📝 Register Free & Create Your Profile")
        st.markdown("""
        - ✅ Create your profile in minutes
        - ✅ Get verified badge
        - ✅ Connect with compatible matches
        - ✅ Chat with genuine people
        """)
        if st.button("Create Free Profile", type="primary"):
            nav_to("create")
    with col2:
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px;">
            <p style="font-style: italic; color: #666;">"Found my perfect match here! We're getting married next month."</p>
            <p style="font-weight: bold; color: #e91e63;">- Priya, 26</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌟 Why Choose ShaadiZone?")
    
    cols = st.columns(4)
    features = [
        ("🔍", "Smart Matching", "AI algorithm finds compatible matches"),
        ("🛡️", "Verified Profiles", "All profiles manually verified"),
        ("💬", "Easy Communication", "Secure messaging system"),
        ("📱", "Mobile Friendly", "Access anywhere on any device"),
    ]
    for i, (icon, title, desc) in enumerate(features):
        with cols[i]:
            st.markdown(f"""
            <div class="feature-card">
                <div style="font-size: 3rem;">{icon}</div>
                <h4>{title}</h4>
                <p style="color: #666;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 💕 Success Stories")
    
    cols = st.columns(3)
    stories = [
        ("We found each other on ShaadiZone and knew instantly this was meant to be.", "Rahul & Priya", "💕"),
        ("After trying other apps, ShaadiZone helped me find my perfect match.", "Amit & Sneha", "💍"),
        ("Best decision I made was to join ShaadiZone. We're now happily married!", "Raj & Kavya", "❤️"),
    ]
    for i, (quote, names, emoji) in enumerate(stories):
        with cols[i]:
            st.markdown(f"""
            <div class="success-story">
                <div style="font-size: 2rem;">{emoji}</div>
                <p style="font-style: italic; color: #666;">"{quote}"</p>
                <p style="font-weight: bold; color: #e91e63;">- {names}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown(f"<p style='text-align: center; color: #888;'>Made with ❤️ by Animesh | Founded by Animesh</p>", unsafe_allow_html=True)

def show_profiles():
    st.markdown(f"<h1 style='text-align: center;'>Browse Profiles</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #666; margin-bottom: 30px;'>Find your perfect match from our verified profiles</p>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        search = st.text_input("Search by name", placeholder="Search...")
    with col2:
        age_filter = st.selectbox("Age", ["All", "18-25", "26-30", "30+"])
    with col3:
        loc_filter = st.selectbox("Location", ["All"] + locations)
    with col4:
        prof_filter = st.selectbox("Profession", ["All"] + professions)
    
    profiles = st.session_state.profiles
    
    if search:
        profiles = [p for p in profiles if search.lower() in p['name'].lower() or search.lower() in p['location'].lower()]
    if age_filter != "All":
        if age_filter == "18-25":
            profiles = [p for p in profiles if p['age'] <= 25]
        elif age_filter == "26-30":
            profiles = [p for p in profiles if 25 < p['age'] <= 30]
        else:
            profiles = [p for p in profiles if p['age'] > 30]
    if loc_filter != "All":
        profiles = [p for p in profiles if p['location'] == loc_filter]
    if prof_filter != "All":
        profiles = [p for p in profiles if prof_filter in p['profession']]
    
    st.markdown(f"<p style='color: #666;'>{len(profiles)} profiles found</p>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, profile in enumerate(profiles):
        with cols[i % 4]:
            with st.container():
                st.markdown(f"""
                <div style="background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px;">
                    <div style="background: linear-gradient(135deg, #fce4ec, #f8bbd0); padding: 30px; text-align: center; font-size: 4rem;">
                        {profile['image']}
                    </div>
                    <div style="padding: 15px;">
                        <h3 style="margin: 0;">{profile['name']}</h3>
                        <p style="color: #e91e63; margin: 5px 0;">{profile['age']} yrs</p>
                        <p style="color: #666; font-size: 0.9rem;">{profile['profession']}</p>
                        <p style="color: #666; font-size: 0.9rem;">📍 {profile['location']}</p>
                        <p style="color: #666; font-size: 0.9rem;">🎓 {profile['education']}</p>
                        {f'<span style="background: #4caf50; color: white; padding: 3px 10px; border-radius: 10px; font-size: 0.8rem;">✓ Verified</span>' if profile['verified'] else ''}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"View {profile['id']}", key=f"view_{profile['id']}"):
                    st.session_state.selected_profile = profile
                    st.session_state.page = "detail"
                    st.rerun()

def show_profile_detail():
    profile = st.session_state.selected_profile
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("← Back to Profiles"):
            st.session_state.page = "profiles"
            st.rerun()
    
    st.markdown(f"""
    <div style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin-top: 20px;">
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 40px; display: flex; align-items: center; gap: 30px;">
            <div style="background: white; border-radius: 20px; padding: 20px; font-size: 5rem;">{profile['image']}</div>
            <div>
                <h1 style="color: white; margin: 0;">{profile['name']}</h1>
                <p style="color: white; opacity: 0.9; font-size: 1.2rem;">{profile['age']} years old • {profile['height']}</p>
                <p style="color: white; opacity: 0.9;">📍 {profile['location']}</p>
                {f'<span style="background: #4caf50; color: white; padding: 5px 15px; border-radius: 20px;">✓ Verified Profile</span>' if profile['verified'] else ''}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 👤 Personal Details")
        details = [
            ("Profession", profile['profession']),
            ("Height", profile['height']),
            ("Location", profile['location']),
            ("Education", profile['education']),
            ("Religion", profile['religion']),
        ]
        for label, value in details:
            st.markdown(f"**{label}:** {value}")
    
    with col2:
        st.markdown("### 📝 About Me")
        st.write(profile.get('about', f"Hello! I'm {profile['name']}, a {profile['profession']} based in {profile['location']}. I have completed my {profile['education']}. Looking for someone who shares similar values."))
    
    st.markdown("### 💕 Partner Preferences")
    cols = st.columns(4)
    prefs = [("Age", "22-30 years"), ("Height", "5'2\" - 5'10\""), ("Profession", "Professional"), ("Location", "Any Indian City")]
    for i, (label, value) in enumerate(prefs):
        with cols[i]:
            st.markdown(f"""
            <div style="background: #fce4ec; padding: 15px; border-radius: 10px; text-align: center;">
                <p style="color: #666; margin: 0;">{label}</p>
                <p style="color: #e91e63; font-weight: bold; margin: 5px 0 0 0;">{value}</p>
            </div>
            """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💌 Send Interest", type="primary", use_container_width=True):
            st.success("Interest sent!")
    with col2:
        if st.button("💬 Chat", use_container_width=True):
            st.info("Chat feature coming soon!")
    with col3:
        if st.button("⭐ Shortlist", use_container_width=True):
            st.success("Profile shortlisted!")

def show_create_profile():
    st.markdown(f"<h1 style='text-align: center;'>Create Your Profile</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #666;'>Fill in your details to find your perfect match</p>", unsafe_allow_html=True)
    
    with st.form("create_profile"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name *")
            age = st.number_input("Age *", min_value=18, max_value=50)
            profession = st.selectbox("Profession *", ["Select"] + professions)
            location = st.selectbox("Location *", ["Select"] + locations)
        with col2:
            height = st.selectbox("Height", ["Select"] + ["4'6\"", "4'7\"", "4'8\"", "4'9\"", "4'10\"", "4'11\"", "5'0\"", "5'1\"", "5'2\"", "5'3\"", "5'4\"", "5'5\"", "5'6\"", "5'7\"", "5'8\"", "5'9\"", "5'10\"", "5'11\"", "6'0\""])
            education = st.text_input("Education *")
            religion = st.selectbox("Religion *", religions)
            image = st.selectbox("Choose Avatar", profile_images)
        
        about = st.text_area("About Yourself")
        
        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button("Create Profile", type="primary", use_container_width=True)
        with col2:
            cancel = st.form_submit_button("Cancel", use_container_width=True)
        
        if submit:
            if name and age and profession != "Select" and location != "Select" and education:
                new_profile = {
                    "id": len(st.session_state.profiles) + 1,
                    "name": name,
                    "age": age,
                    "profession": profession,
                    "location": location,
                    "height": height if height != "Select" else "",
                    "education": education,
                    "religion": religion,
                    "image": image,
                    "verified": False,
                    "about": about
                }
                st.session_state.profiles.insert(0, new_profile)
                st.success("Profile created successfully!")
                nav_to("profiles")
            else:
                st.error("Please fill in all required fields!")
        
        if cancel:
            nav_to("home")

# Main app
st.markdown("""
<style>
    .stButton > button {
        border-radius: 25px;
    }
    .main-nav {
        display: flex;
        justify-content: center;
        gap: 20px;
        padding: 20px;
        background: white;
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .nav-btn {
        padding: 10px 30px;
        border-radius: 25px;
        border: none;
        cursor: pointer;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
nav_cols = st.columns([1, 2, 1])
with nav_cols[1]:
    nav_options = ["🏠 Home", "👥 Browse Profiles", "📝 Create Profile"]
    selected_nav = st.radio("Navigation", nav_options, 
                          index=0 if st.session_state.page == "home" else 1 if st.session_state.page == "profiles" else 2,
                          label_visibility="collapsed", horizontal=True)
    
    if "Home" in selected_nav and st.session_state.page != "home":
        nav_to("home")
    elif "Browse" in selected_nav and st.session_state.page != "profiles":
        nav_to("profiles")
    elif "Create" in selected_nav and st.session_state.page != "create":
        nav_to("create")

# Page content
if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "profiles":
    show_profiles()
elif st.session_state.page == "detail":
    show_profile_detail()
elif st.session_state.page == "create":
    show_create_profile()

# Footer
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #888;'>© 2026 ShaadiZone. All rights reserved. | Founded by Animesh</p>", unsafe_allow_html=True)
