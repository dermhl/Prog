file = 'tema_10.txt'

try:
    with open(file, 'r') as f:
        content = f.read()
        if not content:
            raise ValueError("Файл пустой")
        else:
            print("Содержимое файла:")
            print(content)
except FileNotFoundError:
    print("Файл не найден.")
except ValueError as e:
    print("файл пустой")