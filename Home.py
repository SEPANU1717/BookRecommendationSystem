import streamlit as st
import os
import base64
import time
from PIL import Image

# Page configuration
try:
    image_path = os.path.join(os.path.dirname(__file__), "image/mm.png")
    im = Image.open(image_path)
    st.set_page_config(page_title="Bastoned | Technical Intelligence", page_icon=im, layout="wide")
except Exception:
    st.set_page_config(page_title="Bastoned | Technical Intelligence", layout="wide")

# Load external CSS
with open(os.path.join(os.path.dirname(__file__), "style/main.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render Sidebar
from utils.sidebar import render_sidebar
render_sidebar()

# Hero Section
st.markdown("""
    <div class="hero-wrapper">
        <h1 class="hero-title">Elevate Your Coding Expertise</h1>
        <p class="hero-subtitle">
            Leverage our advanced recommendation engine to discover technical literature 
            specifically tailored to your professional development goals.
        </p>
    </div>
""", unsafe_allow_html=True)

# Live System Stats Dashboard
st.markdown("""
    <div class="stats-dashboard">
        <div class="stat-card">
            <div class="stat-value">20,412</div>
            <div class="stat-label">Books Indexed</div>
            <div class="stat-indicator">
                <div class="stat-dot-live"></div>
                <span style="font-size: 0.7rem; color: #10b981;">Live</span>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-value">0.12s</div>
            <div class="stat-label">Retrieval Latency</div>
            <div class="stat-indicator">
                <i class="fas fa-bolt" style="color: #f59e0b; font-size: 0.7rem;"></i>
                <span style="font-size: 0.7rem; color: #f59e0b;">Fast</span>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-value">V1.2.0</div>
            <div class="stat-label">Engine Version</div>
            <div class="stat-indicator">
                <i class="fas fa-check-circle" style="color: #10b981; font-size: 0.7rem;"></i>
                <span style="font-size: 0.7rem; color: #10b981;">Active</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top: 4rem;'></div>", unsafe_allow_html=True)

# Skeleton Loading Placeholder (shown briefly on initial load)
placeholder = st.empty()

# Simulate skeleton loading effect for feature cards
if 'cards_loaded' not in st.session_state:
    with placeholder.container():
        f1, f2, f3 = st.columns(3)
        for col in [f1, f2, f3]:
            with col:
                st.markdown("""
                    <div class="book-card">
                        <div class="skeleton skeleton-title"></div>
                        <div class="skeleton skeleton-text"></div>
                        <div class="skeleton skeleton-text"></div>
                        <div class="skeleton skeleton-text-short"></div>
                    </div>
                """, unsafe_allow_html=True)
    time.sleep(0.3)
    st.session_state.cards_loaded = True
    placeholder.empty()

# Features Grid
f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
        <div class="book-card">
            <div class="icon-container"><i class="fas fa-brain"></i></div>
            <div class="book-title">Smart Retrieval</div>
            <p style="color: #94a3b8; font-size: 0.95rem;">Our semantic analysis engine identifies high-correlation titles based on technical depth and subject matter.</p>
        </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
        <div class="book-card">
            <div class="icon-container"><i class="fas fa-layer-group"></i></div>
            <div class="book-title">Curated Library</div>
            <p style="color: #94a3b8; font-size: 0.95rem;">Access a strictly curated database of over 20,000 professional programming titles and resources.</p>
        </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
        <div class="book-card">
            <div class="icon-container"><i class="fas fa-bolt"></i></div>
            <div class="book-title">Real-time Insights</div>
            <p style="color: #94a3b8; font-size: 0.95rem;">Receive instantaneous suggestions with detailed technical summaries and direct acquisition paths.</p>
        </div>
    """, unsafe_allow_html=True)