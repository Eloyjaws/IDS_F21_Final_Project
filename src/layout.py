import sys
sys.path.append("..")

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

import text


# Base heading for side bar
sidebar_img = Image.open("images/connections_sidebar.jpg")
st.sidebar.image(sidebar_img)
st.sidebar.title("Social Connections & the Internet")

content_choice = st.sidebar.radio("Menu", \
    ["Intro", "Social Connections", "Rise of Internet", "Rise of Social Media", "Loneliness, Covid-19, and More", "Conclusion", "References"])

if content_choice == "Intro":
    # display relevant content
    # Base heading for main page
    title_img = Image.open("images/connections_title.jpg")
    st.image(title_img)
    st.title("Social Connections & the Internet")
    st.markdown(text.Introduction, unsafe_allow_html=True)

elif content_choice == "Social Connections":
    # display relevant content
    st.write(content_choice)

elif content_choice == "Rise of Internet":
    # display relevant content
    st.write(content_choice)

elif content_choice == "Rise of Social Media":
    # display relevant content
    st.write(content_choice)

elif content_choice == "Loneliness, Covid-19, and More":
    # display relevant content
    st.write(content_choice)

elif content_choice == "Conclusion":
    # display relevant content
    st.write(content_choice)

elif content_choice == "References":
    # display relevant content
    st.write(content_choice)