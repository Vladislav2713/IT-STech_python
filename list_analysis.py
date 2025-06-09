try:
    numbers = [int(x) for x in input("Enter numbers (space-separated): ").split()]
    print(f"Sum: {sum(numbers)}")
    print(f"Maximum: {max(numbers)}")
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {evens}")
except ValueError:
    print ("Please enter vaid numbers!")