#98
"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:   
a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep
def tempo(a, b, c):  
    print(f'Contagem de {a} até {b} pulando de {c} em {c}',)
    cont=a
    while True:
        for c in range(a, b+1, c):
            print(c)
            sleep(0.2)
            cont=cont+c
        if cont>=b:
            break                       
tempo(1, 10, 1)
tempo(10, -2, -2)
print('Agora defina a contagem')
tempo(a=int(input('Defina A= ')), b=int(input('Defina B= ')), c=int(input('Defina C= '))) #programa finalizado com alguns bugs que não sei resolver (Tá funcionando), volta aqui outro dia quando estiver programando melhor
