import pandas as pd
pd.set_option('precision', 2)
pd.set_option('display.max_columns', None)

df = pd.read_csv('divergent.csv')
print(df, end = '\n\n')


df['original'] = ['y', 'n', 'y', 'n' , 'n', 'y', 'n' , 'n', 'n', 'y']
print(df, end = '\n\n')

df = df.set_index(['faction', 'name'])
print(df, end = '\n\n')

print(df.loc['dauntless'].mean())

print(df.groupby('faction')['brave'].mean(), end = '\n\n')
print(df.groupby('faction')['kind'].apply(lambda x : x * 2), end = '\n\n')
print(df.groupby(level = 'faction').mean(), end = '\n\n')
print(df.groupby(['faction', 'original']).mean(), end = '\n\n')
print(df.groupby(['faction', 'original']).agg(['count', 'mean', 'std']))

print('\n', df, end = '\n\n')


def score(score):

    if score.mean() > 85:
        return 'very'
    else:
        return 'eh'

def passed(score):

    if score.mean() > 60:
        return 'passed'
    else:
        return 'failed'

print(df.groupby('faction').agg(score))
print(df.groupby('faction').agg(['count', 'mean', 'std', score]))

print(df.groupby('faction').agg({'kind' : passed, 'brave' : score,
                                 'smart' : score, 'honest' : score,
                                 'selfless' : score}))
