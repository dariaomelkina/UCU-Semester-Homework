import json
import dash
import urllib.request
import urllib.parse
import dash_core_components as dcc
import dash_html_components as html
import pandas
import plotly.express as px

BASE_URL = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"


def get_data_from_URL(base_url):
    with urllib.request.urlopen(base_url) as response:
        data = response.read()
        data = data.decode("utf-8")
        data = json.loads(data)
    return data


ready_data = get_data_from_URL(BASE_URL)
lst = []
for key in ready_data.keys():
    if key != "sol_keys" or key != "validity_checks":
        try:
            df = pandas.DataFrame(ready_data[key])
            lst.append(df["AT"]["av"])
        except KeyError:
            break

inf_series = pandas.DataFrame(list(zip(lst, ready_data['sol_keys'])), columns=["average temperature", "day"])

fig = px.bar(inf_series, x='day', y='average temperature', text='average temperature',
             hover_data=['average temperature', 'day'], color='average temperature',
             labels={'pop': 'temperature'}, height=400)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'text': '#91165a'
}

app.layout = html.Div(children=[
    html.H1(
        children='Dash Experiment',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='There are average temperatures on Mars by days.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig,
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
