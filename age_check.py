try:
    age = int (input("Enter your age: "))
    if age >= 18:
        print("You are an adult!")
    else:
        print("You are a minor.")
except ValueError:
    print ("Please enter a vaid integer!")