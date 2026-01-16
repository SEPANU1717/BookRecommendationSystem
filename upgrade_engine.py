import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import os

def clean_technical_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove special characters but keep technical ones like . (for .js, .net) or # (for C#)
    text = re.sub(r'[^a-z0-9+#.\s]', ' ', text)
    # Remove extra whitespace
    text = " ".join(text.split())
    return text

def upgrade_recommendation_engine():
    print("🚀 Starting Recommendation Engine Upgrade...")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_path, "bastonedd.csv")
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: {csv_path} not found.")
        return

    # 1. Load Data
    df = pd.read_csv(csv_path)
    print(f"📊 Loaded {len(df)} records.")

    # 2. Advanced Preprocessing
    # We combine title and description, giving the title 3x weight because it contains the most 
    # specific technical identifiers (e.g., "Python", "React", "C#").
    print("🧹 Preprocessing metadata...")
    df['clean_title'] = df['title'].apply(clean_technical_text)
    df['clean_desc'] = df['description'].apply(clean_technical_text)
    
    # Create a weighted feature string
    df['metadata'] = (df['clean_title'] + " ") * 3 + df['clean_desc']

    # 3. TF-IDF Vectorization (Better than CountVectorizer)
    # Use n-grams (1,2) to capture phrases like "machine learning" or "web development"
    print("📈 Generating TF-IDF Matrix (n-grams: 1, 2)...")
    tfidf = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        min_df=2, # Ignore terms that appear in only 1 book (likely noise)
        max_df=0.8 # Ignore terms that appear in more than 80% of books (too common)
    )
    
    tfidf_matrix = tfidf.fit_transform(df['metadata'])
    print(f"✨ Feature matrix shape: {tfidf_matrix.shape}")

    # 4. Compute Cosine Similarity
    print("🔄 Computing Similarity Matrix...")
    similarity = cosine_similarity(tfidf_matrix)

    # 5. Export for Streamlit App
    print("💾 Saving upgraded engine models...")
    
    # Save the cleaned dataframe
    with open(os.path.join(base_path, "book_recm.pkl"), "wb") as f:
        pickle.dump(df, f)
        
    # Save the similarity matrix
    with open(os.path.join(base_path, "similarity.pkl"), "wb") as f:
        pickle.dump(similarity, f)

    # Save the vectorizer for real-time search queries
    with open(os.path.join(base_path, "vectorizer.pkl"), "wb") as f:
        pickle.dump(tfidf, f)

    # Save the full TF-IDF matrix (the precomputed vectors for all books)
    with open(os.path.join(base_path, "tfidf_matrix.pkl"), "wb") as f:
        pickle.dump(tfidf_matrix, f)

    print("✅ Upgrade Complete! The system now uses TF-IDF with title-weighting and n-gram analysis.")

if __name__ == "__main__":
    upgrade_recommendation_engine()
