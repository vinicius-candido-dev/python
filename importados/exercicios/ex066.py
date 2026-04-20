soma = cont =  0
while True:
    num = int(input('type the number [999 break]:  '))
    if num == 999:
        break
    soma += num
    cont+=1
print(f'a soma desses numeros é de {soma}, e o total de números digitados é de {cont}')
