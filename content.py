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

from src.graphs import dist_tenure, dist_monthlycharges, dist_totalcharges


# DATA ANALYSIS

card_tensure = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(figure = dist_tenure(), config = {"displayModeBar": False}, style = {"height": "42vh"})
            ]
        ),
    ],
    style = {"background-color": "#16103a"}
)

card_monthlycharges = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(figure = dist_monthlycharges(), config = {"displayModeBar": False}, style = {"height": "42vh"})
                    
            ]
        ),
    ],
    style = {"background-color": "#16103a"}
)



card_totalcharges = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(figure = dist_totalcharges(), config = {"displayModeBar": False}, style = {"height": "42vh"})
            ]
        ),
    ],
    style = {"background-color": "#16103a"}
)

card_categorical = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="categorical_bar_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ], style = {"height": "52vh"}
        ),
    ],
    style = {"background-color": "#16103a"}
)

card_donut = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="categorical_pie_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ], style = {"height": "52vh"}
        ),
    ],
    style = {"background-color": "#16103a"}
)

# TABS

tab_analysis_content = [

    # Categorical Fetaures Visualization

    dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [

                        dbc.Col([
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Categorical Feature", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Gender", "value": "gender"},
                                            {"label": "Partner", "value": "Partner"},
                                            {"label": "Dependents", "value": "Dependents"},
                                            {"label": "Phone Service", "value": "PhoneService"},
                                            {"label": "Multiple Lines", "value": "MultipleLines"},
                                            {"label": "Internet Service", "value": "InternetService"},
                                            {"label": "Online Security", "value": "OnlineSecurity"},
                                            {"label": "Online Backup", "value": "OnlineBackup"},
                                            {"label": "Device Protection", "value": "DeviceProtection"},
                                            {"label": "Tech Support", "value": "TechSupport"},
                                            {"label": "Streaming TV", "value": "StreamingTV"},
                                            {"label": "Streaming Movies", "value": "StreamingMovies"},
                                            {"label": "Contract", "value": "Contract"},
                                            {"label": "Paperless Billing", "value": "PaperlessBilling"},
                                            {"label": "Payment Method", "value": "PaymentMethod"},
                        
                                        ], id = "categorical_dropdown", value="gender"
                                    )
                                ]
                            ),


                            html.Img(src="../assets/customer.png", className="customer-img")
                            
                            
                            ],lg="4", sm=12,
                        ),


                        dbc.Col(card_donut, lg="4", sm=12),

                        # dbc.Spinner(id="loading2",size="md", color="light",children=[dbc.Col(card_categorical, lg="4", sm=12)]),

                        dbc.Col(card_categorical, lg="4", sm=12),

                    ], className="h-15", style={"height": "100%"}
                )
            ]
        ),
        className="mt-3", style = {"background-color": "#272953"}
    ),

    # Tensure, MonthlyCharges and TotalCharges Visualizaion

    dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(card_tensure, lg="4", sm=12),
                        dbc.Col(card_monthlycharges, lg="4", sm=12),
                        dbc.Col(card_totalcharges, lg="4", sm=12),  
                    ], className="h-15"
                )
            ]
        ),
        className="mt-3", style = {"background-color": "#272953"}
    )

]

# PREDICTION

tab_prediction_features = dbc.Card(
    dbc.CardBody(
        [
            # First Row

            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Gender", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Female", "value": "female"},
                                            {"label": "Male", "value": "male"},
                                        ], value="female"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Partner

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Partner", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "yes"},
                                            {"label": "No", "value": "no"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Dependents

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Dependents", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "yes"},
                                            {"label": "No", "value": "no"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # PhoneService

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Phone Service", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "yes"},
                                            {"label": "No", "value": "no"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ), 

            # Second Row

            dbc.Row(
                [
                    # Multiple Lines

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Multiple Lines", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "no"},
                                            {"label": "No phone service", "value": "nps"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Internet Service

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Internet Service", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Fiber optic", "value": "fiberoptic"},
                                            {"label": "DSL", "value": "dsl"},
                                            {"label": "No", "value": "no"},
                                        ], value="fiberoptic"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Online Security

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Online Security", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "no"},
                                            {"label": "No internet service", "value": "nis"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Online Backup

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Online Backup", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "no"},
                                            {"label": "No internet service", "value": "nis"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ),

            # Third Row

            dbc.Row(
                [
                    # Device Protection

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Device Protection", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "no"},
                                            {"label": "No internet service", "value": "nis"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Tech Support

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Tech Support", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "no"},
                                            {"label": "No internet service", "value": "nis"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Streaming TV

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Streaming TV", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "no"},
                                            {"label": "No internet service", "value": "nis"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Streaming Movies

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Streaming Movies", addon_type="prepend"),
                                    dbc.Select(
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "no"},
                                            {"label": "No internet service", "value": "nis"},
                                        ], value="yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ]
            ),
        ]
    ),
    className="mt-3", style = {"background-color": "#272953"}
)

tab_prediction_result = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Button("Predict", size="lg", className="btn-predict")
                        ], lg="4", sm=4, style={"text-align": "center"}, className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("Prediction: Churn"),
                                        html.P("LightGBM")
                                    ]
                                ), className="result-card",
                            )
                        ], lg=4, sm=4, className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("Prediction: Churn"),
                                        html.P("SVM")
                                    ]
                                ), className="result-card",
                            )
                        ], lg=4, sm=4, className="card-padding"
                    )


                ]
            ),


        ]
    ),
    className="mt-3", style = {"background-color": "#272953"}
)

tab_prediction_content =[
    tab_prediction_features,
    tab_prediction_result
]