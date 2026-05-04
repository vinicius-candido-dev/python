numeros_extensos = ("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
                    "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
cont = 'S'
while cont != 'N':
    number = int(input('Digite um número de 0 a 20:   '))
    if 0 < number > 20:
                print('Tente novamente.', end=' ')

    print(f'você digitou o número \033[1:34m{numeros_extensos[number]}\033[m')
    cont = input('Deseja continuar? [S/N] ').upper().strip()[0]