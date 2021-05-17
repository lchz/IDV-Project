import pandas as pd
from math import ceil

import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('./count_by_country.csv')
df_all = pd.read_csv('./university_ranking_2020.csv')

### Table headers and row colors ###
headers = list(df_all.columns.values)
headers.insert(0, ' ')
rowColor1 = 'linen'
rowColor2 = 'white'

def collect_countries():
    return df['Country']

def display_map(click_country=None, z=0):

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

    ### Highlight the clicked / selected (dropdown) country ###
    if click_country:
        highlighted = go.Choropleth(
            locationmode='country names',
            # z = df['Count'],
            # z = [0],
            z = [z],
            locations=[click_country],
            hovertemplate = df[df['Country']==click_country]['Hover_text'],
            colorscale= 'Portland',
            autocolorscale=False,
            marker_line_color='Blue',
            marker_line_width=2,
            showscale = False,
        )
        fig.add_trace(highlighted)

    fig.update_layout(
        title = {
            'text': 'QS University Ranking in 2020',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
    })

    return fig



def display_table(location=None):
    if not location:
        fig = go.Figure(data=[
                go.Table(
                    header=dict(values=headers,
                                align=['center','center','center','left','center','center'],
                                fill_color='lightsteelblue')
                    )
                ])

        fig.update_layout(
            title = {
                'text': f'Choose a country for more details'
        })
        
    else:
        info = df_all[df_all['Country']==location]
        length = info.shape[0]

        fig = go.Figure(data=[
                        go.Table(
                            header=dict(values=headers,
                                        align=['center','center','center','left','center','center'],
                                        fill_color='lightsteelblue'),
                            cells=dict(
                                values=[list(range(length+1))[1:],info['Rank in 2020'],info['Rank in 2019'], info['Institution Name'], info['Country'], info['Overall Score']],
                                        align=['center','center','center','left','center','center'],
                                        fill_color=[[rowColor1, rowColor2]*ceil(length/2)]
                                ))
                        ])

        fig.update_layout(
            title = {
                'text': f'QS 2020 university ranking in {location}'
        })

    return fig

# 1. Layout
# 2. Some errors in the university names
# 3. University search field