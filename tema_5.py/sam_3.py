import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_1 = max(one)
max_2 = max(two)
max_3 = max(three)
p = 0.5*(max_1 + max_2 + max_3)
area_1 = math.sqrt(p*(p-max_1)*(p-max_2)*(p-max_3))
print("Площадь максимального треугольника: ", round(area_1, 2))

min_1 = min(one)
min_2 = min(two)
min_3 = min(three)
polu = 0.5*(min_1 + min_2 + min_3)
area_2 = math.sqrt(polu*(polu-min_1)*(polu-min_2)*(polu-min_3))
print("Площадь минимального треугольника: ",round(area_2, 2))