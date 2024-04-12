br = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fluminense', 'Grêmio', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Cuiabá',
      'São Paulo', 'Atlético-MG', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos', 'Vasco',
      'Coritiba', 'América-MG')
print('-=-' * 30)
print(f'Lista de times do Brasileirão:\n{br}')
print('-=-' * 30)
print(f'Os 5 primeiros colocados são {br[:5]}')
print('-=-' * 30)
print(f'Os últimos 4 colocados são {br[-4:]}')
print('-=-' * 30)
print(f'Times em ordem alfabética:\n{sorted(br)}')
print('-=-' * 30)
if 'Chapecoense' in br:
    print(f'A Chapecoense está na {br.index("Chapecoense") + 1}º posição')
else:
    print('A Chapecoense não está na Série A')
print('-=-' * 30)
