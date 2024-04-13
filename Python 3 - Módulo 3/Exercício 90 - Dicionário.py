dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'

print('-=-' * 10)
for k, v in dados.items():
    print(f'{k}: {v}')
