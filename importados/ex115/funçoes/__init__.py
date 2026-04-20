def lis(lis=50):
    print('-' * lis)


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


def menu():
    lis()
    print(f'{"MENU PRINCIPAL":^{50}}')
    lis()
    print(f'\033[33m1 - \033[34m Ver pessoas cadastradas\033[m ')
    print(f'\033[33m2 - \033[34m Cadastrar nova Pessoa\033[m')
    print(f'\033[33m3 - \033[34m Sair do Sistema\033[m')
    lis()


def ver_cadras():
    lis()
    print(f'{"PESSOAS CADASTRADAS":^50}')
    lis()


def cabeçalho(txt):
    lis()
    print(f'{txt:^50}')
    lis()


def opc():
    while True:
        try:
            opct = int(input('\033[33mSua Opção:  \033[m'))
        except (ValueError, TypeError):
            print('\033[31mERROR: Por favor, informe uma das opções  \033[m')
        else:
            if opct == 0 or opct > 3:
                print('\033[31mERROR: Por favor, informe um búmero válido\033[m')
            else:
                break
    return opct


def sair():
    lis()
    print(f'{"Saindo do sistema... Até logo!":^50}')
    lis()
