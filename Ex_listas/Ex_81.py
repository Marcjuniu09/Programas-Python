#81
''' Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:  
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

l=[]
while True:
    l.append(int(input('Digite um valor: ')))
    p=str(input('Deseja continuar? '))
    if p in 'Nn':
        break
l.sort(reverse=True)
print(f'Você digitou {len(l)}')
print(f'Os números digitados foram: {l}')
if 5 in l:
    print('O número 5 está na lista')
else:
    print('O número 5 não aparece na lista')