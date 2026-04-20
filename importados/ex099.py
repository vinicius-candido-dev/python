from time import sleep


def maior(* num):
    print('-=' * 40)
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c}', end=' ',flush=True)
        sleep(0.5)
    print(f'foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print(f'O maior valor informado foi de 0')
    else:
        print(f'O maior valor informado foi {max(num)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()