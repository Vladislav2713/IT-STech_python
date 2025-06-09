try:
    a = float (input ("Enter first number: "))
    b = float (input ("Enter second number: "))
    result = a / b
except ValueError:
    print ("Please enter valid numbers!")
except ZeroDivisionError:
    print ("Cannot divide by zero!")
else:
    print (f"Result: {result:.2f}")
finally:
    print("Calculation complete.")