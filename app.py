import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import functions as f

## Initiate the app ###
app = dash.Dash(__name__)
server = app.server

print('Starting...')
## Layout
app.layout = html.Div([
    # html.P("Color:"),
    # dcc.Graph(figure=f.display_map()),

    dcc.Dropdown(
        id="country-dropdown",
        options=[
            {'label': country, 'value': country}
            for country in f.collect_countries()
        ],
        placeholder='Select a country',
    ),
    dcc.Graph(id="graph1"),
    # dcc.Graph(id="graph2"),
    dcc.Graph(id="table"),

])

# (id, type)
@app.callback(Output("graph1", "figure"),Input("country-dropdown", "value"))
def dropdown_map(country):
    return f.display_map(country)


@app.callback(Output('table', 'figure'), 
              Input('graph1', 'clickData'),
              Input("country-dropdown", "value"))
def country_to_table(clickData, country):
    if country:
        location = country
    elif clickData is not None:
        location = clickData['points'][0]['location']
        
    return f.display_table(location)


# @app.callback(Output('graph2', 'figure'), 
#             #   Output('graph1', 'figure'),
#               Input('graph1', 'clickData'))
# def test(clickData):    
#     # print('highlighting...')
#     if clickData is not None:      
#         location = clickData['points'][0]['location']
#     else:
#         location = None
        
#     return f.display_map(location)

#     # return f.display_map()


if __name__ == "__main__":
    app.run_server(debug=True)
