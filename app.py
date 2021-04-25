import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import functions as f

## Initiate the app ###
app = dash.Dash(__name__)
server = app.server

print('Starting...')

## Layout
app.layout = html.Div([

    dcc.Dropdown(
        id="country-dropdown",
        options=[
            {'label': country, 'value': country}
            for country in f.collect_countries()
        ],
        placeholder='Select a country',
    ),

    dcc.Graph(id="graph1"),
    dcc.Graph(id="table"),
    dcc.Store(id='previous_click'),
])

@app.callback(Output('graph1', 'figure'), 
                Output('table', 'figure'),
                Output('previous_click', 'data'),
                Input('country-dropdown', 'value'),
                Input('graph1', 'clickData'),
                Input('previous_click', 'data'))
def update_map_and_table(dropdown_country, clickData, previous_click):
    context = dash.callback_context

    if context.triggered:
        update_id = context.triggered[0]['prop_id'].split('.')[0]

        if update_id == 'country-dropdown':
            return (f.display_map(dropdown_country), 
                    f.display_table(dropdown_country),
                    {})

        elif update_id == 'graph1':
            click = clickData['points'][0]['location']

            if not previous_click or click != previous_click['pre']:
                return (f.display_map(click), 
                        f.display_table(click),
                        {'pre': click})
            elif click == previous_click['pre']:
                return (f.display_map(), 
                        f.display_table(),
                        {})

    return (f.display_map(),
            f.display_table(),
            {})


if __name__ == "__main__":
    app.run_server(debug=True)
