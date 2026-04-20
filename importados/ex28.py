import random
a = input('voce quer escolher as rodadas? [N/S]').upper()
if a == 'N':
    while True:
        N = int(input ('adivinhe um numero de 0 a 5:'))
        numero = random.randint(0,5)
        if N == numero:
            print (f'\033[0;32mparabens voce acertou o numero, o numero era {N}\033[0;31m')
        elif N > 5:
            print('Numero invalido')
        else:
            print(f'\033[0;31mvoce perdeu, o numero era {numero} \033[0;31m')
            print('')
        print('\033[97mFIM DO jOGO \033[m')
        print('')


elif a == 'S':
    #contador = 1
    b = int(input('Quantas rodadas?'))
    #while contador <= b:
    for c in range (1,b+1):
        N = int(input('adivinhe um numero de 0 a 5:'))
        numero = random.randint(0, 5)
        if N == numero:
            print(f'\033[0;32mparabens voce acertou o numero, o numero era {N}\033[0;31m')
        elif N > 5:
            print('Numero invalido')
        else:
            print(f'\033[0;31mvoce perdeu, o numero era {numero} \033[0;31m')
            print('')
        print('\033[97mFIM DO jOGO \033[m')
        print('')
        #contador = contador + 1
        print('Jogo finalizado com sucesso!')



else:
    print('Voce nao digitou S ou N')
input('pressione ENTER para sair')



