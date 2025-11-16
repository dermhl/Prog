import time

# Декоратор для измерения времени выполнения функции
def izmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

@izmer
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 100
result = fibonacci(n)
print(f"F({n}) = {result}")