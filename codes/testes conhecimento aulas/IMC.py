a = float(input (' informe sua altura em metros:'))
b = float(input (' informe seu peso em kg:'))
imc = b/(a * a)
print ('O calculo para saber seu peso é saudavel')
print ( f'seu IMC é \033[34m{imc:.1f}\033[m')
if imc < 18.5:
    print('\033[31mPeso inferior ao ideal\033[m')
elif imc >= 18.5 and imc <= 25:
    print ('\033[32mpeso ideal\033[m')
elif imc >= 25.1 and imc <= 29.9:
    print('\033[31mexcesso de peso\033[m')
elif imc >= 30 and imc <= 34.9:
    print('\033[31mObesidade leve\033[m')
elif imc >= 35 and imc <= 39.9:
    print('\033[31mObesidade moderada\033[m')
else:
    print('\033[31mObesidade morbita\033[m')
