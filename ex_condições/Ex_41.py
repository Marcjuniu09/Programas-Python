#41
'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

a=int(input('Digite sua idade: '))
if a<9:
    print('Você tem {} anos e vai para a categoria Mirim'.format(a))
elif a>=9 and a<14:
    print('Você tem {} anos e vai para a categoria infantil'.format(a))
elif a>=14 and a<19:
    print('Você tem {} anos e vai para a categoria Junior'.format(a))
elif a>=19 and a<25:
    print('Você tem {} anos e vai para categoria Sênior'.format(a))
else:
    print('Você tem {} e vai para a categoria Master'.format(a))