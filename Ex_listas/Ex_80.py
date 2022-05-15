#80
'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.'''

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