galera = list()
galera.append('Mari')
galera.append(13)
gente = list()
gente.append(galera[:])
galera[0] = 'PIcachu'
galera[1] = 25
gente.append(galera[:])
for p in gente:
    print(f'{p[0]}  {p[1]}')