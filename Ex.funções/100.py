#100
'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint

def sorteia(l):
    for c in range(0,5):
        a=randint(1,10)
        l.append(a)
def somaPar(l):
    p=0
    for v in l:
        if v%2==0:
            p=p+v
    print(l)
    print(f'A soma dos valores pares é de {p}')
l=[]
sorteia(l)
somaPar(l)
