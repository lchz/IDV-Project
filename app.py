import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

import plotly.express as px
import geopandas as gpd

import pandas as pd

## Initiate the app ###
app = dash.Dash(__name__)
server = app.server
######################

df = pd.read_csv('count_by_country.csv')
fig = go.Figure(data=go.Choropleth(
    locationmode='country names',
    locations = df['Country'],
    z = df['Count'],
    text = df['Country'],
    colorscale= 'YlGnBu',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'Count',
))

## Layout
app.layout = html.Div([
    # html.P("Color:"),
    # dcc.Dropdown(
    #     id="dropdown",
    #     options=[
    #         {'label': x, 'value': x}
    #         for x in ['Gold', 'MediumTurquoise', 'LightGreen']
    #     ],
    #     value='Gold',
    #     clearable=False,
    # ),
    # dcc.Graph(id="graph"),
    dcc.Graph(figure=fig)
])

# @app.callback(Output("graph", "figure"), [Input("dropdown", "value")])
# def display_color(color):
#     # fig = go.Figure(
#         # data=go.Bar(y=[2, 3, 1], marker_color=color))


#      ######################################

#     geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
#     # geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


#     # px.set_mapbox_access_token(open(".mapbox_token").read())
#     fig = px.scatter_mapbox(geo_df,
#                             lat=geo_df.geometry.y,
#                             lon=geo_df.geometry.x,
#                             hover_name="name",
#                             zoom=1)
#     fig.update_layout(mapbox_style="open-street-map")
#     return fig


if __name__ == "__main__":
    app.run_server(debug=True)
