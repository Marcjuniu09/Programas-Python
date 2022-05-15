#59
'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''


from time import sleep
a=0
b=0
c=0

while True:
    a=int(input('Digite o primeiro número: '))
    b=int(input('Digite o segundo número: '))
    print('O que você quer fazer com estes números? ')
    sleep(1)
    print("""
    -=-=-=-=-=-=--=-Suas opções-=-=-=-=-=-=--=-
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa     """ )  

    c=int(input('Qual sua escolha? '))
    if c==1:
        q=a+b
        print('A soma entre estes dois números é {} '.format(q))
    elif c==2:
        w=a*b
        print('A multiplicação entre estes dois números é {}'.format(w))
    elif c==3:
        if a>b:
            print('{} é o maior número e {} é o menor'.format(a, b))
        else:
            print('{} é o maior número e {} é o menor'.format(b, a))
    elif c==4:
        print( 'Insira os números novamente')
    elif c==5:
        break
    else: 
        print('Opção inválida. Tente novamente')
        print('-='*10)
