a = int(input("Write the first number"))
b = int(input("Write the second number"))
operation = input("Which operation do you need?")

if operation == "+":
    print(str(a) + "+" + str(b) + "=" + str(a+b))

elif operation == "-":
    print(str(a) + "-" + str(b) + "=" + str(a - b))

elif operation == "*":
    print(str(a) + "*" + str(b) + "=" + str(a * b))

elif operation == "/":
    print(str(a) + "/" + str(b) + "=" + str(a / b))

else:
    print("I'm sorry, I don't recognize this operation.")
