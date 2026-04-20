a = 0
while a != 1:
    number = float(input('type one number: '))
    number1 = float(input('type other  number: '))
    print('Menu')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair do programa')
    options = input('qual a opcao? ')
    if options == '1':
        soma = number + number1
        print('a resultado da soma é {}'.format(soma))
        a += 1
    elif options == '2':
        multi = number1 * number1
        print('a resultado da multiplicação é {}'.format(multi))
    elif options == '3':
        if number1 > number:
            print ('maior é {}'.format(number1))
            a += 1
        elif  number > number1  :
            print('maior é {}'.format(number))
            a += 1
        else:
            print('Os 2 valores são iguais')
            a += 1

    elif options == '4':
        a = 0

    elif options == '5':
        a+=1
        print('Programa finalizado')

