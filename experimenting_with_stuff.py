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

with open('NASA_example_data.txt') as file:
    json_data = json.load(file)
# BASE_URL = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
#
#
# def get_data_from_URL(base_url):
#     with urllib.request.urlopen(base_url) as response:
#         data = response.read()
#         data = data.decode("utf-8")
#         data = json.loads(data)
#     return data
#
#
# json_data = get_data_from_URL(BASE_URL)

dict_with_day_data = dict()

for key in json_data.keys():
    if key in json_data['sol_keys']:
        dict_with_day_data[key] = json_data[key]

average_temperature = []
average_wind_speed = []
average_pressure = []
seasons = []
days = json_data['sol_keys']

for key in dict_with_day_data.keys():
    average_temperature.append(dict_with_day_data[key]['AT']['av'])
    average_wind_speed.append(dict_with_day_data[key]['HWS']['av'])
    average_pressure.append(dict_with_day_data[key]['PRE']['av'])
    seasons.append(dict_with_day_data[key]['Season'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'url(assets/reset.css)']

layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)


def make_day_table(day):
    fig = go.Figure(data=[go.Table(
        header=dict(values=['MARTIAN DAY {}'.format(days[day])], line_color='DarkOrange', fill_color='PeachPuff',
                    height=40,
                    font=dict(family='Courier New, monospace', color='DarkOrange', size=32)),
        cells=dict(values=[['Average temperature: {}'.format(average_temperature[day]),
                            'Average wind speed: {}'.format(average_wind_speed[day]),
                            'Average pressure: {}'.format(average_pressure[day])], ], line_color='DarkOrange',
                   fill_color='OldLace', align='left', height=40,
                   font=dict(family='Courier New, monospace', color='grey', size=23))),
    ], layout=layout)
    return fig


def make_wind_rose(day):
    data = dict_with_day_data[days[day]]['WD']
    df = pandas.DataFrame(data)
    lst = [i for i in df.iloc[4]][:-1]
    t = [i for i in df.iloc[0]][:-1]
    print(lst, t)
    fig = go.Figure(go.Barpolar(r=lst,
                                theta=t,
                                marker_color=['coral'] * len(lst),
                                ))
    fig.update_layout(layout)
    fig.update_layout(
        template='plotly_dark',
        autosize=False,
        width=500,
        height=450,
        title='Wind Direction Distribution',
        font={'size': 16},
        title_x=0.5,
    )
    return fig


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})
app.layout = html.Div(
    [html.H1(children='MARTIAN WEATHER PROJECT', style={
        'textAlign': 'center', 'color': 'white',
        'text-shadow': '0 0 20px #fff, 0 0 30px coral, 0 0 40px coral, '
                       '0 0 50px coral, 0 0 60px coral, 0 0 70px coral, 0 0 80px coral'}),

     html.Div(children=['''
         Welcome to Martian Weather Project! Here you can check latest weather tendencies on the planet Mars.
     '''], style={'color': 'white', 'text-shadow': '0 0 20px #fff, 0 0 30px coral, 0 0 40px coral'}),
     dcc.Markdown('.', style={"white-space": "pre", 'color': 'black'}),
     html.H4('Select one Sol (Martian day):', style={"white-space": "pre", 'color': 'white',
                                                     'text-shadow': '0 0 20px #fff, 0 0 30px coral, 0 0 40px coral'}),
     dcc.Tabs(id='tabs-example', value='tab-1', children=[
         dcc.Tab(label='{}'.format(days[0]), value='tab-1', style={'color': 'DarkOrange'}, selected_style={
             'backgroundColor': 'OldLace',
             'color': 'grey',
         }),
         dcc.Tab(label='{}'.format(days[1]), value='tab-2', style={'color': 'DarkOrange'}, selected_style={
             'backgroundColor': 'OldLace',
             'color': 'grey',
         }),
         dcc.Tab(label='{}'.format(days[2]), value='tab-3', style={'color': 'DarkOrange'}, selected_style={
             'backgroundColor': 'OldLace',
             'color': 'grey',
         }),
         dcc.Tab(label='{}'.format(days[3]), value='tab-4', style={'color': 'DarkOrange'}, selected_style={
             'backgroundColor': 'OldLace',
             'color': 'grey',
         }),
         dcc.Tab(label='{}'.format(days[4]), value='tab-5', style={'color': 'DarkOrange'}, selected_style={
             'backgroundColor': 'OldLace',
             'color': 'grey',
         }),
         dcc.Tab(label='{}'.format(days[5]), value='tab-6', style={'color': 'DarkOrange'}, selected_style={
             'backgroundColor': 'OldLace',
             'color': 'grey',
         }),
         dcc.Tab(label='{}'.format(days[6]), value='tab-7', style={'color': 'DarkOrange'}, selected_style={
             'backgroundColor': 'OldLace',
             'color': 'grey',
         }),

     ], colors={
         "border": "OldLace",
         "primary": "gold",
         "background": "PeachPuff"
     }, style={'width': '500px'}),
     html.Div(id='tabs-example-content'),

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
if __name__ == '__main__':
    app.run_server(debug=True)


# import plotly.graph_objects as go
#
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5, 6, 7], y=[3, 5, 7, 5, 6, 7, 9],
#                     mode='lines',
#                     name='lines'))
# fig.show()
