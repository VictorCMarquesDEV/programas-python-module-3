exp = str(input('Digite a expressão: '))
pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')' and len(pilha) > 0:
        pilha.pop()
    else:
        pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
