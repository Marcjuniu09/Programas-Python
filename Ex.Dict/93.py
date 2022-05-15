#93
'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

partida={}
g=[]
partida["Nome"]=str(input('Nome: '))
quantidade=int(input(f'Quantas partidas {partida["Nome"]} jogou? '))
tot=0
for c in range(1, quantidade+1):
    g1=int(input(f'Quantos gols {partida["Nome"]} fez na {c}º partida? '))
    g.append(g1)
    tot=tot+g1
partida['Gols']=g[:] #adicionando uma chave nova e colocando uma lista nela
print('-='*20)
print(partida)
print('-='*20)
for k, v in partida.items():
    print(f'{k}: {v}')
print(f'Ao todo {partida["Nome"]} fez {tot} gols ')
print('-='*20)
for i, v in enumerate(partida['Gols']):
    print(f'Na partida {i+1}º partida ele fez {v} gols ')
