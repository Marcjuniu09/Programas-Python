#51

'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
s=0
a=int(input('Digite um número: '))
for c in range(1, a+1):
    if a%c==0:
        print('\33[32m', end='')
        s=s+1
    else:
        print('\33[35m', end=' ')
    print('{}'.format(c),end=' ')
print('\n\33[m')
if s==2:
    print('O número {} foi dividido {} vezes. Logo, é um número primo.'.format(a, s))
else:
    print('O número {} foi divido {} vezes. Logo, NÃO é um número primo.'.format(a, s))

