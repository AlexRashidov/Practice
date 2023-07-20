import re
string = "dsafgfjnhjkjiooi"
result = []
res = []
for let in range(len(string)):
    for j in range(let + 1, len(string) + 1):
        result.append(re.sub(r'\W+', '', string[let:j]))
print(result)
for st in result:
    if st == st[::-1]:
        res.append(st)
print(res)
