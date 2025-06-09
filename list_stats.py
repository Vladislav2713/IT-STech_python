def analyze_numbers(numbers):
    if not numbers:
        return 0, 0, []
    total = sum(numbers)
    average = total / len(numbers)
    positive = [x for x in numbers if x > 0]
    return total, average, positive
try:
    numbers = [int(x) for x in input("Enter numbers (space-separated): ").split()]
    total, avg, pos = analyze_numbers(numbers)
    print (f"Sum: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Positive numbers: {pos}")
except ValueError:
    print ("Please enter vaid numbers!")