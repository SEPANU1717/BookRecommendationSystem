import streamlit as st
import pandas as pd
import os
import random
from PIL import Image

# Page configuration
try:
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "image/mm.png")
    im = Image.open(image_path)
    st.set_page_config(page_title="Bastoned | Library", page_icon=im, layout="wide")
except Exception:
    st.set_page_config(page_title="Bastoned | Library", layout="wide")

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
    <div style='margin-bottom: 1.5rem;'>
        <h2 style='font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700; margin-bottom: 0.5rem;'>
            <i class="fas fa-layer-group" style="margin-right: 0.75rem; color: #6366f1;"></i>Resource Catalog
        </h2>
        <p style='color: #94a3b8; font-size: 1rem;'>Explore specialized collections across various programming domains.</p>
    </div>
""", unsafe_allow_html=True)

"""
Control bar (Domain selector, Difficulty filter, View toggle) moved below after CSVs are loaded to avoid referencing `data_dict` before it's defined.
"""

def load_data(folder_path):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    data_dict = {}
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        data_dict[file[:-4]] = pd.read_csv(file_path)
    return data_dict

# Load CSV files and create select box
base_path = os.path.dirname(os.path.dirname(__file__))
data_dict = load_data(os.path.join(base_path, 'csvfiles'))

# Use session state to track catalog selection and page
if 'selected_catalog' not in st.session_state:
    st.session_state.selected_catalog = None
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "Grid View"
if 'difficulty_filter' not in st.session_state:
    st.session_state.difficulty_filter = "All Levels"

# Control Bar with Domain Selector, View Mode, and Filters (placed after data_dict is available)
col1, col2, col3 = st.columns([3, 1.5, 1])

with col1:
    st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>Programming Domain</p>", unsafe_allow_html=True)
    file_name = st.selectbox(
        'Domain Selection',
        list(data_dict.keys()), 
        label_visibility="collapsed", 
        index=None if not st.session_state.selected_catalog else list(data_dict.keys()).index(st.session_state.selected_catalog) if st.session_state.selected_catalog in data_dict else None,
        placeholder="Select programming domain...",
        key="domain_select_main"
    )
    if file_name and file_name != st.session_state.selected_catalog:
        st.session_state.selected_catalog = file_name
        st.session_state.current_page = 1
        st.rerun()

with col2:
    st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>Difficulty Level</p>", unsafe_allow_html=True)
    difficulty_filter = st.selectbox(
        'Difficulty Filter',
        ["All Levels", "Beginner", "Intermediate", "Advanced"],
        label_visibility="collapsed",
        index=["All Levels", "Beginner", "Intermediate", "Advanced"].index(st.session_state.difficulty_filter),
        key="difficulty_filter_main"
    )
    st.session_state.difficulty_filter = difficulty_filter

with col3:
    st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>View Mode</p>", unsafe_allow_html=True)
    col3_1, col3_2 = st.columns(2)
    with col3_1:
        if st.button("Grid", key="grid_view_btn", help="Switch to grid view", use_container_width=True, type="primary" if st.session_state.view_mode == "Grid View" else "secondary"):
            st.session_state.view_mode = "Grid View"
            st.rerun()
    with col3_2:
        if st.button("List", key="list_view_btn", help="Switch to list view", use_container_width=True, type="primary" if st.session_state.view_mode == "List View" else "secondary"):
            st.session_state.view_mode = "List View"
            st.rerun()

st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)

if st.session_state.selected_catalog is None:
    st.info("Please select a programming domain from the sidebar to view the resource catalog.")
else:
    df = data_dict[st.session_state.selected_catalog]
    
    # Add technical difficulty to each item (simulated based on description)
    def assign_difficulty(row):
        desc = str(row.get('description', row.get('Description', ''))).lower()
        title = str(row.get('title', '')).lower()
        combined = desc + ' ' + title
        if any(word in combined for word in ['advanced', 'expert', 'mastering', 'deep dive', 'architecture', 'performance']):
            return 'Advanced'
        elif any(word in combined for word in ['intermediate', 'practical', 'effective', 'professional', 'complete guide']):
            return 'Intermediate'
        else:
            return 'Beginner'
    
    df['difficulty'] = df.apply(assign_difficulty, axis=1)
    
    # Apply difficulty filter
    if st.session_state.difficulty_filter != "All Levels":
        df = df[df['difficulty'] == st.session_state.difficulty_filter]
    
    items_per_page = 9
    total_items = len(df)
    total_pages = max((total_items - 1) // items_per_page + 1, 1)
    
    # Ensure current page is valid
    if st.session_state.current_page > total_pages:
        st.session_state.current_page = 1
    
    st.markdown(f"""
        <div class="section-header">
            <h3 style='font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700;'>
                <i class="fas fa-book-open" style="margin-right: 0.75rem; color: #6366f1;"></i>Catalog: {st.session_state.selected_catalog}
            </h3>
            <p style='color: #94a3b8; margin-top: 0.5rem;'>
                Showing page {st.session_state.current_page} of {total_pages} 
                <span style="margin-left: 1rem; padding: 0.25rem 0.75rem; background: var(--primary-glow); border-radius: 100px; font-size: 0.8rem;">
                    {total_items} titles
                </span>
                {f'<span style="margin-left: 0.5rem; color: #f59e0b;"><i class="fas fa-filter"></i> {st.session_state.difficulty_filter}</span>' if st.session_state.difficulty_filter != "All Levels" else ''}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if total_items == 0:
        st.warning(f"No resources found for difficulty level: {st.session_state.difficulty_filter}. Try selecting 'All Levels'.")
    else:
        # Calculate slice
        start_idx = (st.session_state.current_page - 1) * items_per_page
        end_idx = start_idx + items_per_page
        df_page = df.iloc[start_idx:end_idx]
        
        # Display based on selected View Mode
        if st.session_state.view_mode == "Grid View":
            # Display results in structured grid with hover preview
            for i in range(0, len(df_page), 3):
                cols = st.columns(3, gap="large")
                for j in range(3):
                    if i + j < len(df_page):
                        row = df_page.iloc[i + j]
                        desc = str(row.get('description', row.get('Description', 'No summary available.')))
                        short_desc = desc[:160] + '...' if len(desc) > 160 else desc
                        difficulty = row.get('difficulty', 'Beginner')
                        level_class = f"tech-level-{difficulty.lower()}"
                        
                        with cols[j]:
                            st.markdown(f"""
                                <div class="book-card">
                                    <div class="book-title">{row['title']}</div>
                                    <div class="book-description">{short_desc}</div>
                                    <div class="difficulty-badge-container">
                                        <span class="tech-level {level_class}" style="font-size: 0.7rem;">{difficulty}</span>
                                    </div>
                                    <div class="book-footer" style="margin-top: 0.75rem;">
                                        <a href="{row['url']}" target="_blank" class="book-button">
                                            View Source <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
                                        </a>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
        else:
            # Display results in List View (Dense mode for technical users)
            st.markdown("<div style='border: 1px solid var(--border-color-subtle); border-radius: var(--radius-lg); overflow: hidden;'>", unsafe_allow_html=True)
            for idx, (_, row) in enumerate(df_page.iterrows()):
                difficulty = row.get('difficulty', 'Beginner')
                level_class = f"tech-level-{difficulty.lower()}"
                
                st.markdown(f"""
                    <div class="list-item">
                        <div style="flex: 1;">
                            <div class="list-title">{row['title']}</div>
                            <div class="list-meta" style="display: flex; align-items: center; gap: 1rem; margin-top: 0.3rem;">
                                <span>Resource ID: {hash(row['title']) % 10000}</span>
                                <span class="tech-level {level_class}" style="font-size: 0.6rem;">{difficulty}</span>
                            </div>
                        </div>
                        <a href="{row['url']}" target="_blank" class="book-button">
                            Access <i class="fas fa-external-link-alt" style="font-size: 0.7rem;"></i>
                        </a>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # Sticky Bottom Pagination Bar
        if total_pages > 1:
            st.markdown("""
                <div class="sticky-pagination">
            """, unsafe_allow_html=True)
            
            _, prev_col, page_col, next_col, _ = st.columns([2, 1, 1, 1, 2])
            
            with prev_col:
                if st.session_state.current_page > 1:
                    if st.button("← Previous", key="prev_sticky", use_container_width=True):
                        st.session_state.current_page -= 1
                        st.rerun()
            
            with page_col:
                st.markdown(f"""
                    <div style='text-align: center; padding: 0.5rem; color: var(--text-secondary); font-weight: 600;'>
                        {st.session_state.current_page} / {total_pages}
                    </div>
                """, unsafe_allow_html=True)
            
            with next_col:
                if st.session_state.current_page < total_pages:
                    if st.button("Next →", key="next_sticky", use_container_width=True):
                        st.session_state.current_page += 1
                        st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Add bottom padding to account for sticky pagination
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
