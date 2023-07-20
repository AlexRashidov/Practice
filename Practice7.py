string = str(input("Введите любое предложение"))
x = ""
for c in string:
    if c.isupper():
        x += c.lower()
    if c.islower():
        x += c.upper()
print(x)
