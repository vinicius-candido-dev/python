a = int(input ('qual seu salario'))
if a > 1250:
    s = a*10/100
    print(f'seu salario é R${s + a }')
else:
    s = a * 15/100
    print(f'seu salario é de R${s + a}')
