valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto é o salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
parcela = valor / (anos * 12)
if parcela > (salario * 0.30):
    print('\nSalário Insuficiente. A prestação seria de R${:.2f}\nEmpréstimo NEGADO!'.format(parcela))
else:
    print('\nEmpréstimo pode ser APROVADO!')
    print('Valor Total: R${:.2f}\nPrestação Mensal: R${:.2f}\nParcelas: {}'.format(valor, parcela, anos * 12))
