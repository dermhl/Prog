from collections import Counter

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def podschet(posledovatelnost):
    colvo = Counter(posledovatelnost)
    result_set = set()
    for num, count in colvo.items():
        # добавляем сами числа
        result_set.add(num)
        # если число повторяется, добавляем строки длиной от 2 до count
        if count != 1:
            for i in range(2, count + 1):
                result_set.add(str(num) * i)
    return result_set

set_1 = podschet(list_1)
set_2 = podschet(list_2)
set_3 = podschet(list_3)

print(set_1)
print(set_2)
print(set_3)
