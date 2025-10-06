his_list = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

besters = sorted(his_list)[:3]  #сортировка по возрастанию
print("Три лучших результата: ", besters)

worsters = sorted(his_list)[-3:]    #выбирает 3 последних результата
print("Три худших результата: ", worsters)

for value in his_list:
    if value >= 10:
        print(value, end=' ')