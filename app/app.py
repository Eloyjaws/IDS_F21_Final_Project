import text
import plots
import utils
import streamlit.components.v1 as components
import streamlit as st
from PIL import Image
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
sys.path.append("..")

# Use Wide Page Format
# st.set_page_config(layout="wide")

logo = Image.open("world.png")
st.image(
    logo,
    width=100,
)

st.title(text.Title)
# world_bank_screenshot = Image.open("world_bank.png")


st.sidebar.subheader("Render Menu")
show_internet_stats = st.sidebar.checkbox("Internet Statistics", True)
show_social_media_stats = st.sidebar.checkbox("Social Media Statistics", True)
show_loneliness_stats = st.sidebar.checkbox("Loneliness Statistics", True)


if show_internet_stats:
    st.subheader("The Internet - usage across the world")
    components.html(
        '<div class="flourish-embed" data-src="story/1056561"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

if show_internet_stats:
    st.subheader("The impact of GNI per capita on the Internet population")
    components.html(
        '<div class="flourish-embed flourish-scatter" data-src="visualisation/8020581"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

if show_social_media_stats:
    st.subheader("The Internet - usage across the world")
    components.html(
        '<div class="flourish-embed" data-src="story/1056561"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

if show_loneliness_stats:
    st.subheader("The Internet - usage across the world")
    components.html(
        '<div class="flourish-embed" data-src="story/1056561"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

st.header("Extra: how well do you know your country's internet ranking?")

st.header("Conclusion")
st.write(text.Conclusion)


with st.expander("References"):
    st.markdown(text.References, unsafe_allow_html=True)

st.sidebar.markdown(text.Footer, unsafe_allow_html=True)
