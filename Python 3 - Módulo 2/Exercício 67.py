while True:
    num = int(input('Digite um número [Negativo para parar]: '))
    i = 1
    if num < 0:
        print('\nPrograma Tabuada encerrado!')
        break
    print('-=-' * 5)
    print(f'Tabuada do {num}:')
    while i != 11:
        print(f'{num} * {i:2} = {num * i}')
        i += 1
    print('-=-' * 5)
