books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = ["Dota2",
    "LOL",
    "Game 2",
]


def display_wishlist(display_name, wishes):
    print(display_name)
    print("====> ", wishes[0], "<=====")
    #return a slice of the list from the 2nd element on
    for wish in wishes[1:]:
        print("* " + wish)

    print()

def display_wishlist_copy(display_name, wishes):
    print(display_name)
    items = wishes.copy()
    suggest_wish = items.pop(0)
    print("=====> ", suggest_wish, "<======")
    for item in items:
        print("* ",item)
    print()

#display_wishlist("Books", books)
#display_wishlist("Game 1", video_games)
#display_wishlist("Game 2", video_games)
#display_wishlist_copy("Book", books)

# for se tang tu 0 toi 1, 2, 3, nhung khi xoa, thi 0 la a, sau khi xoa a,
# thi 0 la b, nhung for tang len 1 nen no se xoa c
inventory_1 = ["a", "b", "c", "d"]
for i in inventory_1:
    print(i.index)
    print(i)
    inventory_1.remove(i)
print(inventory_1)
print()

# tao ra 1 ban copy cua list, va ta se duyet tuan tu trong ban copy,
#  va xoa tuong ung moi phan tu duyet trong ban copy voi ban goc,
#  do ban copy ko bi doi, immuable, nen ta se duyet dc toan bo phan tu ma
# ko bo qua bat ky phan tu nao
inventory_2 = ["a", "b", "c", "d"]
for i in inventory_2.copy():
    print(i)
    inventory_2.remove(i)
print(inventory_2)
print()

