import pandas as pd

df = pd.DataFrame({'City' : ['Zoston', 'Pittsfield'],
                   '2014' : [78425, 52041],
                   '2015' : [81533, 52526]})
df = df.set_index('City')
df.apply(lambda x : x + 1000)
print(df[df > df.mean()].dropna())
print(df)
