import pandas as pd
import numpy as np
from PIL import Image

# Read dataset
def read_data(file_path):
    df=pd.read_csv(file_path)
    return df

# Load the image
def load_image(img_path):
    img=Image.open(img_path)
    return img