class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} издает звук"

    def ages(self):
        print(f"Возраст: {self.age} ")

dog = Animal("Дракончик", 4)
print(f"Кличка животного: {dog.name}")
dog.ages()
print(dog.speak())