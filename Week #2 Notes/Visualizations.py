import matplotlib.pyplot as plt

# Use this to make sure the images fit in the Jupiter Notebook
# %matplotlib inline

# Matplotlib was designed before pandas
# Seaborn is an improvement on matplotlib and is built on
# this library

import seaborn as sns

# Sets the width of the bars on teh bargraph
sns.set_context(rc = {'patch.linewidth' : 2})

# Display the color pallete
sns.palplot(sns.color_palette())
sns.set_palette('colorblind')

# House names and points
house_names = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
house_points = [312, 352, 412, 472]

# Renders a bar graph
graph = sns.barplot(x = house_names, y = house_points,
                    color = 'r', edgecolor = 'k')
# graph.figure.savefig('house_points.png')
plt.show()

# Renders a bar graph
graph = sns.barplot(x = house_names, y = house_points,
                    palette = 'colorblind', edgecolor = 'k')

# Set the title and labels
graph.set_title('House Points', size = 16)
graph.set_xlabel('House', size = 16)
graph.set_ylabel('Points', size = 16)

# Angle of the names on the bar graph
graph.set_xticklabels(house_names, rotation = -45)
plt.show()
