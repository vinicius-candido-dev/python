times = ("São Paulo", "Bahia", "Red Bull Bragantino", "Chapecoense", "Mirassol",
         "Palmeiras", "Fluminense", "Coritiba", "Flamengo", "Botafogo",
         "Athletico-PR", "Grêmio", "Vitória", "Atlético-MG", "Remo", "Internacional",
         "Santos", "Vasco da Gama","Cruzeiro", "Corinthians")

for t in range(0,len(times[:5])):
    print(f'{t+1, times[t]}')

#mostar os ultimos 4 numeros
for h in range(16,20):
    print(f'{times[h]}')


#times em ordem alfabetica
for f in sorted(times[:]):
    print(f'{f}')
print(f'-='*30)
#posição da chapecoense
print(f'{times.index("chapecoense")}')
print(f'-='*30)