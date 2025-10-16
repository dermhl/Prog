def remove(t, el):
    if el not in t:
        return t
    index = t.index(el)
    return t[:index] + t[index+1:]

print(remove((1, 2, 3), 1))
print(remove((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove((2, 4, 6, 6, 4, 2), 9))