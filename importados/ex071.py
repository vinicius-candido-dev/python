print('='*30)
print(f'{'BANCO CEV':^30}')
print('='*30) #50,20,10,1
withdraw = int(input('Qual o valor que você deseja sacar?  '))
tot = 0
ced = 50
total = withdraw
while True:
    if total >= ced:
        total -= ced
        tot += 1
    else:
        if tot > 0:
            print(f'Total de {tot} células de R${ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if total == 0:
            break
print('='*30)
