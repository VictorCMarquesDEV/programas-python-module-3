from time import sleep


def maior(*num):
    sleep(1)
    linha()
    if len(num) == 0:
        m = 0
    else:
        m = num[0]
    for i in num:
        if i > m:
            m = i
    print(f'Analisando os valores passados: {list(num)}')
    print(f'Dos {len(num)} valores ao todo, o {m} é o maior.')


def linha():
    print('=' * 50)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
