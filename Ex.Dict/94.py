#94
'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''

l=[]
dados={}
cont=tot=0
while True:
    dados.clear
    dados['nome']=str(input('Nome: '))
    while True:
        dados['sexo']=str(input('Sexo: '))     
        if dados ['sexo'] in 'MmFf':
            break
        print('Digite somente M ou F')
    dados['Idade']=int(input('Idade: '))
    cont=cont+1
    tot=tot+dados['Idade']
    l.append(dados.copy())
    while True:
        p=str(input('Deseja continuar? '))
        if p in 'Ss':
            break
        print('Digite somente S ou N')
    if p=='Nn':
        break
m=tot/cont
print(f'Ao todo foram cadastradas {cont} pesoas')
print(f'A média de idade é de {int(m)} anos')
for c in l:
    if c['sexo'] in 'Ff':
        print(f'As mulheres cadastradas foram: {c["nome"]}', end='')
for c in l:
    if c['sexo'] in 'Ff' and c['Idade']>=m:
        print(f'As mulheres com idade acima da média são: {c["nome"]}', end='')