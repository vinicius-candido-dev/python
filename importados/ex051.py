one_term = int(input('type the first term: '))
reason = int(input('type the reason: '))
tenth = one_term + (10 - 1) * reason
for c in range(one_term,tenth + reason, reason):
    print(c, end='->')
print('Acabou!')

