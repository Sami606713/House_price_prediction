import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from joblib import load
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
