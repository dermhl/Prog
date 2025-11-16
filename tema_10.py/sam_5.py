class InvalidAgeError(Exception):
    pass

def check_age_18(age):
    if age < 18:
        raise InvalidAgeError(f"Доступ запрещен: возраст {age} меньше 18.")
    else:
        print(f"Доступ разрешен, возраст {age} подходит.")

def check_age_for_driving(age):
    if age < 16:
        raise InvalidAgeError(f"Нельзя сдавать экзамен: возраст {age} меньше 16.")
    else:
        print(f"Можно сдавать экзамен, возраст {age} подходит.")

try:
    check_age_18(15)
except InvalidAgeError as e:
    print(f"Ошибка при проверке входа: {e}")

try:
    check_age_for_driving(14)
except InvalidAgeError as e:
    print(f"Ошибка при проверке на вождение: {e}")

try:
    check_age_18(20)
except InvalidAgeError as e:
    print(f"Ошибка при проверке входа: {e}")

try:
    check_age_for_driving(18)
except InvalidAgeError as e:
    print(f"Ошибка при проверке на вождение: {e}")
