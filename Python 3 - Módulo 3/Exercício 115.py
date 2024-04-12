from uteis import datas
from time import sleep

while True:
    datas.cabecalho()
    datas.op()
    print('-' * 54)
    esc = datas.leiaInt('\033[0;49;34mSua Opção: \033[m')
    if esc == 1:
        datas.visualizacao()
        print('')
    elif esc == 2:
        datas.cadastro()
        print('')
    elif esc == 3:
        print('')
        datas.finalizar()
        break
    else:
        print('\033[0;49;31mERRO! Digite uma opção válida!\033[m')
        print('')
    sleep(3)
