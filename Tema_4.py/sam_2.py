from random import randint

def kubik():
    storona = randint(1,6)
    print(f"Значение на стороне кубика: {storona}")
    if storona in [1,2]:
        print("Вы проиграли")
    elif storona in [3,4]:
        kubik()
    else:
        print("Вы победили")

if __name__ == '__main__':
    kubik()