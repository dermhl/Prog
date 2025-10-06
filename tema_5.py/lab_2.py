#вариант 1
a = set('abcdefg')
print(a)
for i in range(1,5):
    a.add(i)
print(a)

#вариант 2
b = frozenset('abcdefg')
print(b)
for j in range(1,5):
    b.add(j)
print(b)
