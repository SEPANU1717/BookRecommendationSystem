import streamlit as st
import os
from PIL import Image
import base64

def get_img_as_base64(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
        base64_encoded = base64.b64encode(image_data).decode("utf-8")
    return base64_encoded

background_image_path = "image/s.png"
image_path = "image/mm.png"
im = Image.open(image_path)
im2 = Image.open("image/logoside.png")
st.set_page_config(page_title="BastonedProject", page_icon=im)

background_image = Image.open(background_image_path)


st.markdown("""<style> .css-1544g2n.e1fqkh3o4 {margin-top: -70px;}</style>""", unsafe_allow_html=True)
st.markdown("""<style> .css-uf99v8.egzxvld5 {margin-top: -50px;}</style>""", unsafe_allow_html=True)

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

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 