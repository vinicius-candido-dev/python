v = int(input ('qual era a velocidade do veiculo em km/h?'))
if v > 80:
    print('voce foi multado')
    m = (v - 80)*7
    print (f'O valor da sua multa é de R$\033[31m{m}.')
else:
    print ('muito bem voce esta no limite de velocidade pode seguir')