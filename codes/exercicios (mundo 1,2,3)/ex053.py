phrase = input('Type the phrase:  ').strip().upper()
inverso = ''
palavras = phrase.split()
junto = ''.join(palavras)
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]

if inverso == junto:
    print('This is Palindrome')
else:
    print('This is not Palindrome')
print(inverso)


