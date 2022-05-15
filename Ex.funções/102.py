#102
'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(n, show=True):
    f=1
    for c in range(n, 0, -1):
        f=f*c
        if show:
            if c>1:
                print(f' {c} x',end='')
            else:
                print(' 1 = ',end='')
    return f
print(fatorial(n=int(input('Digite o número: '))))