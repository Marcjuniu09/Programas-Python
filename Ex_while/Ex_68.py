#68

'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
from time import sleep
a=''
cont=0
while True:
    c= 1 #randint(0, 10)
    a=str(input('[I/P]: '))
    b=int(input('Jogue um número: '))
    d=(b+c)%2
    e=b+c
    if d==0 and a in 'Pp':
        print('Você jogou {} e o computador jogou {}. Deu {}. Você ganhou!'.format(b, c, e))
    elif d==1 and a in 'Ii':
       print('Você jogou {} e o computador jogou {}. Deu {}, impar. Você ganhou!'.format(b, c, e))
    if d==0 and a in 'Pp' or d==1 and a in 'Ii':
        cont=cont+1
    else:
        break
print('Você ganhou {} vezes'.format(cont))
print('GAME OVER')
