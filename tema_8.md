# Тема 8. Введение в ООП
Отчет по Теме #8 выполнила:
- Турылева Диана Игоревна
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.
```python
class Car: #Создали класс Car
    def __init__(self,make,model):  #инициализация объекта
        self.make = make
        self.model = model

my_car=Car("Toyota", "Corolla") #создан экземпляр объекта класса
```

### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/lab_1.png)

## Выводы

Эта программа создаёт класс Car с атрибутами марки и модели автомобиля:

- class Car: — объявляет класс Car.
- def __init__(self,make,model): — создаёт конструктор с параметрами марки и модели.
- self.make = make и self.model = model — сохраняют параметры в атрибуты объекта.
- my_car = Car("Toyota", "Corolla") — создаёт экземпляр Car с маркой Toyota и моделью Corolla.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль. 
```python
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")
my_car=Car("Toyota", "Corolla")
my_car.drive()
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/lab_2.png)

## Выводы

Эта программа добавляет метод drive для вывода сообщения о вождении автомобиля:

- Метод drive(self): — добавляет функцию для вывода строки с маркой и моделью.
- my_car.drive() — вызывает метод drive объекта, выводя «Driving the Toyota Corolla».

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
```python
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car=Car("Toyota", "Corolla")
my_car.drive()

class ElectricCar(Car):
    def __init__(self,make,model, battery_capacity):
        super().__init__(make,model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/lab_3.png)

## Выводы

Эта программа демонстрирует наследование, расширяя класс Car классом ElectricCar с дополнительным методом зарядки:

- class ElectricCar(Car): — создаёт класс-наследник ElectricCar от Car.
- Конструктор __init__ с вызовом super() — инициализирует базовые атрибуты и добавляет battery_capacity.
- Метод charge(self): — выводит информацию об зарядке электрокара.
- Объект my_electric_car использует методы классa Car и ElectricCar, демонстрируя наследование.

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car:
    def __init__(self,make,model):
        self._make = make   #Защищённый атрибут
        self.__model = model  #Приватный атрибут

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car=Car("Toyota", "Corolla")
print(my_car._make)
#print(my_car.__model)  #Ошибка! Приватный атрибут не доступен
my_car.drive()
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/lab_4.png)

## Выводы

Эта программа показывает использование защищённых и приватных атрибутов в классе для ограничения доступа к данным:

- Атрибут _make — защищённый, доступен из класса и подклассов, по соглашению от пользователя.
- Атрибут __model — приватный, имя подвергается манглингу и недоступно извне.
- print(my_car._make) — удачный вывод защищённого атрибута.
- Попытка print(my_car.__model) вызовет ошибку из-за приватности.
- Метод drive использует оба атрибута внутри класса.

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

a = Rectangle(15,20)
b = Circle(5)
print(a.area())
print(b.area())
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/lab_5.png)

## Выводы

 Эта программа реализует полиморфизм через абстрактный класс Shape и переопределение метода area в классах Rectangle и Circle:

- class Shape: — базовый класс с методом-заготовкой area().
- class Rectangle(Shape): и class Circle(Shape): — наследуют Shape и реализуют собственный метод area().
- Объекты a и b создают разные фигуры.
- Вызов area() вычисляет и выводит площадь прямоугольника и круга соответственно.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издает звук"

dog = Animal("Дракончик")
print(f"Кличка животного: {dog.name}")
print(dog.speak())
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/sam_1.png)

## Выводы

Эта программа создаёт класс Animal с методом speak и атрибутом имени животного:

- class Animal: — объявляет класс Animal.
- def __init__(self, name): — создаёт конструктор с атрибутом name.
- self.name = name — сохраняет имя животного.
- def speak(self): — метод для вывода звука животного.
- dog = Animal("Дракончик") — создаёт объект с именем "Дракончик".
- print(f"Кличка животного: {dog.name}") — выводит имя животного.
- print(dog.speak()) — вызывает метод speak и выводит звук.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/sam_2.png)

## Выводы

Эта программа расширяет класс Animal добавлением атрибута возраста и метода для вывода этого возраста:

- def __init__(self, name, age): — конструктор теперь принимает имя и возраст.
- self.age = age — сохраняет возраст животного.
- def ages(self): — метод для печати возраста.
- dog = Animal("Дракончик", 4) — создаёт объект с именем и возрастом.
- dog.ages() — выводит возраст животного.
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/sam_3.png)

## Выводы

Эта программа демонстрирует наследование, добавляя класс Bird с методом fly на основе класса Animal:

- class Bird(Animal): — создаёт класс-наследник Bird от Animal.
- super().__init__(name, age) — вызывает конструктор базового класса.
- def fly(self): — добавляет метод fly для птиц.
- Объекты dog и ivolga показывают использование методов из Animal и Bird.
- Вызов ivolga.fly() демонстрирует новую функциональность наследника.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/sam_4.png)

## Выводы

Эта программа использует инкапсуляцию с приватными атрибутами и методами доступа в классах Animal и Bird:

- self.__name и self.__age — приватные атрибуты класса Animal (инкапсуляция).
- Методы get_info() и get_name() — предоставляют доступ к приватным данным.
- В классе Bird метод fly() использует get_name() для доступа к имени.
- Создание объектов и вызовы методов демонстрируют безопасность и доступ к данным через методы.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
### Результат.
![Меню](https://github.com/dermhl/Prog/blob/tema_8/pic/sam_5.png)

## Выводы

Эта программа подсчитывает и выводит количество слов, содержащихся в текстовом файле:

- class Animal: с абстрактным методом make_sound() — базовый класс.
- Классы Dog, Cat, Bird — переопределяют make_sound() с разными реализациями.
- Список объектов animals — хранит разные типы животных.
- Цикл for выводит название класса и соответствующий звук, демонстрируя полиморфизм.


## Общие выводы по теме

Вспомнив основы ООП, попрактиковала моделирование объектов с помощью классов. Освежила в памяти принципы наследования, который позволяет создавать новые классы на базе существующих, расширяя их функционал и избегая дублирования кода, инкапсуляции, которая защищает внутренние данные объектов, делая их недоступными для прямого изменения извне, и полиморфизм, помогающий реализовывать одинаковые методы разным классам по-своему, что делает программу гибкой и легко расширяемой. Эти знания помогают структурировать код, делая его более читаемым и безопасным от внешних воздействий. Понимание принципов ООП позволяет создавать сложные и удобные в поддержке программы и эффективно решает задачи моделирования реальных процессов.
