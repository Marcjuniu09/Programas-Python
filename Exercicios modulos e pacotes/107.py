'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
Aula Anterior
'''

import mdl
a=int(input('Digite: '))
print(f'O dobro de {a} é {mdl.dobro(a)}')
print(f'A metade de {a} é {mdl.metade(a)}')
print(f'{a} com um aumento de 10% fica igual a: {mdl.aumento(a)}')