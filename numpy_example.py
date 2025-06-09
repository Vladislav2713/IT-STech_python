import numpy as np
# Создание массива
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original data:", data)
# Операции
squared = data ** 2
mean = np.mean(data)
std = np.std(data)
print("Squared:", squared)
print (f"Mean: {mean:.2f}, Std: {std:.2f}")
# Фильтрация
evens = data[data % 2 == 0]
print("Even numbers:", evens)