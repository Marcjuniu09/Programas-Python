#83
'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
a=[]
f=[]
e=input('Digite uma expressão: ')
for simb in e: #para cada caractere escrito em 'e'
    if simb=='(':
        a.append(simb)
    elif simb==')':
        f.append(simb)
print(a)
print(f)
if len(a) == len(f):
    print('Sua expressão está correta ')
else:
    print('Sua expressão está errada')