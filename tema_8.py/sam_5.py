class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

class Bird(Animal):
    def make_sound(self):
        return "Чик-чирик!"

animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.make_sound()}")