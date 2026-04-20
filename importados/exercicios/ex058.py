from random import randint
from time import sleep
a = 0
c = 0
num = 0
n = 1
random = str(randint(0,10))
while a != 1:
    #print(random)
    b = str(input('type the number:  '))
    sleep(0.5)
    c = b.isalpha()
    if c == True :
        a = 0
        print('Não pode letras')
        print('Fim do jogo')
    else:
        c = str(b)
        if c >= '1'  or c <= '10':
            if random < c:
                num = 'menor'
            else:
                num = 'maior'
            if c != random:
                print(f'{num}... Tente mais uma vez.')
            else:
                print(f'Acertou com {n} tentativas. Parabéns!')
                a+=1
        else:
            print('only 1 the 10')
        n+=1
