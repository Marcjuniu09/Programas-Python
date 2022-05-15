#50
'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

s=0
cont=0
for c in range(0,7):
    a=int(input('Digite um número: '))
    if c%2==0:
        cont=cont+1
        s=s+c
print('A soma dos {} números é igual a {} '.format(cont, s))