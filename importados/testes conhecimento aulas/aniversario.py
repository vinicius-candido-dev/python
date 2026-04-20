month = float(input('qual o mês ?'))
day = float(input('qual o dia ?'))
if month == 2 and day > 30:
    print( 'Invalido')
elif month == 4 and day > 30:
    print ('Invalido')
elif month == 6 and day > 30:
    print ('Invalido')
elif month == 9 and day > 30:
    print ('Invalido')
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
elif month == 1 and day == 4:
    print('Aniversário da Mamãe')
elif month == 1 and day == 14:
    print('Anivérsario da vitória ')
elif month == 1 and day == 18:
    print('Aniversário da Thay')
elif month == 1 and day == 20:
    print('aniversário da Lily')
#2-Fevereiro
elif month == 2 and day == 25:
    print('Aniversário de Gustavo')
#3-Março
#4-Abril
elif month == 4 and day == 3:
    print(' Sexta-feira Santa')
elif month == 4 and day == 15:
    print('Aniversário do Angelo')
elif month == 4 and day == 21:
    print('Tiradentes')
#5-Maio
elif month == 5 and day == 1:
        print ('Aniversário de Paulo Junior')
if month == 5 and day == 1:
    print('Dia do Trabalho')
elif month == 5 and day == 2:
    print ('Aniversário de Mel')
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
    print('começamos a namorar dia 10 de fevereiro as 6 horas da manha')
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
    print('Anivérsario da @marianealvesdeoli1')
elif month == 12 and day == 25:
    print('Natal')
else:
    print('Nehuma data para esse dia.')