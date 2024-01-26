import streamlit as st
from utils import read_data,load_image,load_model,load_tailwind
import numpy as np
import pandas as pd

# Streamlit app page config
# st.set_page_config(page_title="Dashboard", page_icon=":house:", layout="wide")

def dashboard():
    st.write("Dashboard")


def main():
    navbar_classes = "bg-gray-500 text-white p-4 rounded border border-white-500"
    nav_item_classes = "mr-4 hover:text-white cursor-pointer"

    # Add a navigation menu in the navbar
    st.markdown(
    f"""
    <div class="{navbar_classes} text-center text-2xl">
        <span class="{nav_item_classes}  bg-white-500 text-black py-2 hover:text-white px-4 rounded hover:bg-green-500 border border-white-500 p-4" onclick="location.href='/prediction'">Prediction</span>
        <span class="{nav_item_classes} bg-white-500 text-black py-2 hover:text-white px-4 rounded hover:bg-blue-500 border border-white-500 p-4" onclick="location.href='/dashboard'">Dashboard</span>
    </div>
    """,
    unsafe_allow_html=True
    )

# Get the current page
    page = st.query_params.get("page", "prediction")
    # Display the selected page
    if page == "prediction":
        prediction()
    elif page == "dashboard":
        dashboard()
