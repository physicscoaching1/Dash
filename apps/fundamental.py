from app import app, server

import pandas as pd
import time
import os
import warnings
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
from datetime import date
#import pandas_datareader.data as web
from dash.dependencies import Input, Output
from nsepy import get_history

#%%
#import pandas_datareader.data as web
#import datetime
#start = datetime.datetime(2015, 1, 1)
#end = datetime.datetime(2015, 1, 10)
#symbol = 'WIKI/AAPL'
##df = web.DataReader(symbol, 'quandl', start, end)
#df = web.DataReader(symbol, 'quandl', '2015-01-01', '2015-01-05')
#
#import quandl
#quandl.ApiConfig.api_key = 'bmKnz8-auKYXhjysAj6z'
#data = quandl.get('NSE/BOROSIL', start_date='2018-05-25', end_date='2018-05-25')

#from datetime import date
#from nsepy import get_history
#
#end = date.today()
#start = end - datetime.timedelta(days=3*365)
#sbin = get_history(symbol='SBIN',
#                   start=start,
#                   end=end)
#%%
cwd = os.getcwd()
oneupdirectory = os.path.dirname(cwd)
twoupdirectory = os.path.dirname(oneupdirectory)

path = oneupdirectory
stockdatapath = os.path.join(oneupdirectory, 'screener', 'data', 'Annual')
TTMpath = os.path.join(oneupdirectory, 'screener', 'data', 'TTM')

#%%


style1 = {'background-color': 'Lavender', 'border-bottom': '0.5pt solid Blue', 'textAlign': 'center'}
style2 = {'textAlign': 'right'}



#path=r'C:\Users\achowdhury143777\OneDrive - Applied Materials\scripts\NSE_STOCKLIST'
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
                                            
                            
                            html.Div(id='Fundamental_Charts'),
                    ])

