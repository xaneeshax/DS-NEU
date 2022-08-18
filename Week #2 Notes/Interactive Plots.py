import plotly.express as px
import pandas as pd

df = pd.DataFrame({'House' : ['Gryffindor', 'Hufflepuff', 'Ravenclaw',
                             'Slytherin'],
                  'Points' : [482, 352, 426, 472],
                  'Details': ['courage', 'kindness', 'wit', 'ambitious']})

print(df)

fig = px.bar(df, x = 'House', y = 'Points', color = 'Points', template = 'ggplot2',
             hover_name = 'House', hover_data = ['Details'],
             labels = {'House' : 'Hogwarts House', 'Points' : 'House Points'})
fig.update_traces(marker_color = ['#8b0000', '#FFD700', '#00316e', '#013220'])
fig.update_xaxes(title_font = {'size' : 18, 'family' : 'Courier', 'color': 'Gray'},
                 tickfont = {'size' : 16, 'family' : 'Courier', 'color': 'Gray'})
fig.update_yaxes(title_font = {'size' : 18, 'family' : 'Courier', 'color': 'Gray'},
                 tickfont = {'size' : 16, 'family' : 'Courier', 'color': 'Gray'})

fig.show()

# Comparative Bar Chart
# fig = px.bar(quidditch, x = 'House', y = 'Potion_ave', title = 'House
#              Points', color = 'Quidditch', barmode = 'group')
# fig.show()

# To save the file in HTML
# You can include this in a website
#plotly.offline.plot(fig, filename = 'res/fig.html')
