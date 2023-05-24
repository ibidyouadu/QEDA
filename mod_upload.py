import pandas as pd
import base64
import io
from dash import html

from mod_plot import create_scatterplot

def parse_upload(contents, fname):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in fname:
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8"))).head(50)
            fig = create_scatterplot(df, "Merged_All_LEN", "Merged_All_WID")
    except Exception as e:
        print(e)
        return html.Div(["Could not process the file."])

    return fig