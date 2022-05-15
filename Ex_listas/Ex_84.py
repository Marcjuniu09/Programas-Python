## Listas Parte 2

#84
'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
l=[]
l2=[]
cont=0
ml=0
mp=0
while True:
    n=str(input('Digite um nome: '))
    p=float(input('Digite o peso desta pessoa: '))
    cont+=1
    if cont==1:
        ml=p
        mp=p
    else:
        if p>mp:
            mp=p
        if p<ml:
            ml=p
    l.append(n)
    l.append(p)
    l2.append(l[:])
    l.remove(n)
    l.remove(p)
    stop=str(input('Deseja continuar? '))
    if stop in "Nn":
        break
print(f'O mais leve foi {ml}. Peso de: ', end='')
for c in l2:
    if c[1]==ml:
        print(f'{c[0]}')
print(f'O mais pesado foi {mp}, Peso de:  ', end='')
for c in l2:
    if c[1]==mp:
        print(f'{c[0]}')