string_one = input("Write first word")
string_two = input("Write second word")
print(f"{string_one} {string_two}")

for answer in range(10):
    answer = input("Hello, write something :)")
    if answer.isupper() == True:
        print(answer.lower())

    elif answer.isupper() == False:
        print(answer.lower())

    else:
        print(answer)
        break





