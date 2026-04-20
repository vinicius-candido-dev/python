def voto(nasc):
    """
-> year to vote
    :param nasc: type the year your date of the birth
    :return: if is opcional, obrigatorio and não volta
    """
    from datetime import date
    ano_atual = date.today().year
    year = ano_atual - nasc
    if year < 16:
       return f'Com {year} anos: NÂO VOLTA.'
    elif year < 18 or year > 65:
       return f'Com {year} anos: VOTO OPCIONAL.'
    else:
        return f'Com {year} anos: VOTO OBRIGATORIO.'


print('-' * 30)
nascimento = int(input('Em que ano você nasceu?  '))
print(voto(nascimento))
print()
help(voto)