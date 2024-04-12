p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(p, p + 10 * r, r):
    print(p, end=' -> ')
    p += r
print('FIM')
