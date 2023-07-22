import itertools
import random

nums = [random.randint(0, 10 + 1) for i in range(10 + 1)]
combinations = []
a = 10
for r in range(1, len(nums) + 1):
    comb = list(itertools.combinations(nums, r))
    for i in comb:
        if sum(i) == a:
            combinations.append(i)
print(combinations)
print(nums)
