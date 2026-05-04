house = float(input('Qual o valor da casa: R$'))
salary_of_buyer = float(input('Qual o seu salário:   R$'))
year = int(input('Quantos anos deseja pagar: R$'))
monthly = house/(year*12)
#month = year * 12
#monthly = (house / month)
validation = salary_of_buyer * 30/100
if monthly <= validation:
    print(f'Emprestimo concedido para pagar uma cada de {house}0 o valor mensalmente é de {monthly:.2f}0')
else:
    print(f'Para pagar uma cada de {house},00 o valor mensalmente é de {monthly:.2f}')
    print(f'Você não pode pagar')
