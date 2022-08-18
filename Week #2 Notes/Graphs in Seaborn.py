
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('final_characters.csv')
df['Popularity'] = [(i + 1) ** 1.5 for i in range(24)][::-1]
print(df)

'''
    Line Graph in Seaborn
'''

print(sns.plotting_context())

sns.set_context(rc = {'lines.linewidth' : 2})
graph = sns.lineplot(x = 'Intelligence', y = 'Combat', hue = 'Alignment',
                     data = df)

title = 'Intelligence and Combat of Marvel Characters'
graph.set_title(title, size = 16)

graph.set_xlabel('Intelligence', size = 16)
graph.set_ylabel('Combat', size = 16)

plt.legend(loc = 'best')

plt.show()

graph = sns.scatterplot(x = 'Intelligence', y = 'Combat',
                        hue = 'Alignment', data = df, size = 'Popularity',
                        marker = '*', sizes = (100, 1000), alpha = 0.5,
                        palette = ['darkred', 'gold', 'darkblue'])

title = 'Intelligence and Combat of Marvel Characters'
graph.set_title(title, size = 16)

graph.set_xlabel('Intelligence', size = 16)
graph.set_ylabel('Combat', size = 16)
plt.show()

'''
    One Line
'''


years = [i + 1 for i in range(5)]
deducted = [189, 5, 125, 90, 125, 90] 

graph = sns.lineplot(x = years, y = deducted)
title = 'Points Deducted from Gryffindor over Years'
graph.set_title(title, size = 16)

graph.set_xlabel('Year', size = 16)
graph.set_ylabel('Points Deducted', size = 16)
plt.show()

'''
    Two Lines
'''

# For multiple lines

# graph = sns.lineplot(x = 'years', y = 'points', hue = 'Type',
#                     data = df, palette = ['darkred', 'darkgreen'])



