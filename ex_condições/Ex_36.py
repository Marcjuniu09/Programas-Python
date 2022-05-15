#36
'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

a=int(input('Qual o valor da casa? '))
b=int(input('Em quantos anos você quer pagar? '))
c=int(input('E qual o seu salário mensal? '))
d=a/(b*12)
e=(30*c)/100
if d>e:
    print('Você não pode financiar esta casa pois as parcelas de R${} são altas demais'.format(d))
else:
    print('Financiamento aprovado! As parcelas serão no valor de R${}'.format(d))
