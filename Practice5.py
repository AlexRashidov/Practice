win = 3
lose = 0
tied = 1
flag = False
while flag == False:
    score = int(input("Введите кол - во очков команды за игру(0,1,3)"))
    if score == win or score == lose or score == tied:
        if score == win:
            print("Выигрыш")
            break
        elif score == lose:
            print("Проигрыш")
            break
        elif score == tied:
            print("Ничья")
            break
        else:
            print("Некорректное число очков")


