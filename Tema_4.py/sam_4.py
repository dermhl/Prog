def srednee(*args): #объявление функции с аргументом в виде кортежа
    args = [float(arg) for arg in args] #преобразуем аргументы в список в формате float
    col_vo = len(args)
    result = sum(args) / col_vo
    print(result)

if __name__ == '__main__':
    srednee(2, 6, 9, 1, 7, 13, 2)