nums  = []

first = int(input("Введите первое число - "))
nums.append(first)
second = int(input("Введите второе число - "))
nums.append(second)
third = int(input("Введите третье число - "))
nums.append(third)

if (first > second) and (first > third):
    print("Наибольшее число - ", first)
elif (second > first) and (second > third):
    print("Наибольшее число - ", second)
elif (first == second == third):
    print("Наибольшего нет, числа равны")
else: print("Наибольшее число - ", third)
r_nums = list(reversed(sorted(nums)))
print(r_nums)