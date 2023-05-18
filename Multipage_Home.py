import os
import io
import csv
import random
from IPython import display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm
import time

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from IPython.display import Audio
import folium
import streamlit as st
from streamlit_folium import st_folium
from PIL import Image
st.set_page_config(layout="wide")


st.title("------------------------🐶서울특별시 반려동물 종합 플랫폼🐶------------------------\n")

image_file = 'a.png'
image_local = Image.open(image_file)
st.image(image_local, width=1500)
background_image = "a.png"


css = f"""

<style>
body {{
    background-image: url("{background_image}");
    background-size: cover;
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)    
