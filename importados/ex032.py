#ano bissesto
from datetime import date

ano = int(input('qual ano voce quer saber? digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4== 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'esse ano {ano} é bissesto')
else:
    print(f'esse ano {ano} não é bissesto')