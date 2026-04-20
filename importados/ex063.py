a =0
t1=0
t2=1
num= int(input('Quantos termos da sequencia de fibonacci vc quer ?'))
while a != num:
    t3 = t1+t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    a += 1

