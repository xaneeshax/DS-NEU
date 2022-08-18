import pandas as pd

df = pd.read_csv('fruits_data.csv')
print(df.head())

print(df['fruit'].value_counts())

fruit_dict = {'apple' : 1, 'orange' : 2, 'banana' : 3}
fruit_nominal = {1 : 'apple', 2 : 'orange', 3 : 'banana'}


def transform_fruit(column):
    return fruit_dict[column]

df['target'] = df['fruit'].apply(transform_fruit)
print(df.head())


import plotly.express as px
fig = px.scatter_matrix(df, dimensions = ['weight', 'width', 'height'],
                        color = 'fruit')
fig.show()

features = df[['weight', 'width', 'height']]
print(features.head())

target = df['target']
print(target.head())


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(features, target,
                                                    random_state = 3000)

print('HELLLO')
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# k-Nearest Neighbors Algorithm

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X = x_train, y = y_train)

fruit_prediction = knn.predict([[11.3, 3.75, 3.99]])
print(fruit_nominal[fruit_prediction[0]])


predicted = knn.predict(X = x_test)
print('predicted', predicted)

expected = y_test
print('expected', expected)
results = pd.DataFrame(predicted, columns = ['Predicted'])
results['Expected'] = expected.values

print(results)

results = results[results['Predicted'] != results['Expected']]
print(results)

print(len(results) / len(x_test))

accuracy = knn.score(x_test, y_test)
print(accuracy)
