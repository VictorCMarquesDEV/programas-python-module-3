num = int(input('Digite um número inteiro: '))
esc = int(input('\nQual vai ser a conversão?\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nEscolha: '))
if esc == 1:
    print('Dec: {} /// Bin: {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('Dec: {} /// Oct: {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('Dec: {} /// Hexa: {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida!')
