from datetime import date
today = date.today().year
birth = int(input('Qual a sua data de nascimento? '))
category = today - birth
if category <9:
    print('Mirim')
elif 10 >=  category <=14:
    print('Infantil')
elif  15>= category <=19:
    print('Junior')
elif 19 >= category <=20:
    print('Sênior')
elif category >20:
    print('Master')