@app.callback(
    Output(component_id='Fundamental_Charts', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def Profitability_Graph(input_data):

    nsesymbol = stocklist[stocklist['NAME OF COMPANY']==input_data]['SYMBOL'].iloc[0]
          
    stockdatafilename = nsesymbol + '.csv'
    
    stockdata = pd.read_csv(os.path.join(stockdatapath,stockdatafilename), index_col = 0, parse_dates = True)
    TTMdata = pd.read_csv(os.path.join(TTMpath,stockdatafilename), usecols=['Stock P/E', 'Market Cap.', 'PEG Ratio', 'Dividend Yield', 'Promoter holding', 'Pledged percentage', 'Change in promoter holding', 'Change in promoter holding 3Years'])
    
    
    stockdata.index = stockdata.index.date
    
    
    #code for the price data
#    end = date.today()
#    start = end - datetime.timedelta(days=3*365)
#    pricestockdata = get_history(symbol=nsesymbol,
#                   start=start,
#                   end=end)
#    
#    pricestockdata['200MA'] = pricestockdata['Close'].rolling(200).mean()
#    pricestockdata['50MA'] = pricestockdata['Close'].rolling(50).mean()

    return html.Div(children = [
            

     
#            dcc.Graph(
#                id='Price_Chart',
#                figure={
#                    'data': [
#                                {'x': pricestockdata.index, 'y': pricestockdata['Close'], 'type': 'line', 'name': 'Close'},
#                                {'x': pricestockdata.index, 'y': pricestockdata['200MA'], 'type': 'line', 'name': '200 day MA'},
#                                {'x': pricestockdata.index, 'y': pricestockdata['50MA'], 'type': 'line', 'name': '50 Day MA'},
#                            ],
#                    'layout': {
#                        'title': 'Price Action'
#                              }
#                    
#                        }
#                    ),
            html.Br(),
            html.Br(),
            html.H5(children=input_data, style = style1),
            html.Br(),
            html.Br(),
            
    
             html.Div(children=[html.Div(children=[ dcc.Graph(
                                                            id='Stock_PE',
                                                            figure={
                                                                'data': [
                                                                            {'x': ['Stock PE'], 'y': TTMdata['Stock P/E'], 'type': 'bar', 'name': 'Stock PE'},

                                                                        ],
                                                                'layout': {
                                                                    'title': 'Stock P_E'
                                                                          }
                                                                
                                                                    }
                                                                ),
                                                   ], className="three columns"),

                                     html.Div(children=[ dcc.Graph(
                                                            id='MarketCap',
                                                            figure={
                                                                'data': [
                                                                            {'x': ['Market Cap'], 'y': TTMdata['Market Cap.'], 'type': 'bar', 'name': 'Market Cap-Crore'},

                                                                        ],
                                                                'layout': {
                                                                    'title': 'Market Cap-Crore'
                                                                          }
                                                                
                                                                    }
                                                                ),
                                                   ], className="three columns"),

                                     html.Div(children=[ dcc.Graph(
                                                            id='PEG',
                                                            figure={
                                                                'data': [
                                                                            {'x': ['PEG'], 'y': TTMdata['PEG Ratio'], 'type': 'bar', 'name': 'PEG'},

                                                                        ],
                                                                'layout': {
                                                                    'title': 'PEG Ratio'
                                                                          }
                                                                
                                                                    }
                                                                ),
                                                   ], className="three columns"),

                                     html.Div(children=[ dcc.Graph(
                                                            id='DividendYield',
                                                            figure={
                                                                'data': [
                                                                            {'x': ['Dividend Yield'], 'y': TTMdata['Dividend Yield'], 'type': 'bar', 'name': 'Dividend Yield'},

                                                                        ],
                                                                'layout': {
                                                                    'title': 'Dividend Yield'
                                                                          }
                                                                
                                                                    }
                                                                ),
                               #html.H4('GlobalInvestor', style = websitenamestyle)
                                                   ], className="three columns"),   
                                ], className="row"
                    ),
    
             html.Div(children=[html.Div(children=[ dcc.Graph(
                                                            id='PromotorHolding',
                                                            figure={
                                                                'data': [
                                                                            {'x': ['Promoter holding'], 'y': TTMdata['Promoter holding'], 'type': 'bar', 'name': 'Promoter holding'},

                                                                        ],
                                                                'layout': {
                                                                    'title': 'Promoter Holding Percentage'
                                                                          }
                                                                
                                                                    }
                                                                ),
                                                   ], className="three columns"),

                                     html.Div(children=[ dcc.Graph(
                                                            id='Pledgedpercentage',
                                                            figure={
                                                                'data': [
                                                                            {'x': ['Pledged Percentage'], 'y': TTMdata['Pledged percentage'], 'type': 'bar', 'name': 'Pledged percentage'},

                                                                        ],
                                                                'layout': {
                                                                    'title': 'Pledged Percentage'
                                                                          }
                                                                
                                                                    }
                                                                ),
                                                   ], className="three columns"),

                                     html.Div(children=[ dcc.Graph(
                                                            id='Changeinpromoterholding',
                                                            figure={
                                                                'data': [
                                                                            {'x': ['Change in Promoter Holding- 1 year'], 'y': TTMdata['Change in promoter holding'], 'type': 'bar', 'name': 'Change in promoter holding'},

                                                                        ],
                                                                'layout': {
                                                                    'title': 'Change in Promoter Holding- 1 year'
                                                                          }
                                                                
                                                                    }
                                                                ),
                                                   ], className="three columns"),

                                     html.Div(children=[ dcc.Graph(
                                                            id='Change_in_promoter_holding_3Years',
                                                            figure={
                                                                'data': [
                                                                            {'x': ['Change in Promoter Holding-3Years'], 'y': TTMdata['Change in promoter holding 3Years'], 'type': 'bar', 'name': 'Change in promoter holding 3Years'},

                                                                        ],
                                                                'layout': {
                                                                    'title': 'Change in Promoter Holding-3Years:'
                                                                          }
                                                                
                                                                    }
                                                                ),
                               #html.H4('GlobalInvestor', style = websitenamestyle)
                                                   ], className="three columns"),   
                                ], className="row"
                    ),
            
            
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
                id='EPS_Growth_Rate',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['EPS Growth'], 'type': 'line', 'name': 'EPS Growth'},
                    ],
                    'layout': {
                        'title': 'EPS Growth Rate'
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
                id='InterestCoverageRatio',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Interest Coverage Ratio'], 'type': 'line', 'name': 'Interest Coverage Ratio'},
                    ],
                    'layout': {
                        'title': 'Interest Coverage Ratio'
                    }
                    
                }
            ),
    
            dcc.Graph(
                id='LeverageRatio',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Financial Leverage Ratio'], 'type': 'line', 'name': 'Financial Leverage Ratio'},
                    ],
                    'layout': {
                        'title': 'Financial Leverage Ratio'
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
                id='Fixed_Asset_Sales_Ratio',
                figure={
                    'data': [
                        {'x': stockdata.index, 'y': stockdata['Fixed Asset Sales Ratio'], 'type': 'line', 'name': 'Fixed Asset Sales Ratio'},
                    ],
                    'layout': {
                        'title': 'Fixed Asset Sales Ratio'
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
