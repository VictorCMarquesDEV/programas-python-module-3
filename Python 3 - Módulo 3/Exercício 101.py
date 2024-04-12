from datetime import datetime


def voto(a):
    idade = datetime.today().year - a
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
