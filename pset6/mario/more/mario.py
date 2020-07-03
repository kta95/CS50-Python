def build_pyramid(h):
    for i in range(1, h+1):
        print((' ' * (h - i)) + "#" * i + "  " + "#" * i)


while True:
    height = input('Height: ')
    if height.isdigit() and 1 <= int(height) <= 8:
        build_pyramid(int(height))
        break