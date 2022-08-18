import plotly.express as px
import pandas as pd

df = pd.read_csv('world_data.csv')

fig = px.scatter(df, x = 'Income', y = 'LifeExpectancy',
                 labels = {'LifeExpectancy' : 'Life Expectancy'},
                 size = 'Population', animation_frame = 'Year',
                 animation_group = 'Country', hover_name = 'Country',
                 size_max = 50, template = 'ggplot2', color = 'Continent',
                 range_x = [100, 100000], range_y = [25, 90],
                 title = 'Realtionship between Average Income and Life Expectancy')

fig.update_xaxes(title_font = {'size' : 18, 'family' : 'Courier', 'color' : 'gray'},
                 tickfont = {'size' : 16, 'family' : 'Courier', 'color' : 'gray'})

fig.update_yaxes(title_font = {'size' : 18, 'family' : 'Courier', 'color' : 'gray'},
                 tickfont = {'size' : 16, 'family' : 'Courier', 'color' : 'gray'})

fig.show()



'''
    Line Graph in Plotly
'''

'''
fig = px.line(df, x = 'Year', y = 'Points', line_group = 'Type',
              color = 'Type', title = 'House Points for Gryffindor',
              template = 'ggplot2')

fig.update_xaxes(title_font = {'size' : 18, 'family' : 'Courier', 'color' : 'gray'},
                 tickfont = {'size' : 16, 'family' : 'Courier', 'color' : 'gray'})

fig.show()
'''

'''
    Scatter Plot in Plotly
'''

import plotly.express as px
df = pd.read_csv('final_characters.csv')
df['Popularity'] = [(i + 1) ** 1.5 for i in range(24)][::-1]
print(df)

fig = px.scatter(df, x = 'Intelligence', y = 'Combat', size = 'Popularity',
                 hover_name = 'Name', template = 'ggplot2', size_max = 50,
                 title = 'Marvel Powers', color = 'Alignment')

fig.update_xaxes(title_font = {'size' : 18, 'family' : 'Courier', 'color' : 'gray'},
                 tickfont = {'size' : 16, 'family' : 'Courier', 'color' : 'gray'})

fig.update_yaxes(title_font = {'size' : 18, 'family' : 'Courier', 'color' : 'gray'},
                 tickfont = {'size' : 16, 'family' : 'Courier', 'color' : 'gray'})

fig.show()
