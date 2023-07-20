import collections
string = "asdjasowooweasodpoorhrwifllnsasdfghjkxcvbnmrtyuiop"
result_str = ""
f = collections.Counter(string).most_common()
for i in f:
    if i[1] == 1:
        result_str += i[0]
count = len(result_str)
d = {result_str: count}
print(d)