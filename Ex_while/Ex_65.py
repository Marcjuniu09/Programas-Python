#65

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
a=0
b=0
maior=0
menor=0
w=''
while True:
    q=int(input('Digite um número: '))
    w=str(input('Quer continuar? [S/N]: '))
    b=b+1
    if w not in 'Nn':
        a=a+q
        if b==1:
            maior=q
            menor=q
        else:
            if q>maior:
                maior=q
            if q<menor:
                menor=q
    else:
        break
m=a/b
print('Você digitou {} numeros, destes o maior foi {} e o menor foi {}. A média entre eles é de {}'.format(b, maior, menor, m))

