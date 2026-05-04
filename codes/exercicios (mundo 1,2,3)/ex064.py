b = 0
cont = 0
soma = 0
b = int(input('Digite um numero: '))
while b != 999:
    soma +=b
    cont +=1
    b = int(input('Digite um numero: '))
print(f'Quantos numeros foram digitados {cont} e a soma é de {soma}')