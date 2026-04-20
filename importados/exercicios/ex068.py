from random import randint
cont = 0
while True:
    number = randint(0,10)
    jogada = int(input('diga um  valor:  '))
    im_par = input('Par ou ímpar [P/I]  ').upper().strip()[0]
    soma = (number + jogada)
    print('PAR' if soma == 0 else 'IMPAR')
    if  im_par == 'I':
        if soma % 2 ==1:
            print('\033[32mO resultador foi IMPAR você ganhou\033[m')
            cont += 1
        else:
            print(f'\033[31;1mO resultado foi PAR você perdeu\033[m')
            break
    if im_par == 'P':
        if soma % 2 == 0:
            print('\033[32mO O resultado foi PAR você venceu\033[m')
            cont += 1
        else:
            print('\033[31mO resultado foi IMPAR você perdeu\033[m')
            break
print('GAME OVER')
print(f'Você venceu {cont} vezes.')