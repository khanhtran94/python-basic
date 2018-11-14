books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested girf: {}".format(books[0]))
# inser pos
books.insert(0, "Learning python: Origen object")

# string immuable
lytric = "Hello work"
# err 
# lytric[0] = "c"

# debugg python -i file_name.py
#xoa label, Khong tra ve gia tri
del lytric
print(len(books))
# default gia tri cuoi cua arr, list, co the truyen gia tri vao, tra ve 1 gia tri
books.pop(0)
books.pop(1)
print(len(books))

for book in books:
    print("* {}".format(book))
