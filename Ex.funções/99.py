#99
'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from random import randint
from time import sleep
l=[]
def x():
        for c in range(0, randint(1,10)):
            a=randint(1,20)
            l.append(a)
        sleep(0.5)
        print(f'{l} foram os valores informados')
        qtd=len(l)
        l.sort()
        ult=l[-1]
        sleep(0.5)
        print(f'O maior número foi: {ult}')
        sleep(1)
        print('=-'*20)
def slep():
    print('Analisando dados',end='', flush=True)
    sleep(0.5)
    print('.',end='', flush=True)
    sleep(0.5)
    print('.',end='', flush=True)
    sleep(0.5)
    print('.',end='', flush=True)
    print()
for k in range(1,randint(0,10)):
    slep()
    x()
