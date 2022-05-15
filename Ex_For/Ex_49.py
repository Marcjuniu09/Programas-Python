#49
''' Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
a=int(input('Digite um número: '))
for c in range (0,11):
    print('{}x{}={}'.format(a, c, a*c))