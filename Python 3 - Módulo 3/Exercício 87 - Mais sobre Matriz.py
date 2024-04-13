matriz = []
linha = []
contpar = contc3 = maiorl2 = 0
for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input(f'Digite o número [{i + 1}]x[{j + 1}]: ')))
    matriz.append(linha[:])
    linha.clear()

print('-=-' * 7)
print('{:^21}'.format('Matriz:'))
for i in range(0, 3):
    for j in range(0, 3):
        if i == 1 and j == 0:
            maiorl2 = matriz[i][j]
        if matriz[i][j] % 2 == 0:
            contpar += matriz[i][j]
        if j == 2:
            contc3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maiorl2:
                maiorl2 = matriz[i][j]

        print(f'[{matriz[i][j]:^5}]', end='')
    print('')
print('-=-' * 7)
print(f'Soma de todos os pares: {contpar}')
print(f'Soma de todos os valores da 3º coluna: {contc3}')
print(f'Maior valor da 2° linha: {maiorl2}')
