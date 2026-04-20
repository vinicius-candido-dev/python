c = 0
cont = 0
for a in range(0,6):
    number = int(input('type number:  '))
    if number % 2 == 0:
        c += number
        cont += 1
print(c , cont )