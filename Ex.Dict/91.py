#91 Não terminei
'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
final={}
jogadores={}
for c in range(1, 5):
    jogadores[f'jogador {c}']=randint(1,6)
for i in sorted(jogadores, key=jogadores.get):
    print(jogadores)
    print()