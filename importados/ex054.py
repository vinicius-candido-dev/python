from datetime import date
b = d = 0
for c in range(1, 8):
    birth = int(input(f'Em que ano a {c}ª pessoa nasceu?  '))
    year = date.today().year
    a = year - birth
    if a >= 18:
        b+=1
    else:
        d+=1
print(f'ao todo tivemos {b} pessoas maiores de idade \ne também tivemos {d}  pessoas menores de idade')
