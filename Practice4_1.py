import itertools
a = 123
mx = float("-inf")
perm = list(itertools.permutations(str(a), 3))
print(perm)
for num in perm:
    result = "".join(num)
    if int(result) > mx:
        mx = int(result)
print(mx)
