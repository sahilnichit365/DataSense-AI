import plotly.express as px

def create_histogram(df, column):
    return px.histogram(df, x=column)

def create_bar_chart(df, column):
    value_counts = df[column].value_counts().reset_index()
    value_counts.columns = [column, "Count"]
    return px.bar(value_counts, x=column, y="Count")

def create_scatter_plot(df, x_col, y_col):
    return px.scatter(df, x=x_col, y=y_col)

def create_heatmap(df):

    corr = df.corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    return fig