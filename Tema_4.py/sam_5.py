from imoirt_file import formula

def main():
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    area = formula(a, b, c)
    print(f"Площадь: {area}")

if __name__ == '__main__':
    main()