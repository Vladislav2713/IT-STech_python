import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Загрузка датасета
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print("Dataset info:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())
# Визуализация
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df)
plt.title('Sepal Length vs Sepal Width by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.savefig('iris_scatter.png')