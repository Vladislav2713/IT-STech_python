import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
# Загрузка данных
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df = df[['Pclass', 'Age', 'Fare', 'Sex', 'Survived']].dropna()
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
X = df[['Pclass', 'Age', 'Fare', 'Sex']]
y = df['Survived']
# Нормализация
scaler = StandardScaler()
X = scaler.fit_transform(X)
# Модель и поиск
model = LogisticRegression()
param_grid = {'C': [0.01, 0.1, 1, 10, 100], 'penalty': ['l1', 'l2'], 'solver': ['liblinear']}
grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
grid.fit(X, y)
# Результаты
print(f"Best parameters: {grid.best_params_}")
print(f"Best cross-validation score: {grid.best_score_:.2f}")