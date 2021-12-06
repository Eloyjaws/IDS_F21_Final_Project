import sys
sys.path.append("..")


import streamlit.components.v1 as components
import streamlit as st
from PIL import Image
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import text
import plots
import utils
from pathlib import Path
# from utils import get_productivity_countries_list, get_productivity_data

# Use Wide Page Format
# st.set_page_config(layout="wide")

ROOT_DIR = Path(__file__).parent.parent.resolve()

logo = Image.open(ROOT_DIR.joinpath("images/world.png"))
st.image(
    logo,
    width=100,
)

st.title(text.Title)
# world_bank_screenshot = Image.open("world_bank.png")
productivity_data = utils.get_productivity_data()
productivity_df = productivity_data.copy()


st.sidebar.subheader("Render Menu")
show_social_connections = st.sidebar.checkbox("Social Connections", True)
show_internet_stats = st.sidebar.checkbox("Internet Statistics", True)
show_social_media_stats = st.sidebar.checkbox("Social Media Statistics", True)
show_loneliness_stats = st.sidebar.checkbox("Loneliness Statistics", True)


if show_social_connections:
    st.subheader("How Important are Social Connections for our health?")
    happiness_image = Image.open(ROOT_DIR.joinpath("images/happiness-and-friends.png"))
    st.image(happiness_image)

    # Facebook Social Connectedness
    components.html(
        '<div class="flourish-embed flourish-globe" data-src="visualisation/7988652"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    st.subheader('Impact of Connections on Employment')
    components.html(
        '<div class="flourish-embed flourish-chart" data-src="visualisation/8037091"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    # EU
    components.html(
        '<div class="flourish-embed flourish-map" data-src="visualisation/7985810"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    # Productivity # TODO: What has this got to do with our work?
    st.subheader('Impact of Internet on Productivity')
    components.html(
        '<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/7987034"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    # Static Comparison of Productivity
    selected_entities = st.multiselect(
        label="Select interested economic entities for comparison",
        options=utils.get_productivity_countries_list(),
        default=["United States", "Japan", "South Africa", "Australia", "China", "Spain", "Brazil"]
    )
    if selected_entities:
        productivity_filtered = productivity_df[productivity_df["Entity"].isin(selected_entities)].rename(columns={"Productivity (PWT 9.1 (2019))":"Productivity"})
        productivity_plot = plots.lineplot(
            productivity_filtered,
            'Year',
            'Productivity',
            'Year',
            'GDP per hour work ($)',
            'Entity',
            ['Entity', 'Year', 'Code', 'Productivity'],
            'Productivity Comparison Amongst Countries',
        )

        st.altair_chart(productivity_plot, use_container_width=True)

if show_internet_stats:
    st.header('Internet Trends and Impacts')
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8020581"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    
    st.subheader('Offline Statistics')
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016773"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016831"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    st.subheader('Internet Users Ranking by Countries')
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016698"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016738"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016719"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016758"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    st.subheader("The Internet - usage across the world")
    components.html(
        '<div class="flourish-embed" data-src="story/1056561"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)




if show_social_media_stats:
    st.header('Rise of Social Media - Trends and Stats')
    # MAU for Social Media Platform (2002 - 2018)
    st.subheader("Online Social Networking Trends amongst Young Users")
    components.html(
        '<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/8030229"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    st.subheader("Online Social Networking Trends amongst Young Users")
    components.html(
        '<div class="flourish-embed flourish-chart" data-src="visualisation/8015401"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    # Social Media Usage by Gender Distribution
    st.subheader("Online Social Networking Trends amongst Young Users")
    components.html(
        '<div class="flourish-embed flourish-chart" data-src="visualisation/8016063"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    st.subheader("Daily Hours spent with digital Media, United States, 2008 - 2018")
    components.html(
        '<div class="flourish-embed flourish-chart" data-src="visualisation/8040586"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    st.subheader("Daily time spent on the Internet by young people, 2016")
    components.html(
        '<div class="flourish-embed flourish-chart" data-src="visualisation/8040725"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

if show_loneliness_stats:
    st.header("Social Isolation & Loneliness")
    components.html(
        '<div class="flourish-embed flourish-map" data-src="visualisation/7985093"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    # Loneliness
    components.html(
        '<div class="flourish-embed flourish-map" data-src="visualisation/7985093"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    # Friends/Relatives to Count on
    components.html(
        '<div class="flourish-embed flourish-map" data-src="visualisation/7989899"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    # One-Person Household
    components.html(
        '<div class="flourish-embed flourish-scatter" data-src="visualisation/7991020"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

# st.header("Extra: how well do you know your country's internet ranking?")
st.header("Extra: Predict Internet Availability & Affrodability using GNI and 3i data?")

st.header("Conclusion")
st.write(text.Conclusion)


with st.expander("References"):
    st.markdown(text.References, unsafe_allow_html=True)

st.sidebar.markdown(text.Footer, unsafe_allow_html=True)
