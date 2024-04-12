def leiaInt(msg):
    a = str(input(msg))
    while not a.isnumeric():
        print('\033[0;49;31mERRO! Digite um número inteiro válido.\033[m')
        a = input(msg)
    return a


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
