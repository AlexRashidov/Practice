nums_keys = [i for i in range(1, 10 + 1) if (i % 2 == 0)]
value = [i**3 for i in range(1, 10 + 1) if (i % 2 == 0)]
d = dict(zip(nums_keys, value))
print(d)
