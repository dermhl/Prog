def func(event, id):
    try:
        first_idx = event.index(id)
    except ValueError:
        return ()

    try:
        second_idx = event.index(id, first_idx + 1)
        return event[first_idx:second_idx + 1]
    except ValueError:
        return event[first_idx:]

print(func((1, 2, 3), 8))
print(func((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(func((1, 2, 8, 5, 1, 2, 9), 8))