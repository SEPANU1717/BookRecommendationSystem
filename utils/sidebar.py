import streamlit as st

def render_sidebar():
    with st.sidebar:
        # Logo and Branding
        st.markdown("""
            <div class="sidebar-logo-container">
                <div class="logo-text">bastoned</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
        
        # Footer
        st.markdown("""
            <div class="sidebar-footer-static">
                <div class="footer-copyright">
                    © 2026 bastoned
                </div>
            </div>
        """, unsafe_allow_html=True)
