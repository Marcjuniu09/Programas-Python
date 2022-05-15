#86
'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
l1=[]
l2=[]
l3=[]
for a in range(0,3):
    for c in range(0,3):
        a1=int(input(f'Digite [{a,c}]: '))
        l1.append(a1)
print()