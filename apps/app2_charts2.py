import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import os

from app import app

path=r'C:\Users\achowdhury143777\OneDrive - Applied Materials\scripts\NSE_STOCKLIST'
#path=r'/home/abhishek_iitkgp/stocklist'
stocklistfilename  = 'EQUITY_L_NSE.csv'
errorfilename= 'error2.csv'
stocklist = pd.read_csv(os.path.join(path,stocklistfilename), usecols=['SYMBOL', 'NAME OF COMPANY'], encoding='latin1' )

available_stocks = stocklist['NAME OF COMPANY']


layout = html.Div([
    html.H3('Site Under developement'),
    html.Div(children='''
        Company Name to Backtest:
    '''),
    dcc.Dropdown(
        id='input',
        options=[{'label': i, 'value': i} for i in available_stocks],
        #value='Reliance Industries Limited'
    ),
    html.Div(id='app-2-display-value'),
])


@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('input', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)