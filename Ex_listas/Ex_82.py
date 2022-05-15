#82
'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

l=[]
p=[]
i=[]
while True:
    n=int(input('Digite um número: '))
    l.append(n)
    if n%2==0:
        p.append(n)
    else:
        i.append(n)
    a=str(input('Deseja continuar? '))
    if a in 'Nn':
        break
print(f'A lista completa: {l}')
print(f'A lista com números pares: {p}')
print(f'A lista com números impares: {i}')