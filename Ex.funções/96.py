#96
'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def terreno(a,b):
    t=a*b
    print(f'O tamanho do terreno é de {t}m²')

a=int(input('Largura do terreno: '))
b=int(input('Comprimento do terreno: '))
terreno(a,b)