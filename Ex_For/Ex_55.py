
#55

'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maior=0
menor=0
for c in range(1, 6):
    a=float(input('Digite o número da {}º pessoa: '.format(c)))
    if c==1:
        maior=a #lembrando que aqui é importante colocar que tal variável recebe tal coisa e não que é igual. "=" recebe "==" igual
        menor=a
    else:
        if a>maior:
            maior=a
        if a<menor:
            menor=a
print('O maior peso foi {}kg e o menor foi {}kg'.format(maior, menor))