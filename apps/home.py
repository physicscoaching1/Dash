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


style1 = {'background-color': 'SLATEBLUE', 'border-bottom': '0.5pt solid Blue', 'textAlign': 'center'}
style2 = {'background-color': 'MEDIUMSLATEBLUE', 'border-bottom': '0.5pt solid Blue', 'textAlign': 'center'}
textstyles = {'background-color': 'Lavender', 'textAlign': 'justify'}

StockFundamentals = dcc.Markdown('''
Analyze a stock in **Five Minutes**. Get an estimate of historical and current financial performace of the company.
Know from the finances if the company is enjoying a  "moat", if the company is over leveraged 
and whether the management is prudent with its capital.
Avoid a Satyam like scam by looking into signs of financial manipulations. All in less than five minutes with easy to visaulize charts.
In near future we aim to add the following features
* Stock Valuation
* Insider Trading data
* Bulk Deals and Block Deals
* Annual Statement Ananlysis using Machine Learning and AI
* US equity data
''')

Macro = dcc.Markdown('''
Analyze economic macros in Charts. Study GDP Growth Rates, Inflation, Bond Yeilds, Overall stock Market Valuations

''')

BackTest = dcc.Markdown('''
Site under Developement. Plan to add Backtest features on single stock as well as on a portfolio level with
* Technical Indicators
* Fundamentals
''')




layout = html.Div(children=[
                            html.Br(),
                            html.Br(),
                            html.H4(children='Economic and Stock Market research in Charts', style = style1),
                            html.Div( children=[ html.Div(children=[html.H5('Stocks', style = style2),
                                                                    html.Div(children = StockFundamentals, style = textstyles ),
                                                                     html.Div(dcc.Link('   Stocks   ', href='/FundamentalCharts',className="link"),  className="button"),
                                               #html.H4('GlobalInvestor', style = websitenamestyle)
                                                                   ], className="four columns"),
                            #dcc.Input(id='input', value='', type='text'),
                                                  html.Div(children=[html.H5('Economy and Market Macro', style = style2),
                                                                    html.Div(children = Macro, style = textstyles ),
                                                                     html.Div(dcc.Link('   Macro   ', href='/Macro',className="link"),  className="button"),
                                               #html.H4('GlobalInvestor', style = websitenamestyle)
                                                                   ], className="four columns"),
                                                  html.Div(children=[html.H5('Backtest', style = style2),
                                                                    html.Div(children = BackTest, style = textstyles ),
                                                                     html.Div(dcc.Link('   Backtest   ', href='/Backtest',className="link"),  className="button"),
                                               #html.H4('GlobalInvestor', style = websitenamestyle)
                                                                   ], className="four columns"),
                        #    dcc.Dropdown(
                        #        id='input',
                        #        options=[{'label': i, 'value': i} for i in available_stocks],
                        #        #value='Reliance Industries Limited'
                        #    ),
                                                ], className="row"         
                                     ),
                                            
                            
                            #html.Div('Financial_Charts2'),
                    ])



