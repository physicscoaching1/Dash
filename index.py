import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from apps import app1_charts1, app2_charts2, home, macro

#%%
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
    })

#buttonstyle = {'textAlign': 'center', 'background-color': '#0275d8', 'border': 'none', 'font-size': '110%'}
#dcclinkstyle = {'color': 'Black', 'text-decoration':'none'}
buttonstyle = {'textAlign': 'right'}
Headerstyle = { 'border-bottom': '1pt solid Black'}
WebsiteNamestyle = {'font-family': 'Times New Roman', 'font-size': '150%'}


#%%


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
            html.Div(children=[html.Div('Global Investor'),
                       #html.H4('GlobalInvestor', style = websitenamestyle)
                      ], className="six columns", style = WebsiteNamestyle),
            html.Div([
                html.Div(dcc.Link('   Home   ', href='/',  className="link"), className = "button"),
                html.Div(dcc.Link('   Stocks   ', href='/FundamentalCharts',className="link"),  className="button"),
                html.Div(dcc.Link('   Macro   ', href='/Macro',className="link"),  className="button"),
                html.Div(dcc.Link('   Backtest   ', href='/Backtest', className="link"),  className="button"),

                    ], className="six columns", style = buttonstyle),
            ], style = Headerstyle, className="row"),

                        #html.Br(),
    html.Div(id='page-content', className="row")
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return home.layout
    if pathname == '/FundamentalCharts':
         return app1_charts1.layout
    elif pathname == '/Backtest':
         return app2_charts2.layout
    elif pathname == '/Macro':
         return macro.layout
    else:
        return 'Incorrect URL. Please enter correct URL or go to home'

if __name__ == '__main__':
    app.run_server(debug=True)