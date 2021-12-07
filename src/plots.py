import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

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
