def escreva(msg):
    num = len(msg)
    print('=' * (num + 4))
    print('  {:^}  '.format(msg))
    print('=' * (num + 4))


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
