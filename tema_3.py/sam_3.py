n = int(input("Введите число от 0 до 10: "))
if not (0 <= n <= 10):
    print("Некорректный ввод")
else:
    if n <= 3:
        print("от 0 до 3")
    elif n <= 6:
        print("от 3 до 6")
    else:
        print("от 6 до 10")