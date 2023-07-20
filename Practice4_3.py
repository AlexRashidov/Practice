def isPrime(x): #Функция, чтобы определить простоту числа
    dl = []
    ln = 0
    for i in range(1,x + 1):
        if (x % i) == 0:
            dl.append(i)
    if len(dl) == 2: #если длина списка делителей числа == 2, то число простое, если  останется 0, то число составное
        ln = len(dl)
    return ln

a = 1
b = 100
nums = []
for num in range(a, b + 1):
    check = isPrime(num)
    if check == 2:
        nums.append(num)
print(nums)

