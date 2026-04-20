spent = one_thousand = a = 0
cheap = 0
while True:
    a +=1
    print('-='*15)
    name = input('Qual o nome do produto?  ').capitalize()
    price = float(input('Qual o preço do produto?  R$'))
    if price > 1000:
        one_thousand+=1
    spent += price
    if a == 1:
        cheap = price
        names = name
    else:
        if price < cheap:
            cheap = price
            names = name
    print('-=' * 15)
    continue_ = input('Quer continuar? [S/N]').upper()
    if continue_ == 'N':
        break
    elif continue_ != 'S':
        continue_ = input('Quer continuar? [S/N]').upper()

print(f'O total a ser gasto na compra foi de R${spent:.2f}')
print(f'Existem {one_thousand} produtos custando mais de R$1000 ')
print(f'O nome do produto mais barato é {names}')