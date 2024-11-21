def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)

############################################################################################
print('\n')

'''
def notas(*buba, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    tudo = {}
    maior = menor = total = media = soma = 0
    total = len(buba)
    for c in range(0, len(buba)):
        if c == 0:
            maior = menor = buba[c]
        else:
            if buba[c] > maior:
                maior = buba[c]
            if buba[c] < menor:
                menor = buba[c]
        soma += buba[c]
        media = soma/total

    tudo['total'] = total
    tudo['maior'] = maior
    tudo['menor'] = menor
    tudo['media'] = media

    if sit:
        gobos = ''
        if media < 5:
            gobos = 'RUIM'
        elif media < 7:
            gobos = 'RAZOÁVEL'
        else:
            gobos = 'BOA'
        tudo['situação'] = gobos
    return tudo


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)

'''