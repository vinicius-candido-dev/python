weight = float(input('informe o seu peso: '))
height = float(input('informe o sua altura: '))
imc = weight / (height ** 2)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif  18.5 >=  imc <= 25:
    print('Peso ideal')
elif  25 >= imc <= 30:
    print('Sobrepeso')
elif   30 >= imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')