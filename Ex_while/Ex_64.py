#64
'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

n=0
while True:
    a=int(input('Digite um número: '))
    if a !=999:
        n=n+a
    else:
        break
print ('A soma de todos os números digitados é {}'.format(n))