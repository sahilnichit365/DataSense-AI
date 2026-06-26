import plotly.express as px

def create_histogram(df, column):
    fig = px.histogram(df, x=column)
    return fig

def create_bar_chart(df, column):
    value_counts = df[column].value_counts().reset_index()
    value_counts.columns = [column, "Count"]

    fig = px.bar(
        value_counts,
        x=column,
        y="Count"
    )
    return fig

def create_scatter_plot(df, x_col, y_col):
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col
    )
    return fig