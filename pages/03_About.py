import streamlit as st
import os
from PIL import Image

# Page configuration
try:
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "image/mm.png")
    im = Image.open(image_path)
    st.set_page_config(page_title="Bastoned | About", page_icon=im, layout="wide")
except Exception:
    st.set_page_config(page_title="Bastoned | About", layout="wide")

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
            <i class="fas fa-info-circle" style="margin-right: 0.75rem; color: #6366f1;"></i>Technical Authority
        </h2>
        <p style='color: #94a3b8; font-size: 1rem;'>Platform intelligence, system architecture, and development team.</p>
    </div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Our Mission", "System Architecture", "Development Team"])

with tab1:
    st.markdown("""
        <div class="book-card">
            <div class="icon-container"><i class="fas fa-bullseye"></i></div>
            <h3 style='margin-bottom: 1rem; font-family: "Plus Jakarta Sans", sans-serif;'>Operational Mission</h3>
            <p style='margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;'>
                Bastoned provides a critical high-fidelity discovery layer for technical literature. 
                By implementing advanced semantic analysis, we eliminate the friction typically associated 
                with finding specialized educational resources.
            </p>
            <p style='color: var(--text-secondary); line-height: 1.7;'>
                Our platform serves as a definitive resource for both entry-level developers and 
                specialized engineers seeking authoritative technical content.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    metrics = [
        ("20,412", "Books Indexed", "fas fa-book"),
        ("30+", "Languages Covered", "fas fa-code"),
        ("0.12s", "Avg. Response", "fas fa-bolt"),
        ("99.9%", "Uptime", "fas fa-server")
    ]
    for col, (value, label, icon) in zip([m1, m2, m3, m4], metrics):
        with col:
            st.markdown(f"""
                <div class="stat-card" style="text-align: center;">
                    <i class="{icon}" style="font-size: 1.5rem; color: var(--primary); margin-bottom: 0.75rem; display: block;"></i>
                    <div class="stat-value">{value}</div>
                    <div class="stat-label">{label}</div>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
        <div style='margin-bottom: 1.5rem;'>
            <h3 style='font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700;'>
                <i class="fas fa-project-diagram" style="margin-right: 0.75rem; color: #6366f1;"></i>System Architecture
            </h3>
            <p style='color: #94a3b8;'>Visual representation of the recommendation pipeline</p>
        </div>
    """, unsafe_allow_html=True)
    
    # CSS Architecture Flow Diagram
    st.markdown("""
        <div class="architecture-flow">
            <div class="flow-node">
                <div class="flow-node-icon"><i class="fas fa-keyboard"></i></div>
                <div class="flow-node-title">User Query</div>
                <div class="flow-node-subtitle">Text Input</div>
            </div>
            <div class="flow-arrow"><i class="fas fa-arrow-right"></i></div>
            <div class="flow-node">
                <div class="flow-node-icon"><i class="fas fa-cogs"></i></div>
                <div class="flow-node-title">TF-IDF</div>
                <div class="flow-node-subtitle">Vectorizer</div>
            </div>
            <div class="flow-arrow"><i class="fas fa-arrow-right"></i></div>
            <div class="flow-node">
                <div class="flow-node-icon"><i class="fas fa-vector-square"></i></div>
                <div class="flow-node-title">Query Vector</div>
                <div class="flow-node-subtitle">Transformation</div>
            </div>
            <div class="flow-arrow"><i class="fas fa-arrow-right"></i></div>
            <div class="flow-node">
                <div class="flow-node-icon"><i class="fas fa-th"></i></div>
                <div class="flow-node-title">Similarity</div>
                <div class="flow-node-subtitle">Matrix</div>
            </div>
            <div class="flow-arrow"><i class="fas fa-arrow-right"></i></div>
            <div class="flow-node">
                <div class="flow-node-icon"><i class="fas fa-check-circle"></i></div>
                <div class="flow-node-title">Results</div>
                <div class="flow-node-subtitle">Ranked</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    
    # Accordion-style Technical Specifications
    with st.expander("Core Engine Components"):
        st.markdown("""
            <div style='padding: 0.5rem 0;'>
                <h4 style='color: var(--text-primary); margin-bottom: 1rem;'><i class="fas fa-cogs" style="color: var(--primary); margin-right: 0.5rem;"></i>TF-IDF Vectorization</h4>
                <p style='color: var(--text-secondary); line-height: 1.7;'>
                    Term Frequency-Inverse Document Frequency transforms text into numerical vectors, 
                    weighing terms by their importance across the document corpus. This enables 
                    semantic understanding beyond simple keyword matching.
                </p>
                <div style='margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;'>
                    <span class="tech-badge"><i class="fas fa-python"></i> Scikit-learn</span>
                    <span class="tech-badge"><i class="fas fa-calculator"></i> NumPy</span>
                    <span class="tech-badge"><i class="fas fa-table"></i> Pandas</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with st.expander("Similarity Computation"):
        st.markdown("""
            <div style='padding: 0.5rem 0;'>
                <h4 style='color: var(--text-primary); margin-bottom: 1rem;'><i class="fas fa-th" style="color: var(--primary); margin-right: 0.5rem;"></i>Cosine Similarity Matrix</h4>
                <p style='color: var(--text-secondary); line-height: 1.7;'>
                    Measures the cosine of the angle between two non-zero vectors, providing a metric 
                    for document similarity independent of document length. Values range from 0 (no similarity) 
                    to 1 (identical).
                </p>
                <div style='margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;'>
                    <span class="tech-badge"><i class="fas fa-brain"></i> ML Pipeline</span>
                    <span class="tech-badge"><i class="fas fa-vector-square"></i> Vector Ops</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with st.expander("Frontend Architecture"):
        st.markdown("""
            <div style='padding: 0.5rem 0;'>
                <h4 style='color: var(--text-primary); margin-bottom: 1rem;'><i class="fas fa-bolt" style="color: var(--primary); margin-right: 0.5rem;"></i>Streamlit Reactive Framework</h4>
                <p style='color: var(--text-secondary); line-height: 1.7;'>
                    High-performance reactive UI framework enabling rapid prototyping and deployment 
                    of data applications. Features automatic state management, caching, and 
                    responsive component rendering.
                </p>
                <div style='margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;'>
                    <span class="tech-badge"><i class="fas fa-desktop"></i> Streamlit</span>
                    <span class="tech-badge"><i class="fas fa-paint-brush"></i> CSS3</span>
                    <span class="tech-badge"><i class="fas fa-mobile-alt"></i> Responsive</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    
    team_members = [
        {
            "name": "Mark Christianiel Manalo", 
            "role": "Lead Architect", 
            "email": "manalo.2566146@balayan.sti.edu.ph", 
            "icon": "fa-code",
            "badges": ["Python", "ML", "System Design"]
        },
        {
            "name": "Jonah Levi Lagazo", 
            "role": "Project Director", 
            "email": "lagazo.261249@balayan.sti.edu.ph", 
            "icon": "fa-user-tie",
            "badges": ["Project Management", "Agile", "Strategy"]
        },
        {
            "name": "Geian Aboy", 
            "role": "Systems Engineer", 
            "email": "aboy.244098@balayan.sti.edu.ph", 
            "icon": "fa-server",
            "badges": ["Infrastructure", "DevOps", "Python"]
        },
        {
            "name": "Jefferson Lagan", 
            "role": "UX Experience Engineer", 
            "email": "lagan.260664@balayan.sti.edu.ph", 
            "icon": "fa-pencil-ruler",
            "badges": ["UI/UX", "CSS", "Figma"]
        },
        {
            "name": "John Andrei Monroyo", 
            "role": "Data Scientist", 
            "email": "monroyo.265776@balayan.sti.edu.ph", 
            "icon": "fa-database",
            "badges": ["Data Science", "Analytics", "Python"]
        },
    ]
    
    for member in team_members:
        with st.expander(f"{member['name']}"):
            badges_html = ''.join([f'<span class="tech-badge">{badge}</span>' for badge in member['badges']])
            st.markdown(f"""
                <div style='display: flex; align-items: flex-start; gap: 1.25rem; padding: 0.5rem 0;'>
                    <div style='width: 50px; height: 50px; background: var(--primary-glow); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center;'>
                        <i class="fas {member['icon']}" style="font-size: 1.25rem; color: var(--primary);"></i>
                    </div>
                    <div style='flex: 1;'>
                        <div style='font-weight: 700; font-size: 1rem; color: var(--text-primary);'>{member['role']}</div>
                        <div style='color: var(--text-dim); font-size: 0.85rem; margin: 0.25rem 0 0.75rem;'>{member['email']}</div>
                        <div style='display: flex; flex-wrap: wrap; gap: 0.3rem;'>
                            {badges_html}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
