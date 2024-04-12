num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
print('{}{} É primo!'.format(num, ' NÃO' if cont != 2 else ''))
