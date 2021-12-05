import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

DATA_DIR = "../Data/productivity/"


# Loneliness
components.html("""
    <div class="flourish-embed flourish-map" data-src="visualisation/7985093">
    <script src="https://public.flourish.studio/resources/embed.js">
    </script>
    </div>
""", height=600)

# Job Searches
# EU
components.html("""
    <div class="flourish-embed flourish-map" data-src="visualisation/7985810">
    <script src="https://public.flourish.studio/resources/embed.js">
    </script>
    </div>
""", height=600)

# US Job Search
df_job_us = pd.read_csv(DATA_DIR + "job-seeker-job-search-pew.csv").sort_values(by="Proportion", ascending=False)
fig = plt.figure(figsize=(20, 10))
job_plot = sns.barplot(data=df_job_us, x="Proportion", y="Method", orient="h")
job_plot.set_xlabel("Proportion (%)", fontsize=20)
job_plot.set_yticklabels(job_plot.get_yticklabels(), fontsize=20)
job_plot.set_title("Job Search Mehthods in US - 2015", fontsize=40)
job_plot.set(ylabel=None)
st.pyplot(fig)

# Productivity
components.html("""
    <div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/7987034">
    <script src="https://public.flourish.studio/resources/embed.js">
    </script>
    </div>
""", height=600)
# Static Comparison
entities = list(pd.read_csv(DATA_DIR + "productivity_transposed.csv")["Entity"])
df_product = pd.read_csv(DATA_DIR + "productivity.csv")
interested_entities = st.multiselect(label="Select interested economic entities for comparison",
                                    options=entities,
                                    default=["United States", "Japan", "South Africa", "Australia", "China", "Spain", "Brazil"])
df_product_filtered = df_product[df_product["Entity"].isin(interested_entities)].rename(columns={"Productivity (PWT 9.1 (2019))":"Productivity"})
fig = plt.figure(figsize=(20, 10))
job_plot = sns.lineplot(data=df_product_filtered, x="Year", y="Productivity", hue="Entity")
job_plot.set_xlabel("Year", fontsize=20)
job_plot.set_ylabel("GDP per hour work ($)", fontsize=20)
job_plot.set_yticklabels(job_plot.get_yticklabels(), fontsize=20)
job_plot.set_title("Productivity Comparison", fontsize=40)

st.pyplot(fig)

# Facebook Social Connectedness
components.html("""
    <div class="flourish-embed flourish-globe" data-src="visualisation/8038403">
    <script src="https://public.flourish.studio/resources/embed.js">
    </script></div>
""", height=600)

# Friends/Relatives to Count on
components.html("""
    <div class="flourish-embed flourish-map" data-src="visualisation/7989899">
    <script src="https://public.flourish.studio/resources/embed.js">
    </script></div>
""", height=600)

# One-Person Household
components.html("""
    <div class="flourish-embed flourish-scatter" data-src="visualisation/7991020">
    <script src="https://public.flourish.studio/resources/embed.js">
    </script></div>
""", height=600)


