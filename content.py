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

tab_graphs = [

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
                                                {"label": "Senior Citizen", "value": "SeniorCitizen"},
                            
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

tab_analysis_content = tab_graphs


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
                                        id="ft_gender",
                                        options=[
                                            {"label": "Female", "value": "Female"},
                                            {"label": "Male", "value": "Male"},
                                        ], value="Male"
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
                                        id="ft_partner",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ], value="Yes"
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
                                        id="ft_dependents",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ], value="No"
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
                                        id="ft_phoneService",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ], value="Yes"
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
                                        id="ft_multipleLines",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No phone service", "value": "No phone service"},
                                        ], value="Yes"
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
                                        id="ft_internetService",
                                        options=[
                                            {"label": "Fiber optic", "value": "Fiber optic"},
                                            {"label": "DSL", "value": "DSL"},
                                            {"label": "No", "value": "No"},
                                        ], value="Fiber optic"
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
                                        id="ft_onlineSecurity",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
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
                                        id="ft_onlineBackup",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
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
                                        id="ft_deviceProtection",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
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
                                        id="ft_techSupport",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
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
                                        id="ft_streamingTv",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
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
                                        id="ft_streamingMovies",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ),

            # Fourth Row

            dbc.Row(
                [
                    # Contract

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Contract", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_contract",
                                        options=[
                                            {"label": "Month-to-month", "value": "Month-to-month"},
                                            {"label": "One year", "value": "One year"},
                                            {"label": "Two year", "value": "Two year"},
                                        ], value="Month-to-month"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),


                    # PaperlessBilling

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Paperless Billing", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_paperlessBilling",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ], value="Yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),


                    # PaymentMethod

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Payment Method", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_paymentMethod",
                                        options=[
                                            {"label": "Electronic check", "value": "Electronic check"},
                                            {"label": "Mailed check", "value": "Mailed check"},
                                            {"label": "Bank transfer (automatic)", "value": "Bank transfer (automatic)"},
                                            {"label": "Credit card (automatic)", "value": "Credit card (automatic)"}
                                        ], value="Mailed check"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # SeniorCitizen

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Senior Citizen", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_seniorCitizen",
                                        options=[
                                            {"label": "Yes", "value": "1"},
                                            {"label": "No", "value": "0"}
                                        ], value="1"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),
                ], className="feature-row",
            ),

            # Fifth Row

            dbc.Row(
                [
                    # MonhtlyCharges

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Monhtly Charges ($)", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_monthlyCharges",
                                        placeholder="Amount", type="number", value="74.4"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Total Charges

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Total Charges ($)", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_totalCharges",
                                        placeholder="Amount", type="number", value="306.6"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Tenure

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Tenure", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_tenure",
                                        placeholder="Amount", type="number", value="4"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),
                ]
            )
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
                            dbc.Button("Predict", id='btn_predict', size="lg", className="btn-predict")
                        ], lg="4", sm=4, style={"display": "flex", "align-items":"center", "justify-content":"center"},
                        className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dbc.Spinner(html.H4(id="xgb_result", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                                        html.P("XGBoost")
                                    ]
                                ), className="result-card", style={"height":"16vh"}
                            )
                        ], lg=4, sm=4, className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dbc.Spinner(html.H4(id="svm_result", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                                        html.P("SVM")
                                    ]
                                ), className="result-card", style={"height":"16vh"}
                            )
                        ], lg=4, sm=4, className="card-padding"
                    )


                ]
            ),


        ]
    ),
    className="mt-3", style = {"background-color": "#272953"}
)

tab_prediction_content = [
    
    tab_prediction_features,
    tab_prediction_result
    
]