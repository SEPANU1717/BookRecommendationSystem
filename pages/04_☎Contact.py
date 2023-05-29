import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import base64

def get_img_as_base64(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
        base64_encoded = base64.b64encode(image_data).decode("utf-8")
    return base64_encoded

background_image_path = "image/mmm.png"
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


st.header("Get in touch with Us")
st.write("Please use the form below to send us a message:")
contact_form = """
        <form action="https://formsubmit.co/bastonedproject@gmail.com" 
              method="POST">
             <input type="hidden" name="_captcha" value="false">     
             <input type="text" name="name" placeholder="Your Name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here"></textarea>
             <button type="submit">Send</button>
        </form>
        """
st.markdown(contact_form, unsafe_allow_html=True)

# CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

hide_streamlit_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
