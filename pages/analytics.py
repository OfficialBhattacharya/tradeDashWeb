from dash import html

import dash
import dash_bootstrap_components as dbc

from .side_bar import sidebar

dash.register_page(
    __name__,
    name="Analytics",
    top_nav=True,
)


def layout(**kwargs):
    return dbc.Row(
        [dbc.Col(sidebar(), width=2), dbc.Col(html.Div("Analytics Home Page"), width=10)]
    )