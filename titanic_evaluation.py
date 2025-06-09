import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# Загрузка данных
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df = df[['Pclass', 'Age', 'Fare', 'Sex', 'Survived']].dropna()
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
X = df[['Pclass', 'Age', 'Fare', 'Sex']]
y = df['Survived']
# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Нормализация
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Обучение модели
model = LogisticRegression()
model.fit(X_train, y_train)
# Оценка
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
# Кросс-валидация
scores = cross_val_score(model, scaler.fit_transform(X), y, cv=5)
print(f"Cross-validation scores: {scores}")
print(f"Average CV accuracy: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")