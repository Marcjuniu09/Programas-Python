#101
'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def a(ano):
    i=2022-ano
    if i<16:
        return f'Você tem somente {i} anos. Não vota'
    elif 16<=i<18 or i>65:
        return f'Você tem {i} anos. Voto opcional'
    else:
        return f'Você tem {i} anos. Voto obrigatório'

print(a(ano=int(input('Ano: '))))