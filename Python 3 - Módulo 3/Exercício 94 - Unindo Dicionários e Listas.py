dados = dict()
pessoas = list()
cont = soma = 0

while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()
    dados['Idade'] = int(input('Idade: '))
    cont += 1
    soma += dados['Idade']
    pessoas.append(dados.copy())
    dados.clear()
    esc = str(input('Deseja continuar [S/N]? '))
    if esc in 'Nn':
        break
media = soma / cont
print('-=-' * 30)
print(f'> Quantidade de pessoas cadastradas: {cont}')
print(f'> Média de idade do grupo: {media} anos')
print('> Mulheres: ', end='')
for c in range(0, cont):
    if pessoas[c]['Sexo'] == 'F':
        print(pessoas[c]['Nome'], end=' ')
print('\n> Pessoas com idade acima da média:')
for c in range(0, cont):
    if pessoas[c]['Idade'] > media:
        print(f'Nome = {pessoas[c]["Nome"]}, Sexo = {pessoas[c]["Sexo"]}, Idade = {pessoas[c]["Idade"]}')
