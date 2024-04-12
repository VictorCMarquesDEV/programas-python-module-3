r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r3 < (r1 + r2) and r2 < (r1 + r3) and r1 < (r2 + r3):
    print('Podem formar um triângulo e é ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Isósceles!')
    else:
        print('Escaleno!')
else:
    print('Não pode formar triângulo!')
