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


image_path = "image/mm.png"
im = Image.open(image_path)
im2 = Image.open("image/logoside.png")
st.set_page_config(page_title="BastonedProject", page_icon=im)


# Define the tabs
tab1, tab2, tab3, = st.tabs(["About Us", "Project Description", "Team Members"])


# Part 2: Tab 2 - About Us
with tab1:
    st.header("About Us")
    st.write("Introducing our cutting-edge programming book recommendation system! Are you bored of searching through innumerable programming books in search of the best suit for your requirements? There is no need to look any further! Based on your preferences and interests, our recommendation engine uses cutting-edge algorithms to select the most relevant and high-quality programming books.")
    st.write("Our technology evaluates your prior book selections, as well as your intended programming languages and areas of specialization, in a matter of seconds to present you with unique recommendations that are tailored directly to you. Whether you're a newbie hoping to learn the fundamentals or an experienced developer looking for advanced information, our system has you covered.")
    st.write("Our extensive dataset of programming books includes volumes from all major publishers as well as unique publications that are difficult to locate elsewhere. You can trust that the books recommended by our system are of the best quality and relevance, guaranteeing that your time is well spent.")
    st.write("So, what are you holding out for? Try out our programming book suggestion system today to boost your coding skills!")

# Part 3: Tab 3 - Team Members
with tab3:
    st.header("Team Members")
    team_members = [
        {"name": "Manalo, Mark Christianiel", "info": "System Developer, manalo.2566146@balayan.sti.edu.ph"},
        {"name": "Lagazo, Jonah Levi", "info": "Leader, lagazo.261249@balayan.sti.edu.ph"},
        {"name": "Aboy, Geian", "info": "aboy.244098@balayan.sti.edu.ph"},
        {"name": "Lagan, Jefferson", "info": "lagan.260664@balayan.sti.edu.ph"},
        {"name": "Monroyo, John Andrei", "info": "monroyo.265776@balayan.sti.edu.ph"},
    ]
    
    for member in team_members:
        expander = st.expander(member["name"])
        expander.write(member["info"])

# Part 4: Tab 4 - Project Description
with tab2:
    st.header("Project Description")
    st.write("The Book Recommendation System for Programmers is a web application designed to help programmers find books that are relevant to their interests. The system uses a content-based filtering algorithm to recommend books based on user interest.")
    st.write("The system is built using the Python programming language and several libraries such as Streamlit, Pandas, NumPy, and Pillow. The data used in the system is stored in a CSV file, and the similarity matrix is computed using a pre-trained model in a pickle file.")
    st.write("The main menu of the system includes four options: Home Page, Recommendation, Book List, About Us, and Contact. The Home page allows users to select a book from a dropdown list and click on a 'Recommend me' button to get a list of recommended books. The Book List page displays a list of CSV files that can be selected to show their contents. The About Us page provides information about the team members and the project description. Finally, the Contact page allows users to send messages to the team.")
    st.write("The Home page also includes a sidebar menu with icons that represent each option. The Book List page has a button that allows users to show the contents of the selected CSV file. The About Us page uses tabs to display different information such as the team members, project description. The Contact page uses a form that allows users to enter their name, email, and message.")
    st.write("The web application is styled using a CSS file that includes custom styles to improve the user interface. A custom library called streamlit_option_menu is also used to create the dropdown menus in the system.")
    st.write("Overall, the Book Recommendation System for Programmers is a useful tool for programmers who are looking for books that are relevant to their interests. The system is easy to use and provides recommendations based on user preferences.")

# Hide Streamlit footer
hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
