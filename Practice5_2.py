import csv
books_data = []

with open("books.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        books_data.append(row)

users_data = int(input("Сколько хотите добавить записей?"))
last_number = -1
for dictionary in books_data:
    for key in dictionary.values():
        if int(key[0]) > last_number:
            last_number = int(key[0])
            break

while users_data > 0:
    users_dict = {}
    last_number += 1
    author = str(input("Введите автора книги - "))
    year = str(input("Введите год выпуска книги - "))
    book_name = str(input("Введите название книги - "))
    users_dict[" "] = last_number
    users_dict["Книга"] = book_name
    users_dict["Автор"] = author
    users_dict["Год выпуска"] = year
    users_data -= 1
    books_data.append(users_dict)

user_author = str(input("Введите автора, по которому искать книги"))

for dictin in books_data:
    if user_author == dictin["Автор"]:
        print(dictin["Книга"])
