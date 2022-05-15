#56
'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

m=0
maior=0
cont=0
MV= ''
for c in range(1,5):
    print('---Dados da {}º pessoa---'.format(c))
    n=str(input('Digite o nome da {}º pessoa: '.format(c)))
    i=int(input('Digite a idade da {}º pessoa: '.format(c)))
    s=str(input('Sexo [M/F]: '))
    m=m+i
    if s in 'Mm': #quando se é para usar o 'if' com uma str se usa in 'a letra ou str que vai colocar entra estas áspas dupas'
        if c==1:
            maior=i
        else:
            if i>maior:
                maior=i
                MV=n
    if s in 'Ff':
        if i<=20:
            cont=cont+1
print('A média de idade das pessoas é de {} anos'.format(m/4))
print('O homem mais velho se chama {} e tem {} anos'.format(MV, maior))
print('Ao todo tem-se {} mulheres com menos de 20 anos'.format(cont))