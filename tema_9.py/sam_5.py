class Tomato:
    states = ["отсутствует", "цветёт", "зелёный", "красный"]  # статическое свойство

    def init(self, index):
        # Динамические свойства, определяются в методе init:
        self._index = index      # индекс текущей стадии (приватное свойство)
        self._state = self.states[self._index]  # текущая стадия (приватное свойство)

    def grow(self):
        if self._index < len(self.states) - 1:
            self._index += 1
            self._state = self.states[self._index]

    def is_ripe(self):
        return self._state == "красный"

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato() for _ in range(num)]  # создаём пустые объекты Tomato
        for tomato in self.tomatoes:
            tomato.init(0)  # инициализируем каждый томат в начальном состоянии

    def __str__(self):
        return f"Куст с {len(self.tomatoes)} томатами"

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name            # публичное свойство
        self._plant = plant         # приватное свойство

    def __str__(self):
        return f"Садовник {self.name} ухаживает за {self._plant}"

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Все томаты созрели! Урожай собран.")
            self._plant.give_away_all()
        else:
            print("Некоторые томаты еще не созрели. Подождите немного.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Следите за стадиями созревания томатов.")
        print("2. Регулярно поливайте растения.")
        print("3. Удаляйте больные и повреждённые плоды.")
        print("4. Собирайте урожай, когда все плоды созреют.")

plant = TomatoBush(4)
gardener1 = Gardener("Иван", plant)
for _ in range(3):
    gardener1.work()
result = gardener1.harvest()
if result:
    print("Урожай собран:", result)
else:
    print("Томаты еще не готовы к сбору.")
