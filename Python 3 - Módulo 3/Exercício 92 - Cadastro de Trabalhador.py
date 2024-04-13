from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = datetime.today().year - int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('CTPS [0 significa não ter]: '))
if dados['CTPS']:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))


print('-=-' * 10)
for k, v in dados.items():
    print(f'{k}: {v}')
if dados['CTPS']:
    aposentar = dados['Idade'] + 35 - (datetime.today().year - dados['Ano de Contratação'])
    print('Vai se aposentar com {} anos de idade!'.format(aposentar))
