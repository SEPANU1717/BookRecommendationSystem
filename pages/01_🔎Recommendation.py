import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
from PIL import Image
import base64


def get_img_as_base64(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
        base64_encoded = base64.b64encode(image_data).decode("utf-8")
    return base64_encoded

background_image_path = "image/sip.png"
image_path = "image/mm.png"
im = Image.open(image_path)

st.set_page_config(page_title="BastonedProject", page_icon=im)

background_image = Image.open(background_image_path)

page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{get_img_as_base64(background_image_path)}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center center;
    }}
    </style>
    """

st.markdown(page_bg_img, unsafe_allow_html=True)




book_df = pd.read_csv("bastonedd.csv")
similarity = pickle.load(open("similarity.pkl", "rb"))

st.header("Book Recommendation System for Programmers")

list_book = np.array(book_df["title"])
list_book_unique = np.unique(list_book)  # Get unique book titles
list_book_placeholder = [''] + list_book_unique.tolist()  # Add an empty string as a placeholder option
option = st.selectbox("Select Book", list_book_placeholder)

# Function to get recommended book URLs
def show_url(book):
    x = []
    index = book_df[book_df['title'] == book].index
    if len(index) > 0:
        index = index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        for i in distances[1:6]:
            url = book_df.iloc[i[0]]['url']
            x.append(url)
    return x

# Function to get recommended book titles and descriptions
def book_recommend(book):
    index = np.where(list_book == book)[0][0]
    distances = similarity[index]
    indices = np.argsort(distances)[::-1][1:6]
    recommended_books = list_book[indices]
    recommended_descriptions = book_df.iloc[indices]['description']
    
    # Remove the selected book from recommendations
    mask = recommended_books != book
    recommended_books = recommended_books[mask]
    recommended_descriptions = recommended_descriptions[mask]
    
    return recommended_books, recommended_descriptions

# Button to get recommendations
if st.button('Recommend Me'):
    if option == '':
        st.write("No book selected. Please choose a book from the list.")
    else:
        recommended_books, recommended_descriptions = book_recommend(option)
        if len(recommended_books) > 0:
            st.write('Books recommended for "{}" are:'.format(option))
            df = pd.DataFrame({
                'Book Recommended': recommended_books,
                'description': recommended_descriptions,
                'Book url': show_url(option)
            })
            # Format URLs as hyperlinks
            df['Book url'] = df['Book url'].apply(lambda x: '<a href="{}" target="_blank">Link</a>'.format(x))
            df.index = [''] * len(df.index)
            st.write(df.to_html(escape=False), unsafe_allow_html=True)
        else:
            st.write("No books found for '{}'.".format(option))

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
