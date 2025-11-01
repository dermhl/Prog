class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} издает звук"
    def ages(self):
        print(f"Возраст: {self.age} ")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fly(self):
        print(f"{self.name} умеет летать")

dog = Animal("Дракончик", 4)
print(f"Кличка животного: {dog.name}")
dog.ages()
print(dog.speak())

ivolga = Bird("Иволга Инесса", 2)
print(f"Кличка животного: {ivolga.name}")
ivolga.ages()
print(ivolga.speak())
ivolga.fly()