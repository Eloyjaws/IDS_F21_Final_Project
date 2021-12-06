import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

def sns_lineplot(df, x, y, x_label, y_label, plot_title, color=None):
    fig = plt.figure(figsize=(20, 10))
    line_plot = sns.lineplot(data=df, x=x, y=y, hue=color)
    line_plot.set_xlabel(x_label, fontsize=20)
    line_plot.set_ylabel(y_label, fontsize=20)
    line_plot.set_yticklabels(line_plot.get_yticklabels(), fontsize=20)
    line_plot.set_title(plot_title, fontsize=40)
    return fig

def lineplot(data, x, y, x_label, y_label, color, tooltip_list, plot_title):
    lineplot = alt.Chart(data).mark_line().encode(
        alt.X(x, axis=alt.Axis(title=x_label)),
        alt.Y(y, axis=alt.Axis(title=y_label)),
        color=color,
        tooltip=tooltip_list
    )
    return lineplot.properties(title=plot_title, height=600)
