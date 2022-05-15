#38
'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''
a=int(input('Digite o primeior número: '))
b=int(input('Digite o segundo número: '))
if a>b:
    print('O primeiro número é maior que o segundo')
elif a==b:
    print('Os dois númeoros são de mesmo valor')
else:
    print('O Segundo númeoro é maior')