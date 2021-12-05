import sys
sys.path.append("..")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image

import streamlit as st
import streamlit.components.v1 as components

import utils
import plots
import text


logo = Image.open("world.png")
st.image(
    logo,
    width=100,
)

st.title(text.Title)
# world_bank_screenshot = Image.open("world_bank.png")



# components.html('<div class="flourish-embed flourish-chart" data-src="visualisation/7903916"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)