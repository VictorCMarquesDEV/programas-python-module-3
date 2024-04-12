matriz = []
linha = []
for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input(f'Digite o número [{i + 1}]x[{j + 1}]: ')))
    matriz.append(linha[:])
    linha.clear()

print('-=-' * 10)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print('')
