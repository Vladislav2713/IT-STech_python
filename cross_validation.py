import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
# Загрузка данных
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']
# Нормализация
scaler = StandardScaler()
X = scaler.fit_transform(X)
# Модель и кросс-валидация
model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print("Cross-validation scores:", scores)
print(f"Average accuracy: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")