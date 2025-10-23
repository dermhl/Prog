import os

f = 'expen.txt'
def load_expenses():
    """Загрузка списка расходов из файла"""
    expenses = []
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    expenses.append(line)
    return expenses


def save_expense(expense_str):
    """Добавление новой записи расхода в файл"""
    with open(f, 'a', encoding='utf-8') as file:
        file.write(expense_str + '\n')


def add_expense():
    """Запрос у пользователя данных для нового расхода и из созранение"""
    date = input("Введите дату (например, 2023-10-20): ")
    amount = input("Введите сумму: ")

    expense_str = f"{date}| {amount}"
    save_expense(expense_str)
    print("Расход добавлен!")


def show_expenses():
    """Вывод всех сохранённых расходов"""
    expenses = load_expenses()
    if not expenses:
        print("Нет записей расходов.")
    else:
        print("\nТекущие расходы:")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense}")


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить расход")
        print("2. Посмотреть расходы")
        choice = input()

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()



if __name__ == "__main__":
    main()