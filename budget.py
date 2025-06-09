try:
    income = float(input("Enter your monthly income: $"))
    expenses = float(input("Enter your monthly expenses: $"))
    balance = income - expenses
    print (f"Your balance is ${balance:.2f}")
except ValueError:
    print("Please enter vaid numbers!")