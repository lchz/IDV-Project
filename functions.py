import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

def collect_countries():
    df = pd.read_csv('./count_by_country.csv')
    return df['Country']

def display_map():
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
        colorbar_title = 'Count'
    ))

    fig.update_layout(
        title = {
            'text': 'QS University Ranking in 2020',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
    })

    return fig

def update_country(country):
    df = pd.read_csv('count_by_country.csv')
    # count = df[df['Country']==country]['Count'].values[0]

    fig = go.Figure(data=go.Choropleth(
        locationmode='country names',
        locations = [country],
        z = df['Count'],
        text = country,
        colorscale= 'YlGnBu',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = 'Count'
    ))

    fig.update_layout(
        title = {
            'text': 'QS University Ranking in 2020',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
    })

    return fig

# print(display_country('China'))