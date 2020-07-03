def convert(value):
    cent = round(value * 100)
    coin = 0
    while True:
        if cent == 0:
            break
        elif cent >= 25:
            cent -= 25
            coin += 1
        elif cent >= 10:
            cent -= 10
            coin += 1
        elif cent >= 5:
            cent -= 5
            coin += 1
        else:
            cent -= 1
            coin += 1
    return coin


while True:
    change = input('Change owed: ')
    if change.replace('.', '').isdigit() and float(change) > 0:
        print(convert(float(change)))
        break