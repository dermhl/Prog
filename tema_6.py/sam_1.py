data = input("Введите числа, разделённые пробелом: ")
list_numbers = [int(x) for x in data.split()]
tuple_numbers = tuple(list_numbers)

print("Список:", list_numbers)
print("Кортеж:", tuple_numbers)