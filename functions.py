import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('./count_by_country.csv')


def collect_countries():
    return df['Country']

def display_map():
    fig = go.Figure(data=go.Choropleth(
        locationmode='country names',
        locations = df['Country'],
        z = df['Count'],
        hovertemplate = df['Hover_text'],
        colorscale= 'YlGnBu',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = 'University count'
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
    hover = df[df['Country']==country]['Hover_text']

    fig = go.Figure(data=go.Choropleth(
        locationmode='country names',
        locations = [country],
        z = df['Count'],
        text = country,
        hovertemplate = hover,
        colorscale= 'YlGnBu',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = 'University count'
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



def get_clicked(location):
    info = df[df['Country']==location]

    fig = go.Figure(data=[
                    go.Table(
                        header=dict(values=info.columns.values[:3]),
                        cells=dict(values=[[info.iloc[0][0]], [info.iloc[0][1]], [info.iloc[0][2]]]))
                    ])

    fig.update_layout(
        title = {
            'text': 'Table'
    })

    return fig

