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

    /* ─── PHOTOS ─── */
    .profile-photo {
        width: 88px;
        height: 88px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid rgba(255,255,255,0.55);
        box-shadow: 0 4px 18px rgba(0,0,0,0.22);
        display: block;
        margin: 0 auto;
        background: linear-gradient(135deg,#e91e63,#c2185b);
    }

    .detail-photo {
        width: 120px;
        height: 120px;
        border-radius: 22px;
        object-fit: cover;
        border: 3px solid rgba(255,255,255,0.35);
        box-shadow: 0 8px 28px rgba(0,0,0,0.28);
        background: linear-gradient(135deg,#e91e63,#c2185b);
    }

    .match-photo {
        width: 64px;
        height: 64px;
        border-radius: 16px;
        object-fit: cover;
        border: 2px solid rgba(233,30,99,0.2);
        box-shadow: 0 3px 10px rgba(0,0,0,0.12);
        background: linear-gradient(135deg,#e91e63,#c2185b);
    }

    /* upload preview */
    .photo-preview {
        width: 110px;
        height: 110px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #f8bbd0;
        box-shadow: 0 4px 16px rgba(233,30,99,0.15);
        display: block;
        margin: 0 auto 12px;
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

    /* ─── LANDING: HERO CINEMATIC ─── */
    .hero-cinematic {
        background: linear-gradient(160deg, #1a0010 0%, #3d0020 30%, #6b0030 60%, #c2185b 100%);
        min-height: 96vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 80px 40px 60px;
        position: relative;
        overflow: hidden;
    }

    .hero-cinematic::before {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(ellipse 80% 60% at 50% 40%, rgba(201,168,76,0.08) 0%, transparent 70%);
        pointer-events: none;
    }

    .hero-cinematic::after {
        content: '';
        position: absolute;
        bottom: -2px; left: 0; right: 0;
        height: 80px;
        background: linear-gradient(160deg, #fff0f3 0%, #fde8ee 40%, #fff5f7 100%);
        clip-path: ellipse(60% 100% at 50% 100%);
    }

    /* Floating orbs */
    .orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(60px);
        opacity: 0.18;
        animation: orbFloat 18s ease-in-out infinite;
    }
    .orb1 { width:400px; height:400px; background:#e91e63; top:-100px; left:-120px; animation-delay:0s; }
    .orb2 { width:300px; height:300px; background:#c9a84c; bottom:-80px; right:-80px; animation-delay:5s; }
    .orb3 { width:250px; height:250px; background:#ad1457; top:30%; right:5%; animation-delay:10s; }

    @keyframes orbFloat {
        0%,100% { transform: translate(0,0) scale(1); }
        50%      { transform: translate(20px,-30px) scale(1.08); }
    }

    /* Floating petals */
    .petal {
        position: absolute;
        font-size: 1.6rem;
        opacity: 0.18;
        animation: petalDrift 15s ease-in-out infinite;
    }
    .petal:nth-child(1) { top:10%; left:5%;  animation-delay:0s;  font-size:1.2rem; }
    .petal:nth-child(2) { top:20%; right:6%; animation-delay:3s;  font-size:1.8rem; }
    .petal:nth-child(3) { top:55%; left:3%;  animation-delay:6s;  font-size:1.4rem; }
    .petal:nth-child(4) { top:70%; right:8%; animation-delay:9s;  font-size:1rem; }
    .petal:nth-child(5) { top:38%; left:8%;  animation-delay:12s; font-size:2rem; }

    @keyframes petalDrift {
        0%,100% { transform: translateY(0) rotate(0deg);  opacity: 0.18; }
        50%      { transform: translateY(-25px) rotate(15deg); opacity: 0.28; }
    }

    /* Gold script */
    .gold-script {
        font-family: 'Playfair Display', serif;
        font-size: 0.9rem;
        font-weight: 400;
        font-style: italic;
        color: #c9a84c;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 20px;
        position: relative;
        z-index: 2;
    }

    .gold-script::before,
    .gold-script::after {
        content: '—';
        margin: 0 12px;
        opacity: 0.6;
    }

    /* Main headline */
    .hero-headline {
        font-family: 'Playfair Display', serif;
        font-size: 5.5rem;
        font-weight: 700;
        color: white;
        line-height: 1.1;
        margin-bottom: 22px;
        position: relative;
        z-index: 2;
        text-shadow: 0 4px 40px rgba(0,0,0,0.4);
        letter-spacing: -1.5px;
    }

    .hero-headline .gold-word {
        color: #c9a84c;
        font-style: italic;
    }

    .hero-tagline-new {
        font-size: 1.15rem;
        color: rgba(255,255,255,0.72);
        line-height: 1.7;
        max-width: 560px;
        margin: 0 auto 36px;
        position: relative;
        z-index: 2;
        font-weight: 300;
    }

    .hero-cta-group {
        display: flex;
        gap: 16px;
        justify-content: center;
        position: relative;
        z-index: 2;
        margin-bottom: 56px;
        flex-wrap: wrap;
    }

    .btn-gold {
        background: linear-gradient(135deg, #c9a84c, #a8863c);
        color: #1a0010 !important;
        border: none;
        padding: 16px 40px;
        border-radius: 50px;
        font-size: 1rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        cursor: pointer;
        box-shadow: 0 8px 28px rgba(201,168,76,0.4);
        transition: all 0.3s ease;
        text-decoration: none;
    }

    .btn-ghost {
        background: rgba(255,255,255,0.08);
        color: white !important;
        border: 1.5px solid rgba(255,255,255,0.3);
        padding: 15px 38px;
        border-radius: 50px;
        font-size: 1rem;
        font-weight: 500;
        cursor: pointer;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        text-decoration: none;
    }

    /* Hero stats */
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 0;
        position: relative;
        z-index: 2;
        border-top: 1px solid rgba(255,255,255,0.1);
        padding-top: 36px;
        width: 100%;
        max-width: 680px;
    }

    .hero-stat {
        flex: 1;
        text-align: center;
        padding: 0 24px;
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    .hero-stat:last-child { border-right: none; }

    .hero-stat-num {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #c9a84c;
    }

    .hero-stat-lbl {
        font-size: 0.75rem;
        color: rgba(255,255,255,0.5);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 4px;
    }

    /* ─── GOLD DIVIDER ─── */
    .gold-divider {
        display: flex;
        align-items: center;
        gap: 16px;
        margin: 56px auto;
        max-width: 340px;
    }

    .gold-divider-line {
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, transparent, #c9a84c, transparent);
    }

    .gold-divider-icon {
        color: #c9a84c;
        font-size: 1.1rem;
        opacity: 0.8;
    }

    /* ─── BELIEF STRIP ─── */
    .belief-strip {
        background: linear-gradient(135deg, #2d0018, #4a0028);
        padding: 72px 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
        margin: 0;
    }

    .belief-strip::before {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(ellipse 60% 80% at 50% 50%, rgba(201,168,76,0.06) 0%, transparent 70%);
    }

    .belief-quote {
        font-family: 'Playfair Display', serif;
        font-size: 2.4rem;
        font-style: italic;
        color: white;
        line-height: 1.4;
        max-width: 820px;
        margin: 0 auto 20px;
        position: relative;
        z-index: 1;
        letter-spacing: -0.3px;
    }

    .belief-quote .gold-em { color: #c9a84c; }

    .belief-sub {
        color: rgba(255,255,255,0.45);
        font-size: 0.88rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        position: relative;
        z-index: 1;
    }

    /* ─── PROMISE CARDS ─── */
    .promise-card {
        background: white;
        border-radius: 28px;
        padding: 40px 28px;
        text-align: center;
        box-shadow: 0 12px 40px rgba(193,18,91,0.08);
        border: 1px solid rgba(201,168,76,0.15);
        height: 100%;
        transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
        position: relative;
        overflow: hidden;
    }

    .promise-card::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #c9a84c, #e91e63, #c9a84c);
    }

    .promise-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 24px 60px rgba(193,18,91,0.14);
    }

    .promise-icon-wrap {
        width: 72px;
        height: 72px;
        border-radius: 50%;
        background: linear-gradient(135deg, #fff0f3, #fde8ee);
        border: 2px solid rgba(201,168,76,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        margin: 0 auto 20px;
    }

    /* ─── HOW IT WORKS ─── */
    .steps-section {
        background: linear-gradient(160deg, #1a0010 0%, #2d0018 100%);
        padding: 80px 40px;
        position: relative;
        overflow: hidden;
    }

    .steps-section::before {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(ellipse 70% 50% at 50% 50%, rgba(201,168,76,0.05) 0%, transparent 70%);
    }

    .step-card {
        text-align: center;
        padding: 32px 20px;
        position: relative;
        z-index: 1;
    }

    .step-num {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 700;
        color: rgba(201,168,76,0.2);
        line-height: 1;
        margin-bottom: 8px;
    }

    .step-icon {
        font-size: 2.2rem;
        margin-bottom: 16px;
        display: block;
    }

    .step-title {
        font-family: 'Playfair Display', serif;
        color: white;
        font-size: 1.25rem;
        margin-bottom: 10px;
    }

    .step-desc { color: rgba(255,255,255,0.5); font-size: 0.88rem; line-height: 1.7; }

    .step-connector {
        position: absolute;
        top: 48px;
        right: -20px;
        color: rgba(201,168,76,0.3);
        font-size: 1.4rem;
        z-index: 2;
    }

    /* ─── TESTIMONIAL CINEMATIC ─── */
    .story-card-big {
        background: white;
        border-radius: 28px;
        padding: 44px 36px 36px;
        box-shadow: 0 16px 50px rgba(193,18,91,0.10);
        border: 1px solid rgba(201,168,76,0.12);
        position: relative;
        overflow: hidden;
        height: 100%;
        transition: all 0.4s ease;
    }

    .story-card-big:hover {
        transform: translateY(-6px);
        box-shadow: 0 24px 64px rgba(193,18,91,0.16);
    }

    .story-card-big::before {
        content: '\201C';
        font-family: 'Playfair Display', serif;
        font-size: 9rem;
        color: #f8bbd0;
        position: absolute;
        top: -20px;
        left: 24px;
        line-height: 1;
        opacity: 0.5;
    }

    .story-text {
        font-size: 1.05rem;
        color: #444;
        font-style: italic;
        line-height: 1.85;
        margin-top: 32px;
        position: relative;
        z-index: 1;
    }

    .story-author-row {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-top: 24px;
        padding-top: 20px;
        border-top: 1px solid #f8eef2;
    }

    .story-avatar {
        font-size: 2.2rem;
        background: linear-gradient(135deg, #e91e63, #c2185b);
        border-radius: 50%;
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .story-name { font-weight: 600; color: #c2185b; font-size: 0.95rem; }
    .story-city { color: #bbb; font-size: 0.8rem; margin-top: 1px; }

    .story-hearts {
        margin-left: auto;
        color: #f8bbd0;
        font-size: 1.1rem;
        letter-spacing: 2px;
    }

    /* ─── CTA FINAL ─── */
    .cta-final {
        background: linear-gradient(135deg, #3d0020 0%, #6b0030 40%, #c2185b 100%);
        padding: 100px 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .cta-final::before {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(ellipse 70% 60% at 50% 50%, rgba(201,168,76,0.1) 0%, transparent 70%);
    }

    .cta-final-heading {
        font-family: 'Playfair Display', serif;
        font-size: 3.8rem;
        font-weight: 700;
        color: white;
        line-height: 1.2;
        margin-bottom: 18px;
        position: relative;
        z-index: 1;
    }

    .cta-final-sub {
        color: rgba(255,255,255,0.65);
        font-size: 1.05rem;
        max-width: 500px;
        margin: 0 auto 40px;
        line-height: 1.7;
        position: relative;
        z-index: 1;
    }

    /* ─── FOOTER LUXURY ─── */
    .footer-luxury {
        background: #0d0008;
        color: white;
        padding: 64px 40px 32px;
        text-align: center;
    }

    .footer-logo {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #c9a84c;
        margin-bottom: 6px;
    }

    .footer-tagline-lux {
        color: rgba(255,255,255,0.4);
        font-size: 0.82rem;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-bottom: 32px;
    }

    .footer-gold-rule {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(201,168,76,0.4), transparent);
        margin: 28px auto;
        max-width: 400px;
    }

    .footer-copy {
        color: rgba(255,255,255,0.2);
        font-size: 0.78rem;
        letter-spacing: 1px;
    }

    /* Existing section title tweaks */
    .section-title-light {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        text-align: center;
        margin-bottom: 8px;
        color: white;
        letter-spacing: -0.5px;
    }

    .section-subtitle-light {
        text-align: center;
        color: rgba(255,255,255,0.45);
        font-size: 0.95rem;
        margin-bottom: 48px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Hide Streamlit chrome */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stDeployButton { display: none; }
    .block-container { padding-top: 0 !important; padding-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── HELPERS ────────────────────────────────────────────────────────────────
def get_avatar_url(name: str, style: str = "lorelei") -> str:
    """DiceBear illustrated avatar — unique per name, hosted CDN, no key needed."""
    import urllib.parse
    seed = urllib.parse.quote(name.replace(" ", ""))
    return (f"https://api.dicebear.com/9.x/{style}/svg"
            f"?seed={seed}&backgroundColor=fce4ec,f8bbd0,e91e63&backgroundType=solid"
            f"&radius=50")

# ─── DATA ───────────────────────────────────────────────────────────────────
if 'profiles' not in st.session_state:
    _names = ["Ananya Sharma","Raj Verma","Diya Patel","Aditya Singh","Myra Nair","Karan Menon"]
    st.session_state.profiles = [
        {"id": 1, "name": "Ananya Sharma",  "age": 26, "profession": "Software Engineer", "location": "Mumbai",    "education": "B.Tech",    "religion": "Hindu", "image": "👩‍💻", "verified": True,  "about": "I use a wheelchair but that doesn't stop me from dreaming big!",          "disability": "Wheelchair User",  "disability_type": "Physical", "income": "8-10 LPA",  "photo": get_avatar_url("Ananya Sharma")},
        {"id": 2, "name": "Raj Verma",      "age": 28, "profession": "Doctor",            "location": "Delhi",     "education": "MBBS",      "religion": "Hindu", "image": "👨‍⚕️", "verified": True,  "about": "Born blind but I see the world with my heart.",                           "disability": "Visually Impaired","disability_type": "Visual",    "income": "15-20 LPA", "photo": get_avatar_url("Raj Verma")},
        {"id": 3, "name": "Diya Patel",     "age": 24, "profession": "Teacher",           "location": "Ahmedabad", "education": "M.A. B.Ed", "religion": "Hindu", "image": "👩‍🏫", "verified": True,  "about": "I can't hear but I can feel love!",                                       "disability": "Deaf & Mute",      "disability_type": "Hearing",   "income": "5-6 LPA",   "photo": get_avatar_url("Diya Patel")},
        {"id": 4, "name": "Aditya Singh",   "age": 30, "profession": "Business Owner",    "location": "Jaipur",    "education": "MBA",       "religion": "Hindu", "image": "👨‍💼", "verified": True,  "about": "Lost my leg but gained perspective!",                                     "disability": "Amputee",          "disability_type": "Physical",  "income": "25-30 LPA", "photo": get_avatar_url("Aditya Singh")},
        {"id": 5, "name": "Myra Nair",      "age": 27, "profession": "Fashion Designer",  "location": "Bangalore", "education": "B.Des",     "religion": "Hindu", "image": "👩‍🎨", "verified": True,  "about": "Creating beautiful designs and seeking love!",                            "disability": "Hearing Impaired", "disability_type": "Hearing",   "income": "6-8 LPA",   "photo": get_avatar_url("Myra Nair")},
        {"id": 6,  "name": "Karan Menon",      "age": 29, "profession": "Engineer",          "location": "Kochi",       "education": "B.Tech",      "religion": "Hindu",     "image": "👨‍💻", "verified": True,  "about": "Born with cerebral palsy but I'm an engineer and proud of it!",                                     "disability": "Cerebral Palsy",    "disability_type": "Physical",  "income": "12-15 LPA", "photo": get_avatar_url("Karan Menon")},
        {"id": 7,  "name": "Priya Iyer",        "age": 25, "profession": "Graphic Designer",  "location": "Chennai",     "education": "B.Des",       "religion": "Hindu",     "image": "👩‍🎨", "verified": True,  "about": "I was born without my left hand but my art speaks louder than words. Looking for someone who loves life as much as I do!",             "disability": "Limb Difference",   "disability_type": "Physical",  "income": "6-8 LPA",   "photo": get_avatar_url("Priya Iyer")},
        {"id": 8,  "name": "Arjun Kapoor",      "age": 32, "profession": "CA",                "location": "Mumbai",      "education": "CA",          "religion": "Hindu",     "image": "👨‍💼", "verified": True,  "about": "Spinal injury from an accident but it only made me stronger. I love cricket, music and long drives.",                                "disability": "Spinal Injury",     "disability_type": "Physical",  "income": "20-25 LPA", "photo": get_avatar_url("Arjun Kapoor")},
        {"id": 9,  "name": "Zara Sheikh",        "age": 26, "profession": "Journalist",        "location": "Hyderabad",   "education": "M.A.",        "religion": "Muslim",    "image": "👩‍💻", "verified": True,  "about": "I am visually impaired and I write about the world I imagine. My words have been published in three national newspapers.",             "disability": "Visually Impaired", "disability_type": "Visual",    "income": "8-10 LPA",  "photo": get_avatar_url("Zara Sheikh")},
        {"id": 10, "name": "Samuel Mathew",      "age": 31, "profession": "Software Engineer", "location": "Bangalore",   "education": "B.Tech",      "religion": "Christian", "image": "👨‍💻", "verified": True,  "about": "Deaf since birth, fluent in ISL. I build apps by day and cook elaborate meals by night. Seeking my person.",                         "disability": "Deaf",              "disability_type": "Hearing",   "income": "15-18 LPA", "photo": get_avatar_url("Samuel Mathew")},
        {"id": 11, "name": "Kavya Reddy",        "age": 24, "profession": "Physiotherapist",   "location": "Hyderabad",   "education": "B.P.T.",      "religion": "Hindu",     "image": "👩‍⚕️", "verified": True,  "about": "I help others heal every day. I have MS but it doesn't define me — my kindness and my laughter do.",                                 "disability": "Multiple Sclerosis","disability_type": "Physical",  "income": "5-7 LPA",   "photo": get_avatar_url("Kavya Reddy")},
        {"id": 12, "name": "Rohan Bose",         "age": 28, "profession": "Photographer",      "location": "Kolkata",     "education": "B.F.A.",      "religion": "Hindu",     "image": "👨‍🎨", "verified": True,  "about": "I lost my sight in one eye but I still see beauty everywhere. My photographs have won national awards. Love poetry and rain.",       "disability": "Partial Blindness", "disability_type": "Visual",    "income": "8-12 LPA",  "photo": get_avatar_url("Rohan Bose")},
        {"id": 13, "name": "Fatima Malik",       "age": 27, "profession": "Lawyer",            "location": "Delhi",       "education": "LLB",         "religion": "Muslim",    "image": "👩‍💼", "verified": True,  "about": "I have a speech impairment that took years to accept. Today I argue cases in court. I want someone who hears my heart, not just my words.", "disability": "Speech Impairment","disability_type": "Physical",  "income": "12-15 LPA", "photo": get_avatar_url("Fatima Malik")},
        {"id": 14, "name": "Vikram Joshi",       "age": 33, "profession": "Architect",         "location": "Pune",        "education": "B.Arch",      "religion": "Hindu",     "image": "👨‍💻", "verified": True,  "about": "Wheelchair user and architect — I design spaces that are accessible for everyone. I believe in beauty, in inclusion, and in love.",   "disability": "Wheelchair User",   "disability_type": "Physical",  "income": "18-22 LPA", "photo": get_avatar_url("Vikram Joshi")},
        {"id": 15, "name": "Amrita Singh",       "age": 29, "profession": "Music Teacher",     "location": "Chandigarh",  "education": "B.Mus.",      "religion": "Sikh",      "image": "👩‍🏫", "verified": True,  "about": "Hearing impaired but music is my soul. I teach 40 children every day how to feel rhythm. Looking for harmony in love too.",            "disability": "Hearing Impaired",  "disability_type": "Hearing",   "income": "5-6 LPA",   "photo": get_avatar_url("Amrita Singh")},
        {"id": 16, "name": "Dev Pillai",         "age": 26, "profession": "Data Scientist",    "location": "Bangalore",   "education": "M.Tech",      "religion": "Hindu",     "image": "👨‍💻", "verified": True,  "about": "I have dyslexia and ADHD — two things that make me think differently and solve problems nobody else can. Also, I make great chai.",    "disability": "Dyslexia / ADHD",   "disability_type": "Other",     "income": "14-16 LPA", "photo": get_avatar_url("Dev Pillai")},
        {"id": 17, "name": "Nisha Gupta",        "age": 30, "profession": "NGO Founder",       "location": "Lucknow",     "education": "MBA",         "religion": "Hindu",     "image": "👩‍💼", "verified": False, "about": "I run an NGO for specially-abled children. I use a prosthetic leg and walk miles every day for my cause. Passionate, stubborn, loving.", "disability": "Amputee",          "disability_type": "Physical",  "income": "6-8 LPA",   "photo": get_avatar_url("Nisha Gupta")},
        {"id": 18, "name": "Imran Qureshi",      "age": 34, "profession": "Chef",              "location": "Mumbai",      "education": "Hotel Mgmt.", "religion": "Muslim",    "image": "👨‍🍳", "verified": True,  "about": "Born deaf, trained at a 5-star hotel, now head chef at my own restaurant. Food is my love language — literally.",                      "disability": "Deaf",              "disability_type": "Hearing",   "income": "20-25 LPA", "photo": get_avatar_url("Imran Qureshi")},
        {"id": 19, "name": "Lakshmi Prasad",     "age": 23, "profession": "Student",           "location": "Chennai",     "education": "B.Tech",      "religion": "Hindu",     "image": "👩‍💻", "verified": False, "about": "Final year engineering student with a visual impairment. Top of my class. Dreams of building tech that helps people like me navigate life.", "disability": "Visually Impaired","disability_type": "Visual",    "income": "Below 5 LPA","photo": get_avatar_url("Lakshmi Prasad")},
        {"id": 20, "name": "Gurpreet Sandhu",    "age": 35, "profession": "Banker",            "location": "Chandigarh",  "education": "MBA",         "religion": "Sikh",      "image": "👨‍💼", "verified": True,  "about": "Survived a stroke at 30. Lost some speech, gained a completely new perspective on life. Now I live every day like it matters — it does.", "disability": "Post-Stroke",      "disability_type": "Physical",  "income": "25-30 LPA", "photo": get_avatar_url("Gurpreet Sandhu")},
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

    # ── HERO ─────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="
        background: linear-gradient(160deg, #1a0010 0%, #3d0020 40%, #c2185b 100%);
        padding: 80px 40px 60px;
        text-align: center;
        border-radius: 0 0 40px 40px;
        margin-bottom: 8px;
    ">
        <p style="color:#c9a84c; font-size:0.82rem; letter-spacing:3px; text-transform:uppercase;
                  font-style:italic; margin-bottom:18px;">
            India's Most Inclusive Matrimony Platform
        </p>
        <h1 style="font-family:'Playfair Display',serif; font-size:4.2rem; font-weight:700;
                   color:white; line-height:1.15; margin-bottom:20px; letter-spacing:-1px;">
            Every Heart Deserves<br>to be
            <span style="color:#c9a84c; font-style:italic;">Found.</span>
        </h1>
        <p style="font-size:1.08rem; color:rgba(255,255,255,0.65); max-width:520px;
                  margin:0 auto 40px; line-height:1.75; font-weight:300;">
            We built ShaadiZone because love doesn't ask if you can walk, see, or hear.
            It only asks if you're ready — and you are.
        </p>
        <div style="display:flex; justify-content:center; gap:40px; flex-wrap:wrap;
                    border-top:1px solid rgba(255,255,255,0.1); padding-top:32px; margin-top:8px;">
            <div style="text-align:center;">
                <div style="font-family:'Playfair Display',serif; font-size:2rem; font-weight:700; color:#c9a84c;">10,000+</div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.45); text-transform:uppercase; letter-spacing:1.5px; margin-top:3px;">Members</div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'Playfair Display',serif; font-size:2rem; font-weight:700; color:#c9a84c;">500+</div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.45); text-transform:uppercase; letter-spacing:1.5px; margin-top:3px;">Unions</div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'Playfair Display',serif; font-size:2rem; font-weight:700; color:#c9a84c;">200+</div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.45); text-transform:uppercase; letter-spacing:1.5px; margin-top:3px;">Weddings</div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'Playfair Display',serif; font-size:2rem; font-weight:700; color:#c9a84c;">100%</div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.45); text-transform:uppercase; letter-spacing:1.5px; margin-top:3px;">Free to Join</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    cta_c1, cta_c2, cta_c3, cta_c4, cta_c5 = st.columns([2, 1, 0.3, 1, 2])
    with cta_c2:
        if st.button("✦ Begin Your Journey", type="primary", use_container_width=True, key="hero_join"):
            nav_to("create")
    with cta_c4:
        if st.button("Browse Members", use_container_width=True, key="hero_browse"):
            nav_to("profiles")

    # ── BELIEF STRIP ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:linear-gradient(135deg,#2d0018,#4a0028);
                padding:72px 40px; text-align:center; margin:0;">
        <p style="font-family:'Playfair Display',serif; font-size:2.2rem; font-style:italic;
                  color:white; line-height:1.5; max-width:800px; margin:0 auto 18px;">
            "Love is not something you <span style="color:#c9a84c;">earn</span>
            through ability — it is something you <span style="color:#c9a84c;">deserve</span>
            through simply being."
        </p>
        <p style="color:rgba(255,255,255,0.38); font-size:0.82rem; letter-spacing:2.5px;
                  text-transform:uppercase;">— The ShaadiZone Belief</p>
    </div>
    """, unsafe_allow_html=True)

    # ── OUR PROMISE ──────────────────────────────────────────────────────────
    # ── GOLD DIVIDER ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style="display:flex; align-items:center; gap:16px; margin:52px auto; max-width:320px;">
        <div style="flex:1; height:1px; background:linear-gradient(90deg,transparent,#c9a84c,transparent);"></div>
        <span style="color:#c9a84c; font-size:1rem;">✦</span>
        <div style="flex:1; height:1px; background:linear-gradient(90deg,transparent,#c9a84c,transparent);"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── OUR PROMISE ──────────────────────────────────────────────────────────
    st.markdown("""
    <h2 style="font-family:'Playfair Display',serif; font-size:2.4rem; text-align:center;
               color:#c2185b; margin-bottom:6px;">Our Promise to You</h2>
    <p style="text-align:center; color:#aaa; font-size:0.95rem; margin-bottom:40px;">
        Three commitments we make to every member
    </p>
    """, unsafe_allow_html=True)

    pc = st.columns(3)
    promises = [
        ("🛡️", "You Are Safe Here",
         "Every profile is manually verified. Every interaction is monitored. This is a space built on trust — because you deserve nothing less."),
        ("💛", "You Are Seen Here",
         "We don't reduce you to your disability. Your dreams, your career, your laughter — your whole self is celebrated and honoured here."),
        ("🔒", "You Are Never Alone",
         "Our team is available 24/7. From profile help to emotional support — we walk this journey beside you, every single step."),
    ]
    for i, (icon, title, desc) in enumerate(promises):
        with pc[i]:
            st.markdown(f"""
            <div style="background:white; border-radius:24px; padding:36px 24px; text-align:center;
                        box-shadow:0 8px 32px rgba(194,24,91,0.09);
                        border-top:3px solid #c9a84c; height:100%;
                        transition:transform 0.3s ease;">
                <div style="width:68px; height:68px; border-radius:50%;
                            background:linear-gradient(135deg,#fff0f3,#fde8ee);
                            border:2px solid rgba(201,168,76,0.3);
                            display:flex; align-items:center; justify-content:center;
                            font-size:1.7rem; margin:0 auto 18px;">
                    {icon}
                </div>
                <h3 style="font-family:'Playfair Display',serif; color:#c2185b;
                           font-size:1.15rem; margin-bottom:10px;">{title}</h3>
                <p style="color:#777; font-size:0.87rem; line-height:1.75; margin:0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    # ── HOW IT WORKS ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:linear-gradient(160deg,#1a0010 0%,#2d0018 100%);
                padding:64px 40px 48px; margin:52px 0 0; border-radius:28px;">
        <p style="text-align:center; color:#c9a84c; font-size:0.78rem; letter-spacing:3px;
                  text-transform:uppercase; margin-bottom:10px;">Simple · Warm · Meaningful</p>
        <h2 style="font-family:'Playfair Display',serif; font-size:2.3rem; text-align:center;
                   color:white; margin-bottom:6px;">How ShaadiZone Works</h2>
        <p style="text-align:center; color:rgba(255,255,255,0.4); font-size:0.88rem;
                  text-transform:uppercase; letter-spacing:2px; margin-bottom:40px;">
            Three gentle steps to finding your person
        </p>
    </div>
    """, unsafe_allow_html=True)

    sc = st.columns(3)
    steps = [
        ("01", "🌸", "Create Your Profile",
         "Share your story in your own words. No labels, no boxes — just you, as you truly are. Takes 5 minutes."),
        ("02", "💝", "Discover Your Matches",
         "Our algorithm finds people who complement your world. Browse at your own pace, without pressure."),
        ("03", "💍", "Begin Your Story",
         "Send interest, connect, and let love unfold naturally. We're with you at every beautiful step."),
    ]
    for i, (num, icon, title, desc) in enumerate(steps):
        with sc[i]:
            st.markdown(f"""
            <div style="background:linear-gradient(160deg,#1a0010 0%,#3d0020 100%);
                        border:1px solid rgba(201,168,76,0.25);
                        border-radius:20px; padding:36px 24px; text-align:center;">
                <div style="font-family:'Playfair Display',serif; font-size:3.8rem; font-weight:700;
                            color:rgba(201,168,76,0.35); line-height:1; margin-bottom:6px;">{num}</div>
                <div style="font-size:2.2rem; margin-bottom:16px;">{icon}</div>
                <p style="font-family:'Playfair Display',serif; color:#ffffff; font-size:1.1rem;
                          font-weight:600; margin-bottom:10px;">{title}</p>
                <p style="color:rgba(255,255,255,0.7); font-size:0.87rem; line-height:1.75; margin:0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    # ── LOVE STORIES ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style="display:flex; align-items:center; gap:16px; margin:60px auto 0; max-width:320px;">
        <div style="flex:1; height:1px; background:linear-gradient(90deg,transparent,#c9a84c,transparent);"></div>
        <span style="color:#c9a84c; font-size:1rem;">💖</span>
        <div style="flex:1; height:1px; background:linear-gradient(90deg,transparent,#c9a84c,transparent);"></div>
    </div>
    <h2 style="font-family:'Playfair Display',serif; font-size:2.4rem; text-align:center;
               color:#c2185b; margin:20px 0 6px;">Real Love Stories</h2>
    <p style="text-align:center; color:#aaa; font-size:0.95rem; margin-bottom:36px;">
        They were brave enough to hope — and love found them
    </p>
    """, unsafe_allow_html=True)

    tc = st.columns(3)
    stories = [
        (
            "I spent years believing no one could love me the way I am — in a wheelchair, dependent for so many things. ShaadiZone didn't just find me a partner. It gave me back my belief that I deserved to be loved.",
            "Ananya S.", "Mumbai", "👩‍💻", "Married · March 2025"
        ),
        (
            "I'm blind. I've heard a thousand times that I should be 'realistic' about love. My husband — whom I found here — says my blindness is the least interesting thing about me. That is everything.",
            "Raj V.", "Delhi", "👨‍⚕️", "Married · August 2024"
        ),
        (
            "Being deaf in a world that speaks can feel lonely beyond words. When Aditya sent me his first message here, he learned sign language first. ShaadiZone didn't just match us — it matched our souls.",
            "Diya P.", "Ahmedabad", "👩‍🏫", "Engaged · January 2026"
        ),
    ]
    for i, (quote, name, city, avatar, status) in enumerate(stories):
        with tc[i]:
            st.markdown(f"""
            <div style="background:white; border-radius:24px; padding:36px 28px 28px;
                        box-shadow:0 12px 40px rgba(194,24,91,0.09);
                        border:1px solid rgba(201,168,76,0.12); position:relative; height:100%;">
                <div style="font-family:'Playfair Display',serif; font-size:5rem; color:#f8bbd0;
                            position:absolute; top:-8px; left:20px; line-height:1; opacity:0.6;">&#8220;</div>
                <p style="color:#444; font-style:italic; line-height:1.85; font-size:0.97rem;
                          margin-top:24px; margin-bottom:22px;">{quote}</p>
                <div style="display:flex; align-items:center; gap:12px;
                            padding-top:16px; border-top:1px solid #f8eef2;">
                    <div style="background:linear-gradient(135deg,#e91e63,#c2185b); border-radius:50%;
                                width:44px; height:44px; display:flex; align-items:center;
                                justify-content:center; font-size:1.4rem; flex-shrink:0;">{avatar}</div>
                    <div>
                        <div style="font-weight:600; color:#c2185b; font-size:0.92rem;">{name}</div>
                        <div style="color:#bbb; font-size:0.78rem; margin-top:1px;">{city} · {status}</div>
                    </div>
                    <div style="margin-left:auto; color:#f8bbd0; letter-spacing:3px;">♥ ♥ ♥</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── FINAL CTA ─────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:linear-gradient(135deg,#3d0020 0%,#6b0030 40%,#c2185b 100%);
                padding:80px 40px; text-align:center; border-radius:28px; margin:52px 0 0;">
        <p style="color:#c9a84c; font-size:0.78rem; letter-spacing:3px;
                  text-transform:uppercase; margin-bottom:16px;">Your Story is Waiting</p>
        <h2 style="font-family:'Playfair Display',serif; font-size:3.2rem; font-weight:700;
                   color:white; line-height:1.2; margin-bottom:16px;">
            The One Who Understands You<br>is Already Here.
        </h2>
        <p style="color:rgba(255,255,255,0.6); font-size:1rem; max-width:460px;
                  margin:0 auto; line-height:1.75;">
            Thousands of specially-abled souls — just like you —
            are hoping, dreaming, and waiting. Take the first step.
        </p>
    </div>
    """, unsafe_allow_html=True)

    final_col = st.columns([3, 2, 3])
    with final_col[1]:
        st.markdown("<div style='margin-top:20px;'>", unsafe_allow_html=True)
        if st.button("💖 Create My Free Profile", type="primary", use_container_width=True, key="final_cta"):
            nav_to("create")
        st.markdown("</div>", unsafe_allow_html=True)

    # ── FOOTER ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:#0d0008; padding:56px 40px 32px; text-align:center; margin-top:0;">
        <div style="font-family:'Playfair Display',serif; font-size:2rem;
                    font-weight:700; color:#c9a84c; margin-bottom:6px;">ShaadiZone</div>
        <div style="color:rgba(255,255,255,0.35); font-size:0.78rem; letter-spacing:2.5px;
                    text-transform:uppercase; margin-bottom:28px;">
            Inclusive Matrimony · Built with Love
        </div>
        <div style="height:1px; background:linear-gradient(90deg,transparent,rgba(201,168,76,0.35),transparent);
                    max-width:380px; margin:0 auto 24px;"></div>
        <div style="color:rgba(255,255,255,0.18); font-size:0.76rem; letter-spacing:1px;">
            © 2026 ShaadiZone · Founded by Animesh · Every heart matters.
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
        st.markdown(f"<div style='text-align:center; margin-bottom:28px;'><span style='background:linear-gradient(135deg,#fff0f3,#ffe4e9); border:1.5px solid #f8bbd0; color:#c2185b; padding:6px 20px; border-radius:20px; font-size:0.88rem; font-weight:500;'>💖 {len(profiles)} beautiful soul{'s' if len(profiles) != 1 else ''} found</span></div>", unsafe_allow_html=True)

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
            photo = profile.get('photo', get_avatar_url(profile['name']))
            about_snippet = profile.get('about','')[:72] + '…' if len(profile.get('about','')) > 72 else profile.get('about','')
            st.markdown(f"""
            <div style="background:white; border-radius:22px; overflow:hidden; margin-bottom:8px;
                        box-shadow:0 8px 28px rgba(233,30,99,0.09);
                        border:1.5px solid rgba(233,30,99,0.08);">
                <div style="background:linear-gradient(135deg,#e91e63 0%,#c2185b 60%,#ad1457 100%);
                            padding:28px; text-align:center; position:relative;">
                    {verified_html}
                    <img src="{photo}" style="width:88px; height:88px; border-radius:50%;
                         object-fit:cover; border:3px solid rgba(255,255,255,0.55);
                         box-shadow:0 4px 18px rgba(0,0,0,0.22); display:block; margin:0 auto;"
                         alt="{profile['name']}" />
                </div>
                <div style="padding:20px 22px 18px;">
                    <div style="color:#c2185b; font-family:'Playfair Display',serif;
                                font-size:1.25rem; font-weight:600; margin-bottom:3px;">{profile['name']}</div>
                    <div style="color:#777; font-size:0.88rem; margin-bottom:3px;">
                        {profile['age']} yrs &nbsp;·&nbsp; {profile['location']}
                    </div>
                    <div style="color:#555; font-size:0.83rem; margin-bottom:10px;">
                        {profile['profession']} &nbsp;·&nbsp; {profile['education']}
                    </div>
                    <p style="color:#888; font-size:0.82rem; font-style:italic;
                              line-height:1.55; margin-bottom:12px;">{about_snippet}</p>
                    <span style="background:linear-gradient(135deg,#fff0f3,#ffe4e9);
                                 border:1.5px solid #f8bbd0; color:#c2185b; padding:4px 12px;
                                 border-radius:14px; font-size:0.76rem; font-weight:500;">
                        ♿ {profile.get('disability','N/A')}
                    </span>
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

    photo = profile.get('photo', get_avatar_url(profile['name']))
    st.markdown(f"""
    <div class="detail-header">
        <div style="display:flex; align-items:center; gap:36px; flex-wrap:wrap;">
            <div>
                <img src="{photo}" class="detail-photo" alt="{profile['name']}" />
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

        st.markdown("#### 📸 Profile Photo")
        photo_col1, photo_col2 = st.columns([1, 2])
        with photo_col1:
            uploaded_photo = st.file_uploader(
                "Upload your photo",
                type=["jpg", "jpeg", "png", "webp"],
                help="Square photos work best. Max 5 MB.",
                label_visibility="collapsed",
            )
        with photo_col2:
            st.markdown("""
            <div style="color:#999; font-size:0.85rem; line-height:1.7; padding-top:8px;">
                Upload a clear, recent photo of yourself.<br>
                JPG, PNG or WebP · Recommended: square crop.<br>
                <span style="color:#f8bbd0;">If you skip this, a beautiful illustrated avatar will be generated for you.</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
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
            image      = "💖"  # kept for legacy compatibility

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
                import base64
                if uploaded_photo:
                    raw = uploaded_photo.read()
                    b64 = base64.b64encode(raw).decode()
                    photo_url = f"data:{uploaded_photo.type};base64,{b64}"
                else:
                    photo_url = get_avatar_url(name)
                new_profile = {
                    "id": len(st.session_state.profiles) + 1,
                    "name": name, "age": age, "profession": profession,
                    "location": location, "education": education, "religion": religion,
                    "image": image, "verified": False, "about": about,
                    "disability": disability_detail if disability_detail else disability_type,
                    "disability_type": disability_type, "income": income,
                    "photo": photo_url,
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

        m_photo = profile.get('photo', get_avatar_url(profile['name']))
        st.markdown(f"""
        <div class="match-card">
            <div class="match-rank">#{rank}</div>
            <div class="match-avatar" style="background:none; border-radius:16px; overflow:hidden; padding:0;">
                <img src="{m_photo}" class="match-photo" alt="{profile['name']}" />
            </div>
            <div class="match-info">
                <div class="match-name">{profile['name']}
                    &nbsp;{verified_badge}
                </div>
                <div class="match-meta">
                    {profile['age']} yrs &nbsp;·&nbsp; {profile['location']} &nbsp;·&nbsp;
                    {profile['profession']} &nbsp;·&nbsp; {profile['education']}
                </div>
                <span style="background:linear-gradient(135deg,#fff0f3,#ffe4e9); border:1.5px solid #f8bbd0;
                             color:#c2185b; padding:4px 10px; border-radius:14px;
                             font-size:0.76rem; font-weight:500;">♿ {profile.get('disability','N/A')}</span>
                <span style="display:inline-block; padding:3px 10px; border-radius:12px; font-size:0.72rem;
                             font-weight:600; margin-left:6px;
                             background:{'#e8f5e9' if score>=80 else '#fff8e1' if score>=60 else '#fce4ec'};
                             color:{'#2e7d32' if score>=80 else '#f57f17' if score>=60 else '#c2185b'};">
                    {tag_emoji} {tag_text}</span>
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
