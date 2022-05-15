#108
'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''


from mdl import dobro, metade, aumento, format

a=int(input('Digite um valor: R$'))
print(f'O dobro de  {format(a)} é {format(dobro(a))}')
print(f'A metade de {format(a)} é {format(metade(a))}')
print(f'{format(a)} com um aumento de 10% fica igual a: {format(aumento(a))}')