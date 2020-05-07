# main module of the program
# result of the executing is a web-app
from modules.adt_weather_data import WeatherData
import urllib.request
import urllib.parse
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
import pandas

# getting and preparing data
BASE_URL = "https://api.nasa.gov/insight_weather/?api_key=aNnXcB7VnzSnzQVmBRriouUeGJUSblCeD7Pwr4Id&feedtype=json&ver=1.0"


# a demo_key is used for defending private information,
# if needed, it can be replaced by a developer key from NASA API website
# https://api.nasa.gov


def get_data_from_url(base_url):
    with urllib.request.urlopen(base_url) as response:
        data = response.read()
        data = data.decode("utf-8")
        data = json.loads(data)
    return data


json_data = get_data_from_url(BASE_URL)

week_weather = WeatherData(json_data)


# functions for creating visual elements
# return a table with data for one day
def make_day_table(n):
    day = week_weather.day(n)
    fig = go.Figure(data=[go.Table(
        header=dict(values=['MARTIAN DAY {}'.format(day[0])], line_color='DarkOrange',
                    fill_color='PeachPuff',
                    height=40,
                    font=dict(family='Courier New, monospace', color='DarkOrange', size=32)),
        cells=dict(values=[['Average temperature: {}'.format(day[1]),
                            'Average wind speed: {}'.format(day[2]),
                            'Average pressure: {}'.format(day[3])], ], line_color='DarkOrange',
                   fill_color='OldLace', align='left', height=40,
                   font=dict(family='Courier New, monospace', color='grey', size=23))),
    ])
    fig.update_layout(layout)
    return fig


# return the wind rose
def make_wind_rose(n):
    day_wind_rose = week_weather.wind_rose(n)
    lst = day_wind_rose.head().item
    t = day_wind_rose.head().next
    fig = go.Figure(go.Barpolar(r=[i for i in lst],
                                theta=[i for i in t],
                                marker_color=['coral'] * len(lst),
                                ))
    fig.update_layout(
        template='plotly_dark',
        autosize=False,
        width=500,
        height=450,
        title='Wind Direction Distribution',
        font={'size': 16},
        title_x=0.5,
    )
    fig.update_layout(layout)
    return fig


# return the line graph
def make_trace_graph(data, name):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in week_weather.days_list()], y=[i for i in data],
                             mode='lines',
                             name='lines'))
    fig.update_layout(layout)
    fig.update_layout(title=name, template='plotly_dark', font={'size': 16}, height=380,
                      )
    return fig


# main part
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'url(assets/reset.css)']

layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})
app.layout = html.Div(
    [html.H1(children='MARTIAN WEATHER PROJECT', style={
        'textAlign': 'center', 'color': 'white',
        'text-shadow': '0 0 20px #fff, 0 0 30px coral, 0 0 40px coral, '
                       '0 0 50px coral, 0 0 60px coral, 0 0 70px coral, 0 0 80px coral'}),


     html.H4('Select one Sol (Martian day):', style={"white-space": "pre", 'color': 'white',
                                                     'text-shadow': '0 0 20px #fff, 0 0 30px coral, 0 0 40px coral'}),
     dcc.Tabs(id='tabs-example', value='tab-1', children=[
         dcc.Tab(label='{}'.format(week_weather.days_list()[0]), value='tab-1', style={'color': 'DarkOrange'},
                 selected_style={
                     'backgroundColor': 'OldLace',
                     'color': 'grey',
                 }),
         dcc.Tab(label='{}'.format(week_weather.days_list()[1]), value='tab-2', style={'color': 'DarkOrange'},
                 selected_style={
                     'backgroundColor': 'OldLace',
                     'color': 'grey',
                 }),
         dcc.Tab(label='{}'.format(week_weather.days_list()[2]), value='tab-3', style={'color': 'DarkOrange'},
                 selected_style={
                     'backgroundColor': 'OldLace',
                     'color': 'grey',
                 }),
         dcc.Tab(label='{}'.format(week_weather.days_list()[3]), value='tab-4', style={'color': 'DarkOrange'},
                 selected_style={
                     'backgroundColor': 'OldLace',
                     'color': 'grey',
                 }),
         dcc.Tab(label='{}'.format(week_weather.days_list()[4]), value='tab-5', style={'color': 'DarkOrange'},
                 selected_style={
                     'backgroundColor': 'OldLace',
                     'color': 'grey',
                 }),
         dcc.Tab(label='{}'.format(week_weather.days_list()[5]), value='tab-6', style={'color': 'DarkOrange'},
                 selected_style={
                     'backgroundColor': 'OldLace',
                     'color': 'grey',
                 }),
         dcc.Tab(label='{}'.format(week_weather.days_list()[6]), value='tab-7', style={'color': 'DarkOrange'},
                 selected_style={
                     'backgroundColor': 'OldLace',
                     'color': 'grey',
                 }),

     ], colors={
         "border": "OldLace",
         "primary": "gold",
         "background": "PeachPuff"
     }, style={'width': '500px'}),
     html.Div(id='tabs-example-content'),
     dcc.Markdown('''
         ###### Welcome to Martian Weather Project! Here you can check latest weather tendencies on the planet Mars. 
         ###### The project uses NASA's InSight: Mars Weather Service API in order to obtain the most recent information.
         ###### For more information about the weather have a look these graphic:
     ''', style={'color': 'white'}),
     dcc.Markdown('.', style={"white-space": "pre", 'color': 'black'}),
     html.Div([html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.min_temp(), 'Minimum temperature through the week:'),
    )),
     html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.max_temp(), 'Maximum temperature through the week:'),
     )),]),
     html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.av_temp(), 'Average temperature through the week:'),
     )),
     html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.min_pres(), 'Minimum pressure through the week:'),
     )),
     html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.max_pres(), 'Maximum pressure through the week:'),
     )),
     html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.av_pres(), 'Average pressure through the week:'),
     )),
     html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.min_speed(), 'Minimum wind speed through the week:'),
     )),
     html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.min_temp(), 'Maximum wind speed through the week:'),
     )),
     html.Div(dcc.Graph(
         figure=make_trace_graph(week_weather.min_temp(), 'Average wind speed through the week:'),
     )),
     ],
    style={'background-image': 'url("assets/mars.jpg")', 'bottom': '0', 'right': '0', 'left': '0',
           'top': '0'}
)


@app.callback(Output('tabs-example-content', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div(dcc.Graph(
                figure=make_day_table(0),
                style={'width': 500, 'left': 0}), style={'display': 'inline-block'}, ),
            html.Div(dcc.Graph(figure=make_wind_rose(0), style={'left': 100}), style={'display': 'inline-block'}, )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.Div(dcc.Graph(
                figure=make_day_table(1),
                style={'width': 500, 'left': 0}), style={'display': 'inline-block'}, ),
            html.Div(dcc.Graph(figure=make_wind_rose(1), style={'left': 100}), style={'display': 'inline-block'}, )
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.Div(dcc.Graph(
                figure=make_day_table(2),
                style={'width': 500, 'left': 0}), style={'display': 'inline-block'}, ),
            html.Div(dcc.Graph(figure=make_wind_rose(2), style={'left': 100}), style={'display': 'inline-block'}, )
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.Div(dcc.Graph(
                figure=make_day_table(3),
                style={'width': 500, 'left': 0}), style={'display': 'inline-block'}, ),
            html.Div(dcc.Graph(figure=make_wind_rose(3), style={'left': 100}), style={'display': 'inline-block'}, )
        ])
    elif tab == 'tab-5':
        return html.Div([
            html.Div(dcc.Graph(
                figure=make_day_table(4),
                style={'width': 500, 'left': 0}), style={'display': 'inline-block'}, ),
            html.Div(dcc.Graph(figure=make_wind_rose(4), style={'left': 100}), style={'display': 'inline-block'}, )
        ])
    elif tab == 'tab-6':
        return html.Div([
            html.Div(dcc.Graph(
                figure=make_day_table(5),
                style={'width': 500, 'left': 0}), style={'display': 'inline-block'}, ),
            html.Div(dcc.Graph(figure=make_wind_rose(5), style={'left': 100}), style={'display': 'inline-block'}, )
        ])
    elif tab == 'tab-7':
        return html.Div([
            html.Div(dcc.Graph(
                figure=make_day_table(6),
                style={'width': 500, 'left': 0}), style={'display': 'inline-block'}, ),
            html.Div(dcc.Graph(figure=make_wind_rose(6), style={'left': 100}), style={'display': 'inline-block'}, )
        ])


server = app.server
dev_server = app.run_server

# run the program
if __name__ == '__main__':
    app.run_server(debug=True)
