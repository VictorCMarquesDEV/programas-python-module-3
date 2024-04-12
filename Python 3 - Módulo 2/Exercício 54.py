from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    if (date.today().year - ano) >= 18:
        maior += 1
    else:
        menor += 1
print('\nPessoas maiores de idade: {}\nPessoas menores de idade: {}'.format(maior, menor))
