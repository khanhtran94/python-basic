import os
shopping_list = []

def clear_screen():
  os.system("cls" if os.name == 'nt' else 'clear')

def add_to_list(item):
  show_list()
  if len(shopping_list):
    position = input("Where should I add {}? \n"
      "Press Enter to add the end of the list \n"
      "> ".format(item))
  else:
    position = 0
  try:
    position = abs(int(position))
  except ValueError:
    position = None
  if position is not None:
    shopping_list.insert(position - 1, item)
  else:
    shopping_list.append(item)
  
  show_list()

def remove_item_shopping():
  show_list()
  what_remove_item = input("What item remove ? \n")
  try:
    shopping_list.remove(what_remove_item)
  except ValueError as err:
    pass
  show_list()

def show_help():
  clear_screen()
  print("What should we pick up at the store ")
  print("""
Enter DONE finish.
Enter HELP for this help.
Enter SHOW see your list.
Enter REMOVE to delete an item from shopping list.
""" )

def show_list():
  clear_screen()
  print("Here's your list")
  i = 0
  for item in shopping_list:
    print("{} {}".format(i, item))
    i += 1
  print("-"*10)

show_help()
while True:
  new_item = input("> ")
  if new_item.upper() == 'DONE':
    break
  elif new_item.upper() == 'HELP':
    show_help()
    continue
  elif new_item.upper() == 'SHOW':
    show_list()
    continue
  elif new_item.upper() == 'REMOVE':
    remove_item_shopping()
    continue
  else:
    add_to_list(new_item)

show_list()