n = num = int(input('Digite um número: '))
fat = 1
print('{}! = '.format(n), end='')
while num != 0:
    fat *= num
    print('{}'.format(num), end='')
    num -= 1
    if num != 0:
        print(' x ', end='')
    if num == 0:
        print(' = ', end='')
print('{}'.format(fat))
