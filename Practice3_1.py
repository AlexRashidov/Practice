import functools
nums = [12,39,12,55,2,3,1]
len = len(nums)
avg = functools.reduce(lambda x,y: x + y,nums )/ len
print("avg", round(avg,3))