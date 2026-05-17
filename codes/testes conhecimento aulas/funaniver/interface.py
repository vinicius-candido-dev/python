import função
import tela
from time import sleep
from rich import print

while True:
    # se existe
    função.existe("birthdays.txt")
    #tela
    tela.cabeçalho("Aniversário", 70)
    tela.menu("Menu de informações", 70)
    choice = int(input('Qual sua escolha?  '))
    try:

        if choice == 1:
            name = input("Qual o nome da pessoa a ser cadastrada: ").capitalize()
            day = int(input(f"Digite o dia desse aniversário de {name}:  "))
            month = int(input(f"Digite o mes desse aniversário de {name}:  "))

            função.add(day,month,name)
        elif choice == 2:
            print()
            #print(all())
            try:
                with open("birthdays.txt", 'r', encoding="utf-8") as f:
                    for line in f:
                        lin = line.strip().split(',')
                        obj = {
                            "day": lin[0],
                            "month": lin[1],
                            "name": lin[2]}

                        print(f'A pessoa {obj["name"]} no mês {obj["month"]} no dia {obj["day"]}')

            except Exception as e:
                print(f"Erro em {e}")


        elif choice == 3:
            função.aniversario_hoje()

        elif choice == 4:
            day = int(input("Qual o dia que você deseja saber?  "))
            month = int(input("Qual o mês que você deseja saber?  "))
            print(função.especificar(day,month))

        elif choice == 5:
            break
        else:
            print('Por favor, digite numero de 1 a 4')
    except:
        print( f"Erro, número invalido")
    finally:
        sleep(3)


