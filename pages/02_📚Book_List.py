import streamlit as st
import pandas as pd
import base64
import os
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import base64

def get_img_as_base64(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
        base64_encoded = base64.b64encode(image_data).decode("utf-8")
    return base64_encoded

background_image_path = "image/pj.png"
image_path = "image/mm.png"
im = Image.open(image_path)
im2 = Image.open("image/logoside.png")
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



st.header("Book List")
    
    # Define function to load CSV files
def load_data(folder_path):
        csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
        data_dict = {}
        for file in csv_files:
            file_path = os.path.join(folder_path, file)
            data_dict[file[:-4]] = pd.read_csv(file_path)
        return data_dict

    # Load CSV files and create select box
data_dict = load_data('csvfiles')
file_name = st.selectbox('Select a Programming language:', list(data_dict.keys()))
df = data_dict[file_name]

    # Show the selected CSV file
if st.button('Show Books'):
        df['url'] = df['url'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
        df.index = range(1, len(df) + 1)  # Update the index to start from 1
        st.write(df.to_html(escape=False), unsafe_allow_html=True)

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
