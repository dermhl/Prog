class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издает звук"

dog = Animal("Дракончик")
print(f"Кличка животного: {dog.name}")
print(dog.speak())