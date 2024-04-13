# append -> adicionar elemento no final da lista
# insert -> adicionar elemento com posição na lista
# del -> eliminar elemento
# pop -> eliminar elemento, pode eliminar o último elemento
# remove -> eliminar elemento

valores = list(range(4, 11))
print(valores)

listanum = [8, 2, 5, 4, 9, 3, 0, 7]
listanum.sort()
print(listanum)
listanum.sort(reverse=True)
print(listanum)

val = []
print(val)
val.append(5)
val.append(9)
val.append(4)
for c, v in enumerate(val):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
# b = a -> Cria uma ligação
b = a[:]  # Copia os valores
print(f'Lista A: {a}')
print(f'Lista B: {b}')
