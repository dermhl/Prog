class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Декоратор: перед вызовом функции '{self.func.__name__}'")
        result = self.func(*args, **kwargs)
        print(f"Декоратор: после вызова функции '{self.func.__name__}'")
        return result

@MyDecorator
def greet(name):
    print(f"Привет, {name}!")

@MyDecorator
def multiply(a, b):
    print(f"Произведение {a} и {b} равно {a * b}")

if __name__ == "__main__":
    greet("Вовочка")
    multiply(5, 10)