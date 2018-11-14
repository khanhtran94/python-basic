import math

def split_check(total, number_of_people):
  if number_of_people <= 0:
    raise ValueError("More than 1 person is required to split the check")
  return math.ceil(total / number_of_people)
try:
    total_due = float(input("What is the total?"))
    number_of_people = int(input("How many people?"))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("That's mpt a value. Try again...")
    print("${}".format(err))
except ZeroDivisionError:
    print("Not div 0") 
else:
    print("Each person owes ${}".format(amount_due))
