import pandas as pd
# Создание тестового датасета
data = {
'name': ['Alice', 'Bob', None, 'David'],
'age': [25, -5, 30, None],
'score': [85, 90, 88, 92]
}
df = pd.DataFrame(data)
print("Original data:")
print(df)
# Очистка
df = df.dropna()  # Удалить пропуски
df = df[df['age'] > 0]  # Удалить некорректные возраста
print("\nCleaned data:")
print(df)