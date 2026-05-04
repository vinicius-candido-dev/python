def lin():
    print('-'*40)


lin()
print(f"{"I'm absolute":^40}")
lin()
print()
def titulo(xtt):
    print('-'*40)
    print(xtt)


titulo(f'{"msg é top":^40}')
lin()

def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} ')
    print(f'o resultado é {s}')


soma(5, 6)
soma(10, 3)
soma(6, 5)


type = input('type a number:  ')
def mensagem(msg):
    print('-'* len(type))
    print(msg)
    lin()


mensagem('hello angel')