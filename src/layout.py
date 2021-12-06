import sys
# from src.app import ROOT_DIR
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
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.resolve()
# Use Wide Page Format
# st.set_page_config(layout="wide")

# Base heading for side bar
sidebar_img = Image.open(ROOT_DIR.joinpath("images/connections_sidebar.jpg"))
st.sidebar.image(sidebar_img)
st.sidebar.title("Social Connections & the Internet")

content_choice = st.sidebar.radio(
    "Menu", [
        "Intro",
        "Social Connections",
        "Internet: Trends and Impacts",
        "Rise of Social Media",
        "Loneliness",
        "Conclusion"
    ])

if content_choice == "Intro":
    # display relevant content
    # Base heading for main page
    title_img = Image.open(ROOT_DIR.joinpath("images/connections_title.jpg"))
    st.image(title_img)
    st.title("Social Connections & the Internet")
    st.markdown(text.Introduction, unsafe_allow_html=True)

elif content_choice == "Social Connections":
    # display relevant content
    st.header("How Important are Social Connections for our health?")
    st.markdown(text.social_connections_blurb_one, unsafe_allow_html=True)
    st.write(text.social_connections_blurb_two)
    happiness_image = Image.open(ROOT_DIR.joinpath("images/happiness-and-friends.png"))
    st.image(happiness_image)

    st.subheader('Impact of Connections on Job Seeking')
    st.write(text.social_connections_blurb_three)
    with st.expander('Click to view insights on Impact of Connections on Job Seeking'):
        components.html(
            '<div class="flourish-embed flourish-chart" data-src="visualisation/8037091"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

        # EU
        components.html(
            '<div class="flourish-embed flourish-map" data-src="visualisation/7985810"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=550)

    # Productivity # TODO: What has this got to do with our work?
    st.subheader('Impact of Connections on Productivity')
    st.write(text.social_connections_blurb_four)
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

elif content_choice == "Internet: Trends and Impacts":
    # display relevant content
    # st.header('Internet: Trends and Impacts')
    st.header("The Internet usage across the world - A brief story")
    components.html(
        '<div class="flourish-embed" data-src="story/1056561"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=750)

    st.subheader('Internet Usage Ranking by Countries')
    # with st.expander('Internet Users in Millions'):
    #     components.html(
    #     '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016698"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)
    #     components.html(
    #     '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016738"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)
    # with st.expander('Internet Users by Share of Population'):
    #     components.html(
    #     '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016719"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)
    #     components.html(
    #     '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016758"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    # with st.expander('Offline Statistics'):
    #     components.html(
    #     '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016773"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)
    #     components.html(
    #     '<div class="flourish-embed flourish-scatter" data-src="visualisation/8016831"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    with st.expander("Click for insight on Daily time spent on the Internet by young people, 2016"):
        st.write(text.internet_daily_time_spent)
        components.html(
            '<div class="flourish-embed flourish-chart" data-src="visualisation/8040725"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    with st.expander("Click for insight on Daily Hours spent with digital Media, United States, 2008 - 2018"):
        st.write(text.digital_media_time_spent)
        components.html(
            '<div class="flourish-embed flourish-chart" data-src="visualisation/8040586"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    st.subheader('Is there a Relationship between Internet User Population and GNI per capital of countries?')
    st.write(text.internet_usage_gni)
    with st.expander('Click to read more on Internet User Population and GNI per capital of countries?'):
        components.html(
        '<div class="flourish-embed flourish-scatter" data-src="visualisation/8020581"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)
    
    st.subheader('Is the Internet usage really Inclusive?')
    st.write(text.internet_inclusivity_index)
    with st.expander('Insert 3i plot here. Select 5 countries to view their internet inclusivity score'):
        st.write('Insert plot here')

elif content_choice == "Rise of Social Media":
    # display relevant content
    st.write(content_choice)
    st.header('Rise of Social Media - Trends and Stats')

    # Facebook Social Connectedness
    st.subheader('Facebook Connected Index')
    st.write(text.social_connectednes_blurb_one)
    st.latex(r'''
        Social\ Connectedness_{i,j} = \frac{FB\_Connections_{i,j}}{FB\_Users_i * FB\_Users_j}
    ''')
    st.latex(r'''FB\_Users_i\ and\ FB\_Users_j\ are\ number\ of\ Facebook\ users\ in\ locations\ i\ and\ j''')
    st.latex(r'''FB\_Connections_{i,j}\ is\ the\ number\ of\ connections\ between\ the\ two\ locations''')
    components.html(
        '<div class="flourish-embed flourish-globe" data-src="visualisation/8038403"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=650)
    st.write(text.social_connectednes_blurb_two)
    

    # MAU for Social Media Platform (2002 - 2018)
    st.subheader("Online Social Networking Trends amongst Young Users")
    st.write(text.social_media_maus_blurb)
    components.html(
        '<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/8030229"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=650)

    st.subheader("Online Social Networking Trends amongst Young Users")
    st.write(text.social_media_young_users_blurb)
    components.html(
        '<div class="flourish-embed flourish-chart" data-src="visualisation/8015401"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    # Social Media Usage by Gender Distribution
    st.subheader("Usage of Social Media Platforms by Gender Distribution")
    st.write(text.social_media_gender_blurb)
    components.html(
        '<div class="flourish-embed flourish-chart" data-src="visualisation/8016063"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

elif content_choice == "Loneliness":
    # display relevant content
    st.header("Social Isolation & Loneliness")

    # Loneliness
    st.write(text.loneliness_self_reported_blurb)
    components.html(
        '<div class="flourish-embed flourish-map" data-src="visualisation/7985093"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    # Friends/Relatives to Count on
    st.header('Factors Impacting Social Isolation & loneliness')
    st.subheader('Close Friends & Relatives')
    with st.expander('Click to view insight'):
        st.write(text.loneliness_friends_relative_blurb)
        components.html(
            '<div class="flourish-embed flourish-map" data-src="visualisation/7989899"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)

    # One-Person Household
    st.subheader('One-Person Household, GDP per Capita & Increasing Loneliness')
    with st.expander('Click to view insight'):
        st.write(text.loneliness_single_person_household_impact_blurb_one)
        components.html(
            '<div class="flourish-embed flourish-scatter" data-src="visualisation/7991020"><script src="https://public.flourish.studio/resources/embed.js"></script></div>', height=600)
        st.write(text.loneliness_single_person_household_impact_blurb_two)

elif content_choice == "Conclusion":
    # display relevant content
    # st.write(content_choice)
    st.header("Conclusion")
    st.write(text.Conclusion)

    with st.expander("References"):
        st.markdown(text.References, unsafe_allow_html=True)

st.sidebar.markdown(text.Footer, unsafe_allow_html=True)
