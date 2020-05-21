for number in range(10):
    number = int(input("Select a number between 1 and 100"))
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")


    elif number % 5 == 0:
        print("buzz")


    elif number % 3 == 0:
        print("fizz")


    else:
        print(str(number))
