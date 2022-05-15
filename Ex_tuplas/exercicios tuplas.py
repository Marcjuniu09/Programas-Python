#72
'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''


e=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:   
    a=int(input('Escolha um número: '))
    if a >10:
        print('ERRO! Digite um número novamente')
    else:
        print(f'{e[a]}')
        break

#73
'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''


letras=('a', 'g', 'm', 'c', 'q', 'x', 'l', 'z', 'b')
print(f'As 5 primeiras letras são {letras[0:5]}')
print(f'As ultimas 4 letras são {letras[6:11]}')
print(f'As letras em ordem alfabética: {sorted(letras)}')
print(f'A letra g está na {letras.index("q")+1}º posição')

#74
''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
c=(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram {c}')
a=sorted(c)
print(f'O maior número foi: {a[4]}')
print(f'O menor número foi: {a[0]}')


#75
'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

cont=0
n=(int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(n)
for c in n:
    if c==9:
        cont=cont+1
print(f'o 9 Apareceu {cont} vezes')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}º posição')
else:
    print('O número 3 não aparece nenhuma vez')
print(f'Os números pares foram: ')
for p in n:
    if p%2==0:
        print(p,end=' ')

#77

'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
p=(str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')))
for palavra in p:
    print(f'\nNa palavra {palavra} temos:',end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra,end=' ')