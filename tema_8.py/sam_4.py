class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def speak(self):
        return f"{self.__name} издает звук"

    def get_info(self):
        return f"Кличка животного: {self.__name}\nВозраст: {self.__age}"

    def get_name(self):
        return self.__name

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fly(self):
        print(f"{self.get_name()} умеет летать")


dog = Animal("Дракончик", 4)
print(dog.get_info())
print(dog.speak())

ivolga = Bird("Иволга Инесса", 2)
print(ivolga.get_info())
print(ivolga.speak())
ivolga.fly()