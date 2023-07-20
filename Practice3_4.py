import math
a = 0
b = 100
square = []
for i in range(a,b + 1):
    if math.sqrt(i) == round(i**0.5):
        square.append(i)
print(square)
