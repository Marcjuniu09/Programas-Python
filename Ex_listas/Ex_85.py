#85
'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
'''
li=[]
lp=[]
ln=[]
for c in range (0,7):
    a=int(input('Digite um número: '))
    if a%2==0:
        lp.append(a)
    else:
        li.append(a)
ln.append(li)
ln.append(lp)
print(ln)


