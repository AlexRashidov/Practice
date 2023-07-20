import csv

books_data = [
    (" ", "Книга", "Автор", "Год выпуска"),
    ["0", "Metro 2035", "Gluhovskiy", "2004"],
    ["1", "Cso", "Viltor", "5825"],
    ["2", "Robinson", "PZ", "1924"],
]

with open("books.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(books_data)
