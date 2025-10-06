a_list = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
b_list = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
c_list = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print("\n\nСтарый массив\n",a_list)
print("Новый массив: ")
for value in a_list:
    if value == 2 or value == 3:
        value = 4
        new_value = value
        print(new_value, end=' ')
    else:
        new_value = value
        print(new_value, end=' ')

print("\n\nСтарый массив\n",b_list)
print("Новый массив: ")
for valu in b_list:
    if valu == 2 or valu == 3:
        valu = 4
        new_valu = valu
        print(new_valu, end=' ')
    else:
        new_valu = valu
        print(new_valu, end=' ')

print("\n\nСтарый массив\n",c_list)
print("Новый массив: ")
for val in c_list:
    if val == 2 or val == 3:
        val = 4
        new_val = val
        print(new_val, end=' ')
    else:
        new_val = val
        print(new_val, end=' ')