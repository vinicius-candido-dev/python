import random
a = ( input ('fale um nome'))
b = (input ('fale outro nome'))
c = (input ('fale outro nome'))
d = (input ('fale outro nome'))
lista = [ a , b,c,d]
print (f'a sequencia é {random.sample(lista,4)}')