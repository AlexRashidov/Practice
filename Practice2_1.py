import random

colors = ["green", "red", "blue", "black", "orange"]

for color in colors:
    print(color)

flag = False

random_item = random.randint(0, 4)
random_color = colors[random_item]

while not flag:
    user_color = str(input("Угадайте цвет(выберите из предложенных)"))
    if user_color == random_color:
        flag = True
        print("Отлично!")
        break
    elif random_color == "red":
        print("Попробуй еще раз, подсказка: Какого цвета кровь?")
    elif random_color == "green":
        print("Попробуй еще раз, подсказка: Какого цвета трава летом?")
    elif random_color == "blue":
        print("Попробуй еще раз, подсказка: Какого цвета небо?")
    elif random_color == "black":
        print("Попробуй еще раз, подсказка: Какого цвета темнота?")
    elif random_color == "orange":
        print("Попробуй еще раз, подсказка: Какого цвета апельсин?")
    else:
        print("Попробуй еще раз")
