import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from joblib import load
import streamlit as st

# Read dataset
def read_data(file_path):
    df=pd.read_csv(file_path)
    return df

# Load the image
def load_image():
    img=Image.open("src/Notebook/house.jpg")
    return img

def load_model(path):
    model=load(path)
    return model

def load_tailwind():
    return st.markdown(
        """
        <style>
            @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');
        </style>
        """,
        unsafe_allow_html=True
        )
