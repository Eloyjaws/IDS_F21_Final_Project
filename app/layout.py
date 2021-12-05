import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image

# --------- GLOBAL VARIABLES ----------- #
IMAGE_DIR = "../images/"

# Base heading for main page
title_img = Image.open(IMAGE_DIR + "connections_title.jpg")
st.image(title_img)
st.title("Social Connections & the Internet")

# Base heading for side bar
sidebar_img = Image.open(IMAGE_DIR + "connections_sidebar.jpg")
st.sidebar.image(sidebar_img)
st.sidebar.title("Navigation")

content_choice = st.sidebar.radio("Choose Content", \
    ["Intro", "Social Connections", "Rise of Internet & Social Media", "Loneliness, Covid-19, and More", "In a Nutshell", "References"])

if content_choice == "Intro":
    # display relevant content
    st.write(content_choice)

elif content_choice == "Social Connections":
    # display relevant content
    st.write(content_choice)

elif content_choice == "Rise of Internet & Social Media":
    # display relevant content
    st.write(content_choice)

elif content_choice == "Loneliness, Covid-19, and More":
    # display relevant content
    st.write(content_choice)

elif content_choice == "In a Nutshell":
    # display relevant content
    st.write(content_choice)

elif content_choice == "References":
    # display relevant content
    st.write(content_choice)