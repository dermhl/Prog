def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n = int(input("Введите количество чисел Фибоначчи: "))
    for num in fib(n):
        print(num)