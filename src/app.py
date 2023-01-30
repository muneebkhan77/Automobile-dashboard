# Import required packages
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update




auto_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})


app = dash.Dash()
app.config.suppress_callback_exceptions = True
server = app.server


                            
app.layout=html.Div(children=[ html.H1("Car Automobile Components", style={'textAlign':'center', 'color': '#503D36', 'font-size':24}),

    html.Div([
        html.Div( html.H2('Drive Wheels Type:', style={'margin-right':'2em'}),

        ),

        dcc.Dropdown(id='demo-dropdown', options=[
            {'label':'Rear Wheel Drive', 'value' : 'rwd'},
            {'label':'Front Wheel Drive', 'value': 'fwd'},
            {'label':'Four Wheel Drive', 'value' : '4wd'},
        ],
        value='rwd'
        ),

        ]),
        html.Div([  
            html.Div([], id='plot1'),
            html.Div([ ], id='plot2')


        ],style={'display':'flex'}),


    ])
    
@app.callback([Output(component_id='plot1', component_property='children'),
                Output(component_id='plot2', component_property='children')
]  ,   
Input(component_id='demo-dropdown', component_property='value'))

def display_selected_drive_charts(value):
    filtered_df=auto_data[auto_data['drive-wheels']==value].groupby(['drive-wheels','body-style'],
    as_index=False).mean()
    filtered_df=filtered_df
    fig1=px.pie(filtered_df, values='price',names='body-style', title="pie chart")
    fig2=px.bar(filtered_df, y='price', x='body-style', title="bar chart")

    return[dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)]

# Run Application
if __name__ == '__main__':
    app.run_server()