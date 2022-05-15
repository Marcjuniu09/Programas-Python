#40
'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

a=int(input('Digite sua primeira nota: '))
b=int(input('Digite sua segunda nota: '))
c=(a+b)/2
if c<5:
    print('Sua média foi {}, menor do que 5, ou seja, você foi reprovado. Estude mais na próxima!'.format(c))
elif c>=5 and c<7:
    print('Sua média foi {}. Você está de recuperação!'.format(c))
else:
    print('Parabéns! Sua média foi {}. Você está aprovado.'.format(c))
