# STATISTICS NOTES
import pandas as pd
'''
Desciptive Statistics and Data Visualization are part of EDA

Data Scientist:

Someone who extracts meaningful insights from data
using computation and statistics

Use of Statistics:

- Organize and summarize information
- Determine exactly what conclusions are justified
based on the results obtained

Goal of Statistics:
- Accurate and Meaningful Interpretation
- Provide Evalution Procedures

Population: entire group of individulas that you are intersted in
Smaple: a subset of the population

Goal: generalize from the sample data to the larger population

Parameter: A value that describes a population. It is derived from
           measurements made about the population

Statistic: A value that describes the sample. It is usually derived
           from measurements obtained from the sample

Quantitative: describes differences in quantity or numeric terms

Categorical: Assigning labels

4 Scales of Measurements:
Nominal - placing data in categories
Ordianl - the categories have an implied order
        - there is a directional meaning/ difference
        - however we cannot quantify the value or difference
Interval/Ratio - used to represent numeric values
               - we can determine the direction and magnitude of the difference
               - 0 is arbitrary for Interval, meaningful for ratio


1. Descriptive Statistics
     - Central Tendency
     - Variability

2. Inferencial Statistics
     - Hypothesis Testing
     - Predictions

Measures of Central Tendency:
Identify a single score that defines the center of a distribution
Goal: identify a value representative of a group

3 Measures of Central Tendency:

1. Mean
2. Median
3. Mode

THE MEAN:
sum / sample size

THE MEDIAN:
- midpoint when soreted in order
- better when the data contains outliers

THE MODE:
- highest frequency in the distribution
'''

df = pd.DataFrame([87, 82, 89, 90, 94, 92, 86, 92, 96, 96],
                  columns = ['Scores'])
print(sorted(df['Scores']))
print(df['Scores'].mean())
print(df['Scores'].median())
print(df['Scores'].mode())
print(df)

# MEASURES OF VARIABILITY
'''
Variability: describes the spread of the scores or distance of
             a score form the mean
Purpose:
1. Describe the Distribution
2. Measure how well an individual score represents the distribution

3 Measures of Variability

1. Range
2. Variance
3. Standard Deviation

THE RANGE:
- Range = Max Value -Min VALue
- AN imprecise, unreliable measure of variability

THE VARIANCE:
- statistical average of the amount of dispersion in a distribution of scores
- average squared distance from the mean
- average deviation of the scores from teh mean in sq units
- S^2 = sum(observation - average)^2 / sample size - 1
- Deviation is x - x hat

THE STANDARD DEVIATION:
- a measure of standard or average distance from teh mean
- square root of variance
'''

range_scores = df['Scores'].max() - df['Scores'].min()
print(range_scores)
print(df['Scores'].var())
print(df['Scores'].std())

# NORMAL DISTRIBUTION
'''
Frequency Distribution:
- Organized tabulation
- Shows the # of Data Points in each category

- Skewness denotes lack of symmetry
- Tail on the right -> Positive Skew
- Tail on the left -> Negative Skew

Kurtosis
- Leptokurtic = more pointy (higher peak)
- Platykurtic = flatter (lower peak)

THE EMPERICAL RULE
68% - 95% - 99.7%
'''
print(df.count())
print(df['Scores'].unique())
print(df['Scores'].value_counts())

import numpy as np
np.random.seed(1)
s = np.random.normal(loc = 80, scale = 15, size = 10000)
print(s.std())

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(s, kde = False)
plt.show()

# KDE: Kernal Density Estimate
# Applies the normal curve to the dataset

# graph.set_xlim(20,140)
