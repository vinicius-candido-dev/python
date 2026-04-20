from datetime import date
birth_today = date.today().year
birth = int(input('Digite o seu ano de nascimento: '))
verify = birth_today - birth
print(f'Quem nasceu em {birth} tem {verify} anos em {birth_today}.')
if verify < 18:
    saldo = verify - 18
    print('Voce ainda nao tem que se alistar, ainda falta {} anos'.format(saldo))
    print(f'seu alistamento sera em {birth_today + saldo}. ')

elif verify == 18:
    print('Voce tem que se alistar!')

elif verify > 18:
    saldo = verify - 18
    print('O tempo de alistamneto já passou, deveria ter se alistado a {} anos'.format(saldo))
    print(f'seu alistamento foi em {birth_today - saldo} ')
