#67
''' 
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    a=int(input('\33[31mDigite o número que você quer ver a tabuada:\n\33[m'))
    if a>0:
        for c in range (0, 11):
            b=c*a
            print('{}x{}={}'.format(c, a, b))
    else:
        break
print('Programa finalizado!')