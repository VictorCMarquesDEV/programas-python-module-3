continuar = 'S'
cont = soma = maior = menor = media = 0

while continuar == 'S':
    num = int(input('Digite um número: '))
    if cont == 0:
        menor = maior = num
    soma += num
    cont += 1
    media = soma / cont
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = str(input('Deseja continuar [N/S]? ')).upper()

print('\nQuantidade de números: {}'.format(cont))
print('Média entre todos = {:.2f}'.format(media))
print('Maior valor: {}\nMenor valor: {}'.format(maior, menor))
