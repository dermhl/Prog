def uniqel(lst):
    elements = set(lst)
    return len(elements), list(elements)

test1 = [1, 2, 2, 3, 4, 4, 5]
test2 = [10, 10, 10, 20, 30]
test3 = [7, 8, 9, 7, 8]

print(uniqel(test1))
print(uniqel(test2))
print(uniqel(test2))