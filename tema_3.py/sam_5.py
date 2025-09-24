counter = 0
values = [0, 2, 4, 6, 8, 10]
string = 'hello'
while counter != 11:
    if counter in values:
        string = 'hello world'
    else:
        string = 'hello'
    print(string)
    counter += 1
