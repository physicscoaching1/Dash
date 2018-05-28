import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from apps import app1_charts1, app2_charts2

#%%

tabstyle = {'background-color': '#0275d8', 'border-bottom': '1pt solid Blue', 'width': '48%', 'display': 'inline-block'}
websitenamestyle = {'color': 'Black', 'background-color': '#0275d8', 'font-size': '170%', 'border-bottom': '1pt solid Blue', 'width': '48%', 'display': 'inline-block' }
#buttonstyle = {'textAlign': 'center', 'font-size': '100%', 'background-color': 'DodgerBlue' , 'border': '2pt solid Black'}
#buttonstyle = {'textAlign': 'center', 'background-color': 'DodgerBlue'}
buttonstyle = {'textAlign': 'center', 'background-color': '#0275d8', 'border': 'none', 'font-size': '110%'}
dcclinkstyle = {'color': 'Black', 'text-decoration':'none'}
#dcclinkstyle = {'color': 'White', 'text-decoration':'none'}

#%%


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(children=[html.Div('GlobalInvestor'),
                       #html.H4('GlobalInvestor', style = websitenamestyle)
                      ], style = websitenamestyle),
    html.Div([
        html.Button(dcc.Link('   Home   ', href='/', style = dcclinkstyle ), style = buttonstyle),
        html.Button(dcc.Link('   Fundamental Charts   ', href='/FundamentalCharts', style = dcclinkstyle ), style = buttonstyle),
        html.Button(dcc.Link('   Backtest   ', href='/Backtest', style = dcclinkstyle ), style = buttonstyle),

    ], style = tabstyle),
    #html.Br(),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return "Home"
    if pathname == '/FundamentalCharts':
         return app1_charts1.layout
    elif pathname == '/Backtest':
         return app2_charts2.layout
    else:
        return 'Incorrect URL. Please enter correct URL or go to home'

if __name__ == '__main__':
    app.run_server(debug=True)