#52

'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
'''
frase=str(input('Digite a frase: ')).strip().upper()#strip tirou os espaços finais e iniciais, upper deixou tudo maiusculo
palavras=frase.split() #trasnformou a frase em palavras separadas
junto= ''.join(palavras) #juntou as palavras sem espaço nenhum. Note que tem áspas simples, o que eu colocar dentro será o que irá separar as palavras
inverso='' #inverso de junto
for letra in range(len(junto) -1, -1, -1): #pegou o junto e leu do final até o inicio de uma em uma letra (por isso o -1 no final)
    inverso+= junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso ==junto:
    print('Temos um palídromo')
else:
    print('A frase digitada não é um palíndromo')