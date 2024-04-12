# () -> Tupla -> São imutáveis
# [] -> Lista -> São mutáveis
# {} -> Dicionário

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for c in lanche:
    print(c)
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
