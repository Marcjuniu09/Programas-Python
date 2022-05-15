#39
'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

a=int(input('Digite sua idade: '))
b=2022-a
c=18-a
d=a-18
e=2022+c
f=2022-d
if a<18:
    print('Você tem somente {} anos, ainda não pode se alistar, aguarde {} anos para poder se alistar'.format(a,c))
    print('O seu alistamento será em {}'.format(e))
elif a==18:
    print('Quem nasceu em {} tem exatamente 18 anos e já pode se alistar'.format(b))
else:
    print('Você nasceu em {} e hoje tem mais de 18 anos. Você deveria ter se alistado em {} a cerca de {} anos atrás'.format(b, f, d))
