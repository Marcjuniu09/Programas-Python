#58

'''
O computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
from time import sleep
c= randint(0, 10)
a=0
cont=0
print('Olá')
sleep(1)
print('Irei pensar em um número aleatório de 0 a 10. Consegue adivinha?')
sleep(1)
while True:
    a=int(input('Qual o seu palpite? '))
    cont=cont+1
    if a!=c:
        print('Hmmmmm...')
        sleep(1)
        print('Errouuuu')
    else:
        break
print('Parabéns você acertou! Eu pensei no número {}. Você precisou de {} tentativas para acertar'.format(c, cont))
