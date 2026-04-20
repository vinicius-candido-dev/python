import random

import lista
a = ( input ('fale um nome'))
b = (input ('fale outro nome'))
c = (input ('fale outro nome'))
d = (input ('fale outro nome'))
lista = [ a , b,c,d]
no = random.choice(lista)
print (no)