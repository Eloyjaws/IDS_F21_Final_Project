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
import plots
import utils


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
    st.header("How Important are Social Connections for our health?")
    st.markdown(text.social_connections_paragraph_one, unsafe_allow_html=True)
    st.write(text.social_connections_paragraph_two)
    happiness_image = Image.open("images/happiness-and-friends.png")
    st.image(happiness_image)

    st.subheader('Impact of Connections on Job Seeking')
    st.write(text.social_connections_paragraph_three)
    with st.expander('Click to view insights on Impact of Connections on Job Seeking'):
        components.html(
            '<div class="flourish-embed flourish-chart" data-src="visualisation/8037091"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

        # EU
        components.html(
            '<div class="flourish-embed flourish-map" data-src="visualisation/7985810"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    # Productivity # TODO: What has this got to do with our work?
    st.subheader('Impact of Connections on Productivity')
    st.write(text.social_connections_paragraph_four)
    with st.expander('Click to view insights on Impact of Connections on Productivity'):
        components.html(
            '<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/7987034"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

        # Static Comparison of Productivity
        selected_entities = st.multiselect(
            label="Select interested economic entities for comparison",
            options=utils.get_productivity_countries_list(),
            default=["United States", "Japan", "South Africa", "Australia", "China", "Spain", "Brazil"]
        )

        # Fetch Data
        productivity_data = utils.get_productivity_data()
        productivity_df = productivity_data.copy()

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

elif content_choice == "Rise of Internet":
    # display relevant content
    st.header('Internet Trends and Impacts')
    st.subheader("The Internet - usage across the world; A brief story")
    components.html(
        '<div class="flourish-embed" data-src="story/1056561"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    

    st.subheader('Is there a Relationship between Internet User Population and GNI per capital of countries?')
    with st.expander('Click to read more on Internet User Population and GNI per capital of countries?'):
        components.html(
        '<div class="flourish-embed flourish-scatter" data-src="visualisation/8020581"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    
    st.subheader('Internet Users Ranking by Countries')
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016698"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016738"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016719"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016758"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

    st.subheader('Offline Statistics')
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016773"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)
    components.html(
    '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016831"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=800)

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