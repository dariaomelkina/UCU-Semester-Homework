# import class from the module
from adt_weather_data import WeatherData
# import needed libs
import json
import urllib.request
import urllib.parse
import plotly.graph_objects as go

# get data for the adt
BASE_URL = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"


def get_data_from_url(base_url):
    with urllib.request.urlopen(base_url) as response:
        data = response.read()
        data = data.decode("utf-8")
        data = json.loads(data)
    return data


json_data = get_data_from_url(BASE_URL)

# load data into the class
week_weather = WeatherData(json_data)

# print the sols, which are described in the data
print(week_weather.days_list())

# assign information about one day to a variable
monday = week_weather.day(1)
print(monday)

# return a table with data for one day (in that case monday and we use only average data for each)
# def make_day_table(day):
#     """ Return a table with data for one day. """
#     fig = go.Figure(data=[go.Table(
#         header=dict(values=['MARTIAN DAY {}'.format(day(0))], line_color='DarkOrange',
#                     fill_color='PeachPuff',
#                     height=40,
#                     font=dict(family='Courier New, monospace', color='DarkOrange', size=32)),
#         cells=dict(values=[['Average temperature: {}'.format(day(3)),
#                             'Average wind speed: {}'.format(day(6)),
#                             'Average pressure: {}'.format(day(9))], ], line_color='DarkOrange',
#                    fill_color='OldLace', align='left', height=40,
#                    font=dict(family='Courier New, monospace', color='grey', size=23))),
#     ])
#     return fig


# make_day_table(monday).show()

# assign a name of season of a particular day to a variable and print it
monday_season = week_weather.season(1)
print(monday_season)

# assign information needed for a wind rose to a variable
monday_wind_rose = week_weather.wind_rose(1)
print(monday_wind_rose)


# build the wind rose
# def make_wind_rose(day_wind_rose):
#     """ Return a wind rose from data for one day. """
#     lst = day_wind_rose.head()
#     t = day_wind_rose.head().next
#     fig = go.Figure(go.Barpolar(r=lst,
#                                 theta=t,
#                                 marker_color=['coral'] * len(lst),
#                                 ))
#     fig.update_layout(
#         template='plotly_dark',
#         autosize=False,
#         width=500,
#         height=450,
#         title='Wind Direction Distribution',
#         font={'size': 16},
#         title_x=0.5,
#     )
#     return fig
#
#
# make_wind_rose(monday_wind_rose).show()

# and an example of a graph with minimum temperatures thorough week
# assign needed list to the variable
week_min_temp = week_weather.min_temp()
print(week_min_temp)

# build the line graph
# def make_trace_graph(data):
#     """ Return a line graph with data for the week. """
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5, 6, 7], y=data,
#                              mode='lines',
#                              name='lines'))
#
#
# make_trace_graph(week_min_temp).show()
