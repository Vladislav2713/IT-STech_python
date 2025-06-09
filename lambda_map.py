numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)
evens_squared = list (map(lambda x: x **2, filter(lambda x: x % 2 == 0, numbers)))
print("Squares of even numbers:", evens_squared)