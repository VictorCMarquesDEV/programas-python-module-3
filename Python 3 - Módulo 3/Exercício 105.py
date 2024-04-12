def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos.
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    soma = 0
    for i in num:
        soma += i
    media = soma / len(num)
    info = {'Quantidade de notas': len(num), 'Maior Nota': max(num), 'Menor Nota': min(num),
            'Média da turma': soma / len(num)}
    if sit:
        info['Situação'] = 'RUIM' if media < 7 else 'BOA'
    return info


resp = notas(3.5, 2, 6.5, 2, 7, 4)
print(resp)
help(notas)
