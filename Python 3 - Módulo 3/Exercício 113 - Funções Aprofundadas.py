def leiaInt(msg):
    a = str(input(msg))
    while not a.isnumeric():
        print('\033[0;49;31mERRO! Digite um número inteiro válido.\033[m')
        a = str(input(msg))
    return int(a)


def leiaFloat(msg):
    a = str(input(msg)).strip()
    while a.isalpha() or a == '':
        print('\033[0;49;31mERRO! Digite um número inteiro válido.\033[m')
        a = str(input(msg)).strip()
    return float(a)


aux = 1
try:
    n = leiaInt('Digite um número Inteiro: ')
except KeyboardInterrupt:
    print('\033[0;49;31mO usuário preferiu não informar os dados.\033[m')
    n = f = aux = 0
if aux:
    try:
        f = leiaFloat('Digite um número Real: ')
    except KeyboardInterrupt:
        print('\033[0;49;31mO usuário preferiu não informar os dados.\033[m')
        f = 0

print(f'Você acabou de digitar o número inteiro {n} e número real {f}')
