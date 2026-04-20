lista = []
lorena = []
while True:
    name = input('Qual o seu nome:  ')
    grade = float(input('Qual a 1 nota?  '))
    mark = float(input('Qual a 2 nota?  '))
    media = (grade + mark)/2
    lorena.append([name, [grade, mark], media])
    lista.append(lorena[:])
    cont = input('Quer continuar? [S/N]')
    if cont in 'Nn':
        break
print('-='*40)
print(f'{"No.":<4}{"NOME":<10}{"MÊDIA":>8}')
print('-'*35)
for i,a in enumerate(lorena):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

while True:
    print('-'* 35)
    h = int(input('Mostrar de qual aluno? (999 para terminar):  '))
    if h == 999:
        break
    if h <= len(lista)-1:
        print(f'Notas de {lorena[h][0]} são {lorena[h][1]} ')
print('<<< VOLTE SEMPRE >>>')