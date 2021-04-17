import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import functions as f

## Initiate the app ###
app = dash.Dash(__name__)
server = app.server


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
    
])

# (id, type)
@app.callback(Output("graph1", "figure"), [Input("country-dropdown", "value")])
def display_map(country):
    if country:
        return f.update_country(country)

    return f.display_map()



if __name__ == "__main__":
    app.run_server(debug=True)
