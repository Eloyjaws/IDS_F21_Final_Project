import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import utils
import streamlit as st


def lineplot(data, x, y, x_label, y_label, color, tooltip_list, plot_title):
    lineplot = alt.Chart(data).mark_line().encode(
        alt.X(x, axis=alt.Axis(title=x_label)),
        alt.Y(y, axis=alt.Axis(title=y_label)),
        color=color,
        tooltip=tooltip_list
    )
    return lineplot.properties(title=plot_title, height=600)


def barplot(data, x, y, x_label, y_label, color, column, tooltip_list, plot_title):
    bars = alt.Chart(data).mark_bar().encode(
        x=alt.X(x, axis=alt.Axis(title=x_label)),
        y=alt.Y(y, axis=alt.Axis(title=y_label)),
        color=color,
        column=alt.Column(column),
        tooltip=tooltip_list
    )

    return bars.properties(title=plot_title, width=100)


def mlplot():
    df_viz = utils.get_ml_data()

    st.write("We trained a Random Forests model - XGBoost and got very good scores in calculating the relevance of the internet from its availability and affordability ")

    affordability = alt.Chart(df_viz).mark_circle().encode(
        x='AFFORDABILITY',
        y='RELEVANCE',
        color='GROUP',
    ).interactive()

    availability = alt.Chart(df_viz).mark_circle().encode(
        x='AVAILABILITY',
        y='RELEVANCE',
        color='GROUP',
    ).interactive()

    st.write("With a strong, affordable, available internet comes a better online community that generates relevant content for the country/culture")
    return (affordability + availability)
