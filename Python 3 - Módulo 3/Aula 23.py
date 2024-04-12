try:  # tente
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ZeroDivisionError:  # se não conseguir
    print(f'Não é possível dividir um número por zero!')
except (ValueError, TypeError):
    print(f'Tivemos problemas com os tipos de dados que você digitou.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:  # se conseguir
    print(f'O resultado é {r:.2f}')
finally:  # final
    print('Volte sempre!')
