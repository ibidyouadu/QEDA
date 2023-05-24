from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd

from mod_plot import create_scatterplot
from mod_upload import parse_upload

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id="upload-data",
        children=html.Button(["Upload data"]),
    ),
    dcc.Graph(id="plot")
])

@app.callback(
    Output("upload-data", "children"),
    Output("plot", "figure"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    prevent_initial_call=True
)
def update_output(contents, fname):
    if contents is not None:
        fig = parse_upload(contents, fname)
        return html.Div(style={"hidden":True}), fig

if __name__ == "__main__":
    app.run_server(debug=True)