a = int(input("Введите первое число - "))
b = int(input("Введите второе число - "))
sum = 0
for i in range(a, b + 1):
    sum += i
print(sum)