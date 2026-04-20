while True:
    number = int(input('Qual numéro deseja converter?'))
    converter = input('digite o numero do qual converter\n1-para binário \n2-pára octal\n3-para hexadeximal ')
    if converter == '1':
        print(bin(number)[2:])
    elif converter == '2':
        print(oct(number)[2:])
    elif converter == '3':
        print(hex(number)[2:])
    else:
        print('Invalido')