#45
'''Crie um programa que faça o computador jogar Jokenpô com você'''

from time import sleep
from random import randint
c=randint(0, 2)
itens= ('Pedra', 'Papel', 'tesoura')
print('''Itens: 
[Pedra]
[Papel]
[Tesoura]''')
a=int(input('Escolha um item: '))
print('Jô')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if a==0 and c==1 or a==1 and c==2 or a==2 and c==0:
    if a==0 and c==1:
        print('Você jogou {} e o pc jogou {}. Você perdeu!'.format(itens[a], itens[c]))
    elif a==1 and c==2:
        print('Você jogou {} e o pc jogou {}. Você perdeu!'.format(itens[a], itens[c]))
    elif a==2 and c==0:
        print('Você jogou {} e o pc jogou {}. Você perdeu!'.format(itens[a], itens[c]))
elif a==0 and c==2 or a==1 and c==0 or a==2 and c==1:
    if a==0 and c==2:
        print('Você jogou {} e o computador jogou {}. Você ganhou!'.format(itens[a], itens[c]))
    elif a==1 and c==0:
        print('Você jogou {} e o computador jogou {}. Você ganhou!'.format(itens[a], itens[c]))
    elif a==2 and c==1:
        print('Você jogou {} e o computador jogou {}. Você ganhou!'.format(itens[a], itens[c]))
elif a==c:
    print('Empate!')
    print('Ambos jogaram {}'.format(itens[a]))
else:
    print('...')
    sleep(2)
    print('O que é isso?')
    sleep(1)
    print('Você é burro?')
    sleep (1)
    print('Só tem 3 opções, bocó!')
    sleep(1)
    print('Jogada inválida!')