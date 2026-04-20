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


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO: por favor, digite um número real valido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            real = 0
            break
        else:
            break

    return real


result = {}
i = leiaInt('Digite um número Inteiro:  ')
r = leiaFloat('Digite um número Real:  ')
result['Inteiro'] = i
result['Real'] = r

print(f'O valor inteiro digitado foi {result["Inteiro"]} e o real foi {result["Real"]}')