valores = []
pos = -1
for i in range(0, 5):
    a = int(input('\nDigite um número: '))
    if i == 0:
        valores.append(a)
        print(f'Valor adicionado no final da lista')
    else:
        pos = len(valores)
        for j in range(pos, 0, -1):
            if a < valores[j - 1]:
                pos += -1
            if a > valores[j - 1]:
                break
        valores.insert(pos, a)
        if pos != len(valores) - 1:
            print(f'Valor adicionado na posição {pos} da lista')
        else:
            print(f'Valor adicionado no final da lista')

print(f'\nLista: {valores}')
