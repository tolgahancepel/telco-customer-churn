import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

import os
import sys
import copy
import time

from src.navbar import get_navbar
from src.graphs import df, layout
from content import tab_prediction_content, tab_analysis_content

# Creating the app

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets = [dbc.themes.SUPERHERO,'/assets/styles.css']
) 

server=app.server

# Tabs Content

tabs = dbc.Tabs(
    [
        dbc.Tab(tab_prediction_content, label="Prediction"),
        dbc.Tab(tab_analysis_content, label="Data Analysis"),
    ]
)


jumbotron = dbc.Jumbotron(
    [
        # html.H1("Jumbotron", className="display-3"),
        # html.P(
        #     "Use a jumbotron to call attention to "
        #     "featured content or information.",
        #     className="lead",
        # ),
        # html.Hr(className="my-2"),
        html.H4("Telco Customer Churn Analysis and Prediction"),
        # html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ], className="cover"
)


# App Layout

app.layout = html.Div(
    [
        get_navbar(),

        jumbotron,

        html.Div(
            [
                dbc.Row(dbc.Col(tabs, width=12)),
            ], id="mainContainer",style={"display": "flex", "flex-direction": "column"}
        ),

        html.P("Developed by Tolgahan Çepel", className="footer")


    ],
)

# Callbacks

@app.callback(
    Output("categorical_bar_graph", "figure"),
    [
        Input("categorical_dropdown", "value"),
    ],
)

def bar_categorical(feature):

    time.sleep(0.2)

    temp = df.groupby([feature, 'Churn']).count()['customerID'].reset_index()
    
    fig = px.bar(temp, x=feature, y="customerID",
             color=temp['Churn'].map({'Yes': 'Churn', 'No': 'NoChurn'}),
             color_discrete_map={"Churn": "#47acb1", "NoChurn": "#f26522"},
             barmode='group')
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    _title = (feature[0].upper() + feature[1:]) + " Distribution by Churn"
    
    fig.update_layout(
        title = {'text': _title, 'x': 0.5},
        #xaxis_visible=False,
        xaxis_title="",
        yaxis_title="Count",
        legend_title_text="",
        legend = {'x': 0.16}
    )
    return fig

@app.callback(
    Output("categorical_pie_graph", "figure"),
    [
        Input("categorical_dropdown", "value"),
    ],
)

def donut_categorical(feature):

    time.sleep(0.2)

    temp = df.groupby([feature]).count()['customerID'].reset_index()

    fig = px.pie(temp, values="customerID", names=feature, hole=.5,
                            #color=temp['Churn'].map({'Yes': 'Churn', 'No': 'NoChurn'}),
                                #color_discrete_map={"Churn": "#47acb1",
                                                            #"NoChurn": "#f26522"},
    )

    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    _title = (feature[0].upper() + feature[1:]) + " Percentage"

    fig.update_layout(
        title = {'text': _title, 'x': 0.5},
        legend = {'x': 0.24}
    )

    return fig



@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)

# we use a callback to toggle the collapse on small screens
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open





if __name__ == "__main__":
    app.run_server(debug=True, port=8050)