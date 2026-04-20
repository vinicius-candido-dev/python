import random
while True:
    user = ['p','t','s','p','t','s','p','t','s']
    jogada = random.choice(user)
    jogada2 = input('escolha entre esses \033[1m.\n  S \033[m para Pedra.\n \033[1m P \033[m para Papel.\n \033[1m T \033[m para Tesoura.\nqual sua escolha?:')

    print(f'Escolha da maquina foi {jogada}')
    if jogada == jogada2:
        print('\033[34m Empate \033[m')
#tesoura x papel
    elif jogada == 't' and jogada2 == 'p':
        print('\033[31m Maquina venceu \033[m')

#tesoura x pedra
    elif jogada == 't' and jogada2 == 's':
        print('\033[32m Você venceu \033[m')

#papel x tesoura
    elif jogada == 'p' and jogada2 == 't':
        print('\033[32m Você venceu\033[m')

#papel x pedra
    elif jogada == 'p' and jogada2 == 's':
        print('\033[31m Maquina venceu\033[m')
#pedra x tesoura
    elif jogada == 's' and jogada2 == 't':
        print('\033[31m Maquina venceu\033[m')
#pedra x papel
    elif jogada == 's' and jogada2 == 'p':
        print('\033[31m Voce venceu \033[m')
    else:
        print('INVALIDO')
    print('')
