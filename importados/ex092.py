from datetime import date
dic = dict()
dic['nome'] = input('nome:  ')
nas = int(input('Ano de nascimento:  '))
dat = date.today().year
dat = int(dat)
idade = dat - nas
dic['idade']=  idade
dic['clps'] = int(input('Carteira de Trabalho (0 não tem):  '))
if dic['clps'] != 0:
    dic['contratação'] = int(input('Ano de contratação:  '))
    dic['salário'] = int(input('Salário: R$ '))
    ano_trab =  dat - dic['contratação']
    dic['aposentar'] = idade + 35 - ano_trab
print(dic)
print('-='*30)
for k,v in dic.items():
    print(f'{k} tem o valor {v}')
