from app import app, server

import pandas as pd
import time
import os
import warnings
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
#import pandas_datareader.data as web
from dash.dependencies import Input, Output


style1 = {'background-color': 'Lavender', 'border-bottom': '0.5pt solid Blue', 'textAlign': 'center'}
style2 = {'textAlign': 'right'}



path=r'C:\Users\achowdhury143777\OneDrive - Applied Materials\scripts\NSE_STOCKLIST'
#path=r'/home/abhishek_iitkgp/stocklist'
stocklistfilename  = 'EQUITY_L_NSE.csv'
errorfilename= 'error2.csv'
stocklist = pd.read_csv(os.path.join(path,stocklistfilename), usecols=['SYMBOL', 'NAME OF COMPANY'], encoding='latin1' )

available_stocks = stocklist['NAME OF COMPANY']



layout = html.Div(children=[
                            html.Br(),
                            html.Br(),
                            html.H4(children='Fundamental Analysis of Stocks in Charts', style = style1),
                            html.Div( children=[ html.Div(children=[html.H5('Select Stock:', style = style2),
                                               #html.H4('GlobalInvestor', style = websitenamestyle)
                                                                   ], className="three columns"),
                            #dcc.Input(id='input', value='', type='text'),
                                                 html.Div(children=[ dcc.Dropdown(
                                                                                    id='input',
                                                                                    options=[{'label': i, 'value': i} for i in available_stocks],
                                                                                    #value='Reliance Industries Limited'
                                                                                  ),
                                               #html.H4('GlobalInvestor', style = websitenamestyle)
                                                                   ], className="six columns"),
                        #    dcc.Dropdown(
                        #        id='input',
                        #        options=[{'label': i, 'value': i} for i in available_stocks],
                        #        #value='Reliance Industries Limited'
                        #    ),
                                                ], className="row"         
                                     ),
                                            
                            
                            html.Div(id='Financial_Charts2'),
                    ])

@app.callback(
    Output(component_id='Financial_Charts2', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def Profitability_Graph(input_data):

    nsesymbol = stocklist[stocklist['NAME OF COMPANY']==input_data]['SYMBOL'].iloc[0]
    
    stockdatapath = r'C:\Users\achowdhury143777\OneDrive - Applied Materials\scripts\Fundamental\ScreenerFundamental_Annual'
    #stockdatapath = r'/home/abhishek_iitkgp/data/screener/Annual'
    
    
    stockdatafilename = nsesymbol + '.csv'
    
    stockdata = pd.read_csv(os.path.join(stockdatapath,stockdatafilename), index_col = 0, parse_dates = True)
    
    stockdata.index = stockdata.index.date

    return html.Div(children = [
            dcc.Graph(
                id='Growth_Rates',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['YOY Sales Growth'], 'type': 'line', 'name': 'Sales Growth Rate'},
                        {'x': stockdata.index, 'y': stockdata['YOY Op Profit Growth'], 'type': 'line', 'name': 'Op Profit Growth Rate'},
                        {'x': stockdata.index, 'y': stockdata['YOY Net Profit Growth'], 'type': 'line', 'name': 'Net Profit Growth Rate'},
                    ],
                    'layout': {
                        'title': 'Growth Rates'
                    }
                    
                }
            ),
            dcc.Graph(
                id='Profit_Margin',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['OPM'], 'type': 'line', 'name': 'OPM'},
                        {'x': stockdata.index, 'y': stockdata['NPM'], 'type': 'line', 'name': 'NPM'},
                    ],
                    'layout': {
                        'title': 'Profit Margin'
                    }
                    
                }
            ),
            dcc.Graph(
                id='Buisness_Strength_Return Ratios',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Return on Equity'], 'type': 'line', 'name': 'Return on Equity'},
                        {'x': stockdata.index, 'y': stockdata['Return on Capital Employed'], 'type': 'line', 'name': 'Return on Capital Employed'},
                    ],
                    'layout': {
                        'title': 'Buisness Strength-Return Ratios'
                    }
                    
                }
            ),
            html.Div("The real measure of a moat is whether a company can consistently generate returns (ROCEs) above the cost of capital. In the end, it boils down to value creation over a long period of time", style = style1),
            
            dcc.Graph(
                id='Borrowings',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Borrowings'], 'type': 'line', 'name': 'Borrowings'},
                    ],
                    'layout': {
                        'title': 'Borrowings'
                    }
                    
                }
            ),
    
            dcc.Graph(
                id='DebttoEquity',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Debt to Equity Ratio'], 'type': 'line', 'name': 'Debt to Equity Ratio'},
                    ],
                    'layout': {
                        'title': 'Debt to Equity Ratio'
                    }
                    
                }
            ),
            
            dcc.Graph(
                id='Dividend_Payout',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Dividend Payout'], 'type': 'line', 'name': 'Dividend Payout'},
                    ],
                    'layout': {
                        'title': 'Dividend Payout Percentage'
                    }
                    
                }
            ),
            dcc.Graph(
                id='Tax_Rate',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Tax Rate'], 'type': 'line', 'name': 'Tax Rate'},
                    ],
                    'layout': {
                        'title': 'Detect Fiancial Manipulation 1_Tax Rate'
                    }
                    
                }
            ),
            dcc.Graph(
                id='CScore_1',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Receivables Sales Ratio'], 'type': 'line', 'name': 'Receivables Sales Ratio'},
                        {'x': stockdata.index, 'y': stockdata['Inventory Sales Ratio'], 'type': 'line', 'name': 'Inventory Sales Ratio'},
                    ],
                    'layout': {
                        'title': 'Detect Fiancial Manipulation 2_Receivables and Inventory'
                    }
                    
                }
            ),
            dcc.Graph(
                id='CScore_2',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Depreciation to Fixed Assets'], 'type': 'line', 'name': 'Depreciation to Fixed Assets'},
                        {'x': stockdata.index, 'y': stockdata['Depreciation to Gross Fixed Assets'], 'type': 'line', 'name': 'Depreciation to Gross Fixed Assets'},
                    ],
                    'layout': {
                        'title': 'Detect Fiancial Manipulation 3_Depreciation'
                    }
                    
                }
            ),
            dcc.Graph(
                id='Operating_Cash_Flow_to_Net_Profit',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Operating Cash Flow to Net Profit'], 'type': 'line', 'name': 'Operating Cash Flow to Net Profit'},
                    ],
                    'layout': {
                        'title': 'Operating Cash Flow to Net Profit'
                    }
                    
                }
            )
    ]
    )   

if __name__ == '__main__':
    #for local
    app.run_server(debug=True)
    #for server
    #app.run_server(host='0.0.0.0', debug=True)

