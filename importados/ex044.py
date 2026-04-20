product = int(input('informe o valor do produto: '))
print(f'''Qual a forma de pagamento?
1-Á vista dinheiro/cheque:10% de desconto 
2-Á vista no cartão: 5% de desconto 
3-Em até 2x no cartão: preço normal 
4-3x ou mais no cartão: 20% de juros''')
form = input('informe o valor do produto: ')
if form == '1':
    payment = product- (product /10)
    print(payment)
elif form == '2':
    payment = product -(product *0.05)
    print(payment)
elif form == '3':
    payment = (product /2)
    print(f'vc vai pagar {payment} em 2 mêses')
elif form == '4':
    installment = int(input('Deseja pagar em quantas vezes: '))
    fees = product * 0.2
    payment = (product + fees)  / installment
    print(payment)
else:
    print('digite apenas numéros de 1 a 4')
