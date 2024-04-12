num = int(input('Digite um número: '))
ver = 0
a = 0
b = 1
while num != 0:
    if ver == 1:
        print(' -> ', end='')
    ver = 1
    num -= 1
    print(a, end='')
    soma = a + b
    a = b
    b = soma
if ver != 0:
    print(' -> FIM')
