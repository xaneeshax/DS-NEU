'''
5 Steps before you begin:

1. State the hypothesis

Avoid HARKING - stating the hypothesis after the results are known

2. Set the criteria for a decision

Determine alpha level (generally alpha = 0.05 in most sciences)

3. Collect/retrieve data

Always after stating your hypothesis and setting the criteria
(ensures objectivity)

4. Compute sample statistic

Choose and conduct your statistical test

5. Make a Decision

If p < alpha level, reject the null hypothesis
If not, you fail to reject the null hypothesis
'''

# Independant Sample T test

'''
Used to compare two means to see if they are significantly
different from each other

Hypothesis:

Ho: No difference between the two means
H1: The two means are different

t = (x1 mean - x2 mean) / Estimate Standard Error

Estimate Standerd Error = sqrt(s^2/N1 + s^2/N2)

Degrees of Freedom: estimate the unknown population parameter
Sample Mean is used to estimate the population mean

df = n1 + n2 -2
'''
from scipy import stats
import pandas as pd

data = pd.read_csv('candles_data.csv')
print(data)

descriptives = data.groupby('Group').agg(['count', 'mean', 'std', 'sem'])
print(descriptives)

descriptives = descriptives['Candles']
descriptives.reset_index(inplace = True)
print(descriptives)

import plotly.express as plt
graph = plt.bar(descriptives, x = "Group", y = "mean", error_x = "sem", error_y = "sem",
                template='ggplot2', width=500, 
                labels = {"mean": "Number of Candles", "Group": "Wand Used"})

graph.update_traces(marker_color="#d4202f")
graph.update_traces(marker= dict(line={"width":3,"color":"#000000"}))

graph.update_xaxes(title_font={"size":16}, tickfont = {"size":14, "color":"gray"})
graph.update_yaxes(title_font={"size":16}, tickfont = {"size":14, "color":"gray"})

elder_wand = data[data['Group'] == 'Elder Wand']['Candles']
print(elder_wand)
regular_wand = data[data['Group'] == 'Regular Wand']['Candles']
print(regular_wand)

result = stats.ttest_ind(elder_wand, regular_wand)
print(result)

t_stat = result[0]
print('t-statistic', format(t_stat, '.2f'))
p_value = result[1]
print('p-value', format(p_value, '.10f'))

df = len(elder_wand) + len(regular_wand) - 2
print(df)

def report_independent_t(t, p, df):
    print('t(%d)=%.2f, p=%.3f' % (df, t, p))

print(report_independent_t(t_stat, p_value, df))

#graph.show()


# Assumptions of a T-test
# - Assumption of Equality of Variances
# - Assumption of Normality

'''
- Homogeniety: variances should be roughly the same
- Dependant variable should be normally distributed

You want non-significant results:
Variance A = Variance B (Null Hypothesis is True)
'''

# t-statistic first, p value second
levene_results = stats.levene(elder_wand, regular_wand)
print(levene_results)

shapiro_results = stats.shapiro(data['Candles'])
print(shapiro_results)



'''
Assumptions of normality,as assessed by Shapiro-Wilk's test (p > 0.05)
and homogenity (equality) of variances, as assessed by Levene's test
(p > 0.05) were met.
'''

# Paired Sample T test

'''
t = Xd / (Sd / sqrt(n))

Ho: The null hypothesis states that the population mean difference is 0
H1 : The difference of the two means does not equal 0

df = n - 1
'''

paired = pd.read_csv('candles_pairs.csv')
print(paired)

describo = paired.agg(['count', 'mean', 'std', 'sem'])
describo
print(describo)
describo = describo.T.drop('Participant')
print(describo)

describo.reset_index(inplace = True)
print(describo)

import plotly.express as plt
graph = plt.bar(describo, x = "index", y = "mean", error_x = "sem", error_y = "sem",
                template='ggplot2', width=500, 
                labels = {"mean": "Number of Candles", "index": "Wand Used"})

graph.update_traces(marker_color="#FFF")
graph.update_traces(marker= dict(line={"width":3,"color":"#000000"}))

graph.update_xaxes(title_font={"size":16}, tickfont = {"size":14, "color":"gray"})
graph.update_yaxes(title_font={"size":16}, tickfont = {"size":14, "color":"gray"})
#graph.show()

results = stats.ttest_rel(paired['Elder_Wand'], paired['Regular_Wand'])
print(results)
t_stat = results[0]
print(t_stat)

p_value = results[1]
print(p_value)

df = len(paired) - 1

# Assumption: Only normality
# Use mean differences


