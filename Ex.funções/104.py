#104
'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt(Digite um n: )'''

def leiaint(num):
    while True:
        n=str(input('Digite um número:'))
        if n.isnumeric():
            n=int(n)
            break
        else:
            print('ERRO! Digite um número válido')
    return n

n=leiaint('Digite um número')
print(f'Você digitou o número {n}')