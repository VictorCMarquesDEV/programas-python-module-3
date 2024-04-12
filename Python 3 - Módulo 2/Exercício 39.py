from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = int(date.today().year) - ano
if idade < 18:
    print('Você ainda vai se alistar.\nFalta(m) {} ano(s)'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar.')
else:
    print('Passou da hora de alistar em {} ano(s)'.format(idade - 18))
