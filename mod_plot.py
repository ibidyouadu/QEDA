import plotly.express as px

def create_scatterplot(df, x, y):
    fig = px.scatter(df, x=x, y=y)

    return fig