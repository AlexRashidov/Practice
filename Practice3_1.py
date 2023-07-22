import functools

nums = [12, 39, 12, 55, 2, 3, 1]
ln = len(nums)
avg = functools.reduce(lambda x, y: x + y, nums) / ln
print("avg", round(avg, 3))
