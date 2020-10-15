import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import pandas as pd
import joblib
import plotly.express as px
import plotly.figure_factory as ff

import copy

layout = dict(
    autosize=True,
    #automargin=True,
    margin=dict(l=20, r=20, b=20, t=30),
    hovermode="closest",
    plot_bgcolor="#16103a",
    paper_bgcolor="#16103a",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    font_color ="#e0e1e6",
    xaxis_showgrid=False,
    yaxis_showgrid=False
)

# Model Read
svm_path = 'data/svm_model.sav'
svm_model = joblib.load(svm_path)

xgb_path = 'data/xgb_model.sav'
xgb_model = joblib.load(xgb_path)

# Data Read
df = pd.read_csv('data/Telco-Customer-Churn.csv')
df['TotalCharges'] = df['TotalCharges'].replace(" ", 0).astype('float32')

cat_features = df.drop(['customerID','TotalCharges', 'MonthlyCharges', 'SeniorCitizen', 'tenure', 'Churn'],axis=1).columns

# Encoding categorical features
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)
ohe.fit(df[cat_features])


def dist_tenure():
    x1 = df[df['Churn'] == 'No']['tenure']
    x2 = df[df['Churn'] == 'Yes']['tenure']
    
    
    
    fig = ff.create_distplot([x1,x2], group_labels= ['No', 'Yes'],
                             bin_size=3,
                             curve_type='kde',
                             show_rug=False,
                             show_hist=False,
                             show_curve=True,
                             colors=['#47acb1','#f26522'])
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': 'KDE of Tenures', 'x': 0.5},
        legend = {'x': 0.25}
    )
    
    return fig


def dist_monthlycharges():
    x1 = df[df['Churn'] == 'No']['MonthlyCharges']
    x2 = df[df['Churn'] == 'Yes']['MonthlyCharges']
    
    
    
    fig = ff.create_distplot([x1,x2], group_labels= ['No', 'Yes'],
                             bin_size=3,
                             curve_type='kde',
                             show_rug=False,
                             show_hist=False,
                             show_curve=True,
                             colors=['#47acb1','#f26522'])
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': 'KDE of Monthly Charges', 'x': 0.5},
        legend = {'x': 0.25}
        
    )
    
    return fig

def dist_totalcharges():
    x1 = df[df['Churn'] == 'No']['TotalCharges']
    x2 = df[df['Churn'] == 'Yes']['TotalCharges']
    
    
    
    fig = ff.create_distplot([x1,x2], group_labels= ['No', 'Yes'],
                             bin_size=3,
                             curve_type='kde',
                             show_rug=False,
                             show_hist=False,
                             show_curve=True,
                             colors=['#47acb1','#f26522'])
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': 'KDE of Total Charges', 'x': 0.5},
        legend = {'x': 0.25}
    )
    
    return fig
