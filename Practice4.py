num = int(input("Введите число от 10 до 20\n"))
flag = False
while not flag:
    if num < 10:
        print("Введенное числов меньше 10")
        num = int(input("Введите число от 10 до 20\n"))
    elif (num > 20):
        print("Введенное числов больше 20")
        num = int(input("Введите число от 10 до 20\n"))
    else:
        flag = True
        print(num, "Спасибо")
