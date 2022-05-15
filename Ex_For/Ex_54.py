#54
'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
s=0
d=0
for c in range (1, 8):
    a=int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    c=2022-a
    if c<18:
        s=s+1
    else:
        d=d+1
print('Ao todo tiveram {} pessoas menores de idade e {} pessoas maiores de idade'.format(s, d))

#Outra forma de resolver. Forma feia!
print('Tiveram {} pessoas menores de idade'.format(s))
t=7-s
if t<0:
    t*-1
    print('E {} pessoas maiores de idade'.format(t))
else:
    print('E {} pessoas maiores de idade'.format(t))