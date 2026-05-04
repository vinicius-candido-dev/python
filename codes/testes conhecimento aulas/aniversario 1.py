import tkinter as tk
def aniver(manual=False):
    if manual==False:
        from datetime import date
        month = date.today().month
        day = date.today().day
    if manual==True:
        month = int(input('informe o mês que deseja saber:  '))
        day = int(input('informe o dia que deseja saber:'))
    if month == 2 and day > 30:
        print ('Invalido')
    elif month and day > 30:
        print ('Invalido')
    elif month == 6 and day > 30:
        print('Invalido')
    elif month == 9 and day > 30:
        print('Invalido')
    elif month == 11 and day > 30:
        print('Invalido')
    elif month == 1 and day > 31:
        print('Invalido')
    elif month == 3 and day > 31:
        print('Invalido')
    elif month == 5 and day > 31:
        print('Invalido')
    elif month == 7 and day > 31:
        print('Invalido')
    elif month == 8 and day > 31:
        print('Invalido')
    elif month == 10 and day > 31:
        print('Invalido')
    elif month == 12 and day > 31:
        print('Invalido')
    elif month == 13:
        print('Invalido')
    # aniversario
    #1-Janeiro
    if month == 1:
        if day == 4:
            return  'Aniversário da Mamãe'
        elif day == 14:
            return 'Anivérsario da vitória'
        elif day == 18:
            return 'Aniversário da Thay'
        elif day == 20:
            return 'aniversário da Lily'
    #2-Fevereiro
    elif month == 2:
        if day == 25:
            return 'Aniversário de Gustavo'
    #3-Março
    elif month == 3:
        if day == 8:
            return 'Dia Internacional das Mulheres'
    #4-Abril
    elif month == 4:
        if day == 3:
            return 'Sexta-feira Santa'
        elif day == 15:
            return 'Aniversário do Angelo'
        elif day == 21:
            return 'Tiradentes'
    #5-Maio
    elif month == 5:
        if day == 1:
            return 'Aniversário de Paulo Junior \n Dia do Trabalho'
        elif day == 2:
            return 'Aniversário de Mel'
    #6-Junho
    elif month == 6 and day == 26:
        print('Aniversário da Mari')
    #7-Julho
    #8-Agosto
    #9-Setembro
    elif month == 9 and day == 7:
        print('independência do Brasil')
    #10-Outubro
    elif month == 10 and day == 6:
        print('Aniversário da Franciely, inclusive ela nasceu em 2009')
        print('Palavras dela do dia 24 de Dezembro de 2025: \033[0:34m "Eu vou namorar em 2026 com um loiro de olho verde, alto, podre de rico e da igrejaaa" \033[m ')
        print('Correção do dia 3 de janeiro de 2026:\033[35m "Ele é moreno,Nasceu dia 27/11 de 2009, e Tem cara de coitado"\033[m')
        print('Palavras dela no dia 10 de janeiro:\033[36m "Projeto loiro ainda está de pé, Eu viii um hojeeeeee na ruaaaaaaaaa, Do olho bem azullll 😍😍😍😍😍,Affs namoraaa😭 "\033[m ')
        print('Palavras do dia 15 de janeiro:  \033[32m"Eu tenho um gosto especifico,es tu" \033[m')
        print('10 de fevereiro as 6 da manhã: \033[33m"Começamos a namorar"\033[m')
    elif month == 10 and day == 12:
        print('feriado Nossa Senhora Aparecida')
    #11-Novembro
    elif month == 11 and day == 2:
        print('Finados')
    elif month == 11 and day == 15:
        print('Proclamação da República')
    elif month == 11 and day == 20:
        print('Dia Nacional de Zumbi e da Consciência Negra ')
    #12-Dezembro
    elif month == 12 and day == 12:
        print('Aniversário de @marianealvesdeoli1')
    elif month == 12 and day == 25:
        print('Natal')
    else:
        print('Nehuma data para esse dia.')
    print()
    input('Digite ENTER para sair')














# 1. Definir a função que o botão chamará

# Cria a janela principal
janela = tk.Tk()
# Define o título da janela
janela.title("Minha Primeira Interface")
# Define o tamanho da janela (largura x altura) - Ajustado para ser mais visível
janela.geometry("400x300")
variável = aniver()
# Botão com texto entre aspas e comando correto
botao = tk.Button(janela, text="Clica aqui", command=aniver)
# pady menor para melhor visualização
botao.pack(pady=20)

# Label inicial

label = tk.Label(janela, text="Aguardando...")
label.pack(pady=10)

# Inicia o loop principal que mantém a janela aberta
janela.mainloop()