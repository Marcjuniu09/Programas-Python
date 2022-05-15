#69

'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

cp=0
cf=0
ch=0
p=''
s=''
while p in 'Ss':  
    i=int(input('Digite a idade: '))
    s=str(input('Digite o sexo: '))
    if s in 'FfMm':
        if i>18:
            cp=cp+1
        if s in 'Ff' and i<20:
            cf=cf+1
        if s in 'Mm':
            ch=ch+1
        p=str(input('Deseja continuar[S/N]? '))
    else:
        print('Dados inválidos! Insisra novamente')
        print('-=='*20)
print('Ao todo foram {} pessoas maiores de 18, {} mulheres com menos de 20 anos e {} homens cadastrados'.format(cp, cf, ch))

#Não lembro o número
l=[]
for c in range(0,5):
    a=int(input('Digite um número: '))
    if c==0 or a>l[-1]:
        l.append(a)
        print('Adicionado na última posição')
    else:
        pos=0
        while pos <len(l):
            if a<=l[pos]:
                l.insert(pos,a)
                print(f'Adicionado na {pos+1}º posição da lista')
                break
            pos+=1
print(f'Vocês adicionou estes números: {l}')