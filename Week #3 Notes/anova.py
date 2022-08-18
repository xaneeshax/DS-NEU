# Analysis of Variance aka ANOVA
'''
Used to compare two means to see if they are significantly
different from each other

Hypotheses:

Ho: No difference among the means
H1: There is atleast one mean difference among the populations
'''

from scipy import stats
import pandas as pd

data = pd.read_csv('candles_three.csv')
print(data)

descriptives = data.groupby('Group').agg(['count', 'mean', 'std', 'sem'])
print(descriptives)

descriptives = descriptives['Candles']
descriptives.reset_index(inplace = True)
print(descriptives)

import plotly.express as plt

graph = plt.bar(descriptives, x = 'Group', y = 'mean', error_x = 'sem',
                error_y = 'sem', template = 'ggplot2', width = 500,
                labels = {'mean' : 'Number of Candles', 'Group' :
                          'Wands Used'})
graph.update_traces(marker_color = ['#d3d3d3', '#FFF', '#FFF'])
graph.update_traces(marker = dict(line = {'width' : 3, 'color' : '#000000'}))

graph.update_xaxes(title_font = {'size' : 16},
                   tickfont = {'size' : 14, 'color' :'gray'})

graph.update_yaxes(title_font = {'size' : 16},
                   tickfont = {'size' : 14, 'color' :'gray'})

#graph.show()

elder_wand = data[data['Group'] == 'Elder Wand']['Candles']
personal_wand = data[data['Group'] == 'Personal Wand']['Candles']
regular_wand = data[data['Group'] == 'Regular Wand']['Candles']

wands = [elder_wand, personal_wand, regular_wand]
print(stats.f_oneway(wands))

df1 = len(descriptives) - 1
df2 = (len(elder_wand) - 1) + (len(personal_wand) - 1) + (len(regular_wand) - 1)

print('Degrees of Freedom', df1, df2)

'''
Assumption of Equality of Variances
Assumption of Normality
'''

levene_results, y = stats.levene(elder_wand, regular_wand, personal_wand)
print(levene_results, y)


shapiro_elder = stats.shapiro(elder_wand)
print(shapiro_elder)
shapiro_regular = stats.shapiro(regular_wand)
print(shapiro_regular)
shapiro_personal = stats.shapiro(personal_wand)
print(shapiro_personal)


'''
After an ANOVA test you need a further analysis to find out which groups differ

An ANOVA test only establishes that mean differnces exist-- however, it does
not identify exactly which means are significantly different and which are not

A Post hoc test is only conducted after a significant ANOVA result

A significant F-statistic tells us that M1 = M2 = M3 is NOT true

'''


from statsmodels.stats.multicomp import MultiComparison
from statsmodels.stats.multicomp import pairwise_tukeyhsd

mc = MultiComparison(data['Candles'], data['Group'])
tukey_result = mc.tukeyhsd()
print(tukey_result)



'''
When reporting the results of a One-way ANOVA Test
1. Descriptives
2. Assumption Checks
3. F-stat, Degrees of Freedom, p-value
4. A bar graph

Test & Purpose:
A one-way analysis of variance was conducted to compare
the...

Actaul Results:
Results revealed a statistically significant difference among...
F(2,57) = 56.45, p < 0.001
Post-hoc comparisions using teh Tukey test indicated that the
... (M = 12.2, SE = 0.78)

Interpretation
These results indicate that the...
'''
# Parametric and Nonparametric Statistics

'''
Parametric Tests Share the following assumptions:
- Normal Distribution
- Homogeneity of varaince in the population
- Numerical score for each individual

Nonparametric statistical test are used as alternative
tests when the assumptions are violated

- Less likely to reject the null hypothesis
'''
















