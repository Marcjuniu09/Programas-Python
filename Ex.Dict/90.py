#90
'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
aluno={}
aluno['Nome']=str(input('Digite um nome: '))
aluno['Media']=float(input(f'A média de {aluno["Nome"]}: '))
if aluno['Media'] >7:
    aluno['Situação']= 'aprovado'
elif 7 <= aluno['Media'] >=5:
    aluno['Situação']= 'recuperação'
else:
    aluno['Situação']= 'Reprovado'
for k, v in aluno.items():
    print(f'{k}= {v}')