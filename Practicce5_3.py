import csv

books_data = []

with open("books.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        books_data.append(row)
try:
    year_start = int(input("Введите начальный год"))
    year_end = int(input("Введите конечный год"))
except ValueError:
    print("Вводите только число")
    exit()

for dict in books_data:
    if year_start <= int(dict["Год выпуска"]) <= year_end:
        print(dict["Книга"])
