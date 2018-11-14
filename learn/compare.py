first_name = input("What is your name ")
print(first_name)
if first_name == "K":
    age = int(input("How old are you"))
    if age <= 6:
        print("wow you are {}".format(first_name))
        print("I am {}".format(age))
else:
    print("Not {}".format(first_name))

