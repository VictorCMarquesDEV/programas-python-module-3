valor = float(input('Digite o valor: R$'))
pag = int(input('1 - À vista em débito\n2 - À vista no crédito\n3 - Em até 2x no crédito\n4 - 3x ou mais no crédito\n'))
if pag == 1:
    print('Valor: R${:.2f}\nDesconto: 10%\nValor Total: R${:.2f}'.format(valor, valor * 0.90))
elif pag == 2:
    print('Valor: R${:.2f}\nDesconto: 5%\nValor Total: R${:.2f}'.format(valor, valor * 0.95))
elif pag == 3:
    print('Valor: R${:.2f}\nValor Total: R${:.2f}'.format(valor, valor * 1))
    print('Parcelas: 2x de R${:.2f}'.format(valor * 1 / 2))
elif pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Valor: R${:.2f}\nJuros: 20%\nValor Total: R${:.2f}'.format(valor, valor * 1.20))
    print('Parcelas: {}x de R${:.2f}'.format(parcelas, valor * 1.2 / parcelas))

else:
    print('Forma de pagamento inválida!')
