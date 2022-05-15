#78
'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

menor=0
maior=0
l=[]
for c in range(0,5):
    n=int(input('Digite um número:'))
    l.insert(c,n)
    if c==0:
        maior=n
        menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
for i, v in enumerate(l):        #aqui é para saber a posição dos maiores e menores números.
    if v==maior:             
        print(f'{i},',end='')
    if v==menor:
        print(f'{i},',end='')    # Fiquei com preguiça de deixar bonito com as frases mas funcionou e é isso 
        