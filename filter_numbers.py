try:
    numbers = [int(x) for x in input("Enter numbers (space-separated): ").split()]
    multiples_of_there = [x for x in numbers if x % 3 == 0]
    multiples_of_there. sort()
    if multiples_of_there:
        print ("Numbers divisible by 3:", multiples_of_there)
    else:
        print ("No numbers divisible by 3.")
except ValueError:
    print("Please enter vaid numbers!")