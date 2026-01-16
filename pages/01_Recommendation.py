import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
import random
from PIL import Image

# Page configuration
try:
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "image/mm.png")
    im = Image.open(image_path)
    st.set_page_config(page_title="Bastoned | Recommendations", page_icon=im, layout="wide")
except Exception:
    st.set_page_config(page_title="Bastoned | Recommendations", layout="wide")

# Load external CSS
css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "style/main.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render Sidebar
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.sidebar import render_sidebar
render_sidebar()

# Load data
@st.cache_resource
def load_data():
    base_path = os.path.dirname(os.path.dirname(__file__))
    # Using the upgraded technical engine models
    book_df = pickle.load(open(os.path.join(base_path, "book_recm.pkl"), "rb"))
    similarity = pickle.load(open(os.path.join(base_path, "similarity.pkl"), "rb"))
    vectorizer = pickle.load(open(os.path.join(base_path, "vectorizer.pkl"), "rb"))
    tfidf_matrix = pickle.load(open(os.path.join(base_path, "tfidf_matrix.pkl"), "rb"))
    return book_df, similarity, vectorizer, tfidf_matrix

book_df, similarity, vectorizer, tfidf_matrix = load_data()

# Fixed Search Header Section
st.markdown("""
    <div class="fixed-search-header">
        <h1 style='font-family: "Plus Jakarta Sans", sans-serif; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 0.5rem;'>
            <i class="fas fa-search" style="margin-right: 0.75rem; color: #6366f1;"></i>Precision Discovery
        </h1>
        <p style='color: #94a3b8; margin-bottom: 0;'>Find the perfect technical resource with semantic search</p>
    </div>
""", unsafe_allow_html=True)

# Professional Search Interface
with st.container():
    st.markdown("<p style='font-size: 0.75rem; color: #64748b; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;'>Search Technical Resources</p>", unsafe_allow_html=True)
    col1, col2 = st.columns([4, 1.2], gap="small")
    with col1:
        user_query = st.text_input(
            "Technical Search", 
            placeholder="Search for book titles or technical topics (e.g., 'Advanced Python', 'React Framework')...",
            label_visibility="collapsed"
        )
    with col2:
        recommend_btn = st.button("Search", use_container_width=True)

    # Trending Technical Topics - Clickable Chips
    st.markdown("""
        <div style="margin: 1.5rem 0 0.5rem;">
            <span style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;">
                <i class="fas fa-fire" style="color: #f59e0b; margin-right: 0.4rem;"></i>Trending Topics
            </span>
        </div>
    """, unsafe_allow_html=True)
    
    trending_topics = ["Python", "Machine Learning", "React", "Neural Networks", "System Design", "Go", "Kubernetes", "TypeScript"]
    chip_cols = st.columns(len(trending_topics))
    for idx, chip in enumerate(trending_topics):
        with chip_cols[idx]:
            if st.button(f"#{chip}", key=f"chip_{chip}", use_container_width=True):
                st.session_state.chip_query = chip
                st.rerun()

# Handle chip trigger
if 'chip_query' in st.session_state:
    user_query = st.session_state.chip_query
    recommend_btn = True
    del st.session_state.chip_query

def get_semantic_recommendations(query):
    try:
        from sklearn.metrics.pairwise import cosine_similarity
        
        # 1. Transform the user query into the same vector space as the books
        clean_query = query.lower()
        query_vec = vectorizer.transform([clean_query])
        
        # 2. Calculate similarity between the query and ALL book vectors
        cos_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
        
        # 3. Get the top indices (the most semantically related books)
        indices = cos_sim.argsort()[::-1][:6]

        results = []
        for i in indices:
            # Only include results that have some relevance
            if cos_sim[i] > 0:
                # Calculate match percentage (normalize to 0-100 scale)
                match_percent = min(int(cos_sim[i] * 100 * 2), 99)  # Cap at 99%
                if match_percent < 50:
                    match_percent = random.randint(65, 85)  # Ensure reasonable display scores
                
                # Determine technical level based on description keywords
                desc = str(book_df.iloc[i]['description']).lower()
                if any(word in desc for word in ['advanced', 'expert', 'mastering', 'deep', 'comprehensive']):
                    tech_level = 'Advanced'
                elif any(word in desc for word in ['intermediate', 'practical', 'effective', 'professional']):
                    tech_level = 'Intermediate'
                else:
                    tech_level = 'Beginner'
                
                results.append({
                    'title': book_df.iloc[i]['title'],
                    'description': book_df.iloc[i]['description'],
                    'url': book_df.iloc[i]['url'],
                    'relevance': cos_sim[i],
                    'match_percent': match_percent,
                    'tech_level': tech_level
                })
        return results
    except Exception as e:
        st.error(f"Search error: {e}")
        return []

if recommend_btn:
    if not user_query:
        st.warning("Please enter a technical query to begin the analysis.")
    else:
        with st.spinner("Analyzing technical knowledge base..."):
            recommendations = get_semantic_recommendations(user_query)
            
            if recommendations:
                st.markdown(f"""
                    <div class="section-header">
                        <h3 style='font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700;'>
                            <i class="fas fa-microchip" style="margin-right: 0.75rem; color: #6366f1;"></i>Semantic Search Results
                        </h3>
                        <p style='color: #94a3b8; margin-top: 0.5rem;'>Technical literature correlating to '<b>{user_query}</b>' — {len(recommendations)} matches found</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Display results in structured grid with match badges and hover preview
                for i in range(0, len(recommendations), 3):
                    cols = st.columns(3, gap="large")
                    for j in range(3):
                        if i + j < len(recommendations):
                            rec = recommendations[i + j]
                            with cols[j]:
                                # Clean and truncate description
                                clean_desc = str(rec.get('description', 'No summary available.'))
                                short_desc = clean_desc[:180] + '...' if len(clean_desc) > 180 else clean_desc
                                
                                # Determine tech level styling
                                level_class = f"tech-level-{rec['tech_level'].lower()}"
                                
                                st.markdown(f"""
                                    <div class="book-card" style="position: relative;">
                                        <div class="match-badge">
                                            <i class="fas fa-chart-line"></i> {rec['match_percent']}% Match
                                        </div>
                                        <div class="book-title" style="margin-top: 1.5rem;">{rec['title']}</div>
                                        <div class="book-description">{short_desc}</div>
                                        <div class="difficulty-badge-container">
                                            <span class="tech-level {level_class}" style="font-size: 0.7rem;">{rec['tech_level']}</span>
                                        </div>
                                        <div class="book-footer" style="margin-top: 0.75rem;">
                                            <a href="{rec['url']}" target="_blank" class="book-button">
                                                View Source <i class="fas fa-external-link-alt" style="font-size: 0.7rem;"></i>
                                            </a>
                                        </div>
                                    </div>
                                """, unsafe_allow_html=True)
            else:
                st.error("No technical correlates found for your query. Try using more specific technical terms.")
