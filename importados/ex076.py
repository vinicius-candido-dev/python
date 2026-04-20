produtos_preco = ('lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('_'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('_'*40)

for  a in range(0,len(produtos_preco)-1,2):
    print(f'{produtos_preco[a]:.<28}R$   {produtos_preco[a+1]:.2f} ')
print('_'*40)