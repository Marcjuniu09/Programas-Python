#48
''' Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s=0
cont=0
for c in range(1,501):
    if c%3==0 and c%2==1:
        cont=cont+1
        s=s+c
print('A soma de todos os {} números será: {}'.format(cont,s))