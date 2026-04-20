def linha(quant=30):
    print('-' * quant)


def interface(text):
    linha()
    print(f'{text:^30}')
    linha()

def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! por favor, digite um número inteiro valido\033[m')
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            inteiro = 0
            break
        else:
            break
    return inteiro


def menu(msg):
    print(f'{"Menu principal"}')
    print(f'1 - Ver tudo')
    linha()
    num = leiaInt(msg)
    linha()
    return num