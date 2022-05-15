#79
'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. 
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
l=[]
while True:
    a=int(input('Digite um número: '))
    if a not in l:
        l.append(a)
    else:
        print(f'Ignorei o número {a} pois ele já foi adicionado.')
    p=str(input('Deseja continuar? '))
    if p in 'Nn':
        break
l.sort()
print(f'Você digitou os valores {l}')