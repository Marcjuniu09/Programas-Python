#95
'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

partida={}
g=[]
while True:
    partida["Nome"]=str(input('Nome: '))
    quantidade=int(input(f'Quantas partidas {partida["Nome"]} jogou? '))
    tot=0
    for c in range(1, quantidade+1):
        g1=int(input(f'Quantos gols {partida["Nome"]} fez na {c}º partida? '))
        g.append(g1)
        tot=tot+g1
    while True:
        p=str(input('Deseja continuar?'))
        if p not in 'SsNn':
            print('Por favor digite somente S ou N')
        else:
            break
    if p in 'Nn':
        break
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