import pandas as pd
from math import ceil

import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('./count_by_country.csv')
df_all = pd.read_csv('./university_ranking_2020.csv')
rowColor1 = 'floralwhite'
rowColor2 = 'ghostwhite'


def collect_countries():
    return df['Country']

def display_map(country=None, location=None):
    if country:
        hover = df[df['Country']==country]['Hover_text']
        locations = [country]
    else:
        hover = df['Hover_text']
        locations = df['Country']

    fig = go.Figure(data=go.Choropleth(
        locationmode='country names',
        locations = locations,
        z = df['Count'],
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



def display_table(location):
    if not location:
        fig = go.Figure()
        
    else:
        info = df_all[df_all['Country']==location]
        headers = list(info.columns.values)
        headers.insert(0, ' ')
        length = info.shape[0]

        fig = go.Figure(data=[
                        go.Table(
                            header=dict(values=headers,
                                        align=['center','center','center','left','center','center']),
                            cells=dict(
                                values=[list(range(length+1))[1:],info['Rank in 2020'],info['Rank in 2019'], info['Institution Name'], info['Country'], info['Overall Score']],
                                        align=['center','center','center','left','center','center'],
                                        fill_color=[[rowColor1, rowColor2]*ceil(length/2)]
                                ))
                        ])

    fig.update_layout(
        title = {
            'text': f'Universities in {location}'
    })

    return fig

