
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários aluno.
    :param n: uma ou mais notas dos alunos (aceito vários)
    :param sit: valoe opocional, indicando se deve ou não adicionar a situação
    :return: dicionário com varias informações sobre a situação da turma.
    """
    h =dict()
    h['total'] = len(n)
    h['maior'] = max(n)
    h['menor'] = min(n)
    h['media'] = sum(n) / len(n)
    if sit:
        if h['media'] >= 7:
            h['situação'] = 'bom'
        elif h['media'] > 5:
            h['situação'] = 'RAZOAVEL'
        else:
            h['situação'] = 'Ruim'
    return h


resp = notas(5.5, 9.5, 10, 6.5,sit=True)
print(resp)
