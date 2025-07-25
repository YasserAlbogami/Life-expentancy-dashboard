# utils.py
import streamlit as st
import base64
import os

def apply_custom_style():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def add_logo_to_sidebar():
    # Get the absolute path of the current script (main_app.py directory)
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "layout_set_logo.png")  # change name to match your file

    # Read and encode the image
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    # Display the image in the sidebar
    st.sidebar.markdown(
        f"""
        <img src="data:image/png;base64,{encoded}" class="logo">
        """,
        unsafe_allow_html=True,
    )
