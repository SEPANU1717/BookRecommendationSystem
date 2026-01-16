import streamlit as st
import os
import datetime
import random
import string
from PIL import Image

# Page configuration
try:
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "image/mm.png")
    im = Image.open(image_path)
    st.set_page_config(page_title="Bastoned | Contact", page_icon=im, layout="wide")
except Exception:
    st.set_page_config(page_title="Bastoned | Contact", layout="wide")

# Load external CSS
css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "style/main.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render Sidebar
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.sidebar import render_sidebar
render_sidebar()

st.markdown("""
    <div style='margin-bottom: 2rem;'>
        <h2 style='font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700; margin-bottom: 0.5rem;'>
            <i class="fas fa-ticket-alt" style="margin-right: 0.75rem; color: #6366f1;"></i>Submit a Ticket
        </h2>
        <p style='color: #94a3b8; font-size: 1rem;'>Professional protocol for technical inquiries and system feedback.</p>
    </div>
""", unsafe_allow_html=True)

# Initialize session state for form submission
if 'ticket_submitted' not in st.session_state:
    st.session_state.ticket_submitted = False
if 'ticket_data' not in st.session_state:
    st.session_state.ticket_data = None

col1, col2 = st.columns([2, 1])

with col1:
    if not st.session_state.ticket_submitted:
        # Ticket Form Header
        st.markdown("""
            <div class="ticket-form">
                <div class="ticket-header">
                    <div class="ticket-icon"><i class="fas fa-file-alt"></i></div>
                    <div>
                        <h3 style="margin: 0; font-family: 'Plus Jakarta Sans', sans-serif;">New Support Ticket</h3>
                        <p style="margin: 0; color: var(--text-dim); font-size: 0.85rem;">All fields are required for processing</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("ticket_form", clear_on_submit=False):
            # Subject Category Dropdown
            st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.25rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>SUBJECT CATEGORY</p>", unsafe_allow_html=True)
            subject_category = st.selectbox(
                "Subject Category",
                ["Select a category...", "Bug Report", "Resource Addition Request", "System Partnership", "Feature Request", "Technical Support", "General Inquiry"],
                label_visibility="collapsed"
            )
            
            st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
            
            # Name Field
            st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.25rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>FULL NAME</p>", unsafe_allow_html=True)
            name = st.text_input("Full Name", placeholder="Enter your professional name...", label_visibility="collapsed")
            
            st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
            
            # Email Field
            st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.25rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>CONTACT EMAIL</p>", unsafe_allow_html=True)
            email = st.text_input("Email", placeholder="Enter your email address...", label_visibility="collapsed")
            
            st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
            
            # Priority Level
            st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.25rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>PRIORITY LEVEL</p>", unsafe_allow_html=True)
            priority = st.select_slider(
                "Priority",
                options=["Low", "Normal", "High", "Critical"],
                value="Normal",
                label_visibility="collapsed"
            )
            
            st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
            
            # Message Field
            st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.25rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>TICKET DETAILS</p>", unsafe_allow_html=True)
            message = st.text_area("Message", placeholder="Provide detailed information about your inquiry...", height=150, label_visibility="collapsed")
            
            st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
            
            submit_btn = st.form_submit_button("Submit Ticket", use_container_width=True)
            
            if submit_btn:
                if subject_category == "Select a category..." or not name or not email or not message:
                    st.warning("All fields are mandatory for ticket submission.")
                else:
                    # Generate ticket ID
                    ticket_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                    st.session_state.ticket_submitted = True
                    st.session_state.ticket_data = {
                        "id": ticket_id,
                        "name": name,
                        "email": email,
                        "category": subject_category,
                        "priority": priority,
                        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
                    }
                    st.rerun()
    
    else:
        # Transmission Success Animation
        ticket = st.session_state.ticket_data
        st.markdown(f"""
            <div class="transmission-success">
                <div class="transmission-icon">
                    <i class="fas fa-check"></i>
                </div>
                <div class="transmission-title">Transmission Successful</div>
                <p style="color: var(--text-secondary); margin-bottom: 0;">Your ticket has been logged and queued for review.</p>
                
                <div class="transmission-receipt">
                    <div style="text-align: center; margin-bottom: 0.75rem; color: var(--primary-light); font-weight: 600;">
                        ━━━ TRANSMISSION RECEIPT ━━━
                    </div>
                    <div class="transmission-receipt-row">
                        <span>TICKET ID:</span>
                        <span style="color: var(--primary-light);">#{ticket['id']}</span>
                    </div>
                    <div class="transmission-receipt-row">
                        <span>OPERATOR:</span>
                        <span>{ticket['name']}</span>
                    </div>
                    <div class="transmission-receipt-row">
                        <span>CATEGORY:</span>
                        <span>{ticket['category']}</span>
                    </div>
                    <div class="transmission-receipt-row">
                        <span>PRIORITY:</span>
                        <span style="color: {'#ef4444' if ticket['priority'] == 'Critical' else '#f59e0b' if ticket['priority'] == 'High' else '#10b981'};">{ticket['priority']}</span>
                    </div>
                    <div class="transmission-receipt-row">
                        <span>TIMESTAMP:</span>
                        <span>{ticket['timestamp']}</span>
                    </div>
                    <div style="text-align: center; margin-top: 0.75rem; color: var(--text-dim);">
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        if st.button("Submit Another Ticket", use_container_width=True):
            st.session_state.ticket_submitted = False
            st.session_state.ticket_data = None
            st.rerun()

with col2:
    st.markdown("""
        <div class="book-card">
            <div class="icon-container"><i class="fas fa-headset"></i></div>
            <h4 style="font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 1rem;">Support Infrastructure</h4>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <i class="fas fa-at" style="color: var(--primary); width: 20px;"></i>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">sys@bastoned.pro</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <i class="fas fa-university" style="color: var(--primary); width: 20px;"></i>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">STI College Balayan</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <i class="fas fa-globe" style="color: var(--primary); width: 20px;"></i>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">bastoned.pro/network</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    
    # Response Time Expectations
    st.markdown("""
        <div class="book-card">
            <h4 style="font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 1rem;">
                <i class="fas fa-clock" style="color: var(--primary); margin-right: 0.5rem;"></i>Response Times
            </h4>
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="tech-level tech-level-advanced" style="font-size: 0.65rem;">Critical</span>
                    <span style="color: var(--text-secondary); font-size: 0.85rem;">< 4 hours</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="tech-level tech-level-intermediate" style="font-size: 0.65rem;">High</span>
                    <span style="color: var(--text-secondary); font-size: 0.85rem;">< 24 hours</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="tech-level tech-level-beginner" style="font-size: 0.65rem;">Normal</span>
                    <span style="color: var(--text-secondary); font-size: 0.85rem;">1-3 days</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
