#92
'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
dados={}
dados['Nome']=str(input('Nome: '))
nascimento=int(input('Ano de nascimento: '))
dados['idade']=2022-nascimento
dados['CTPS']=int(input('CTPS (0 caso não tenha)'))
if dados['CTPS']==0:
    print("=-"*30)
    print(f'O nome é: {dados["Nome"]}')
    print(f'Tem {dados["idade"]} anos')
    print(f'Número do CTPS: {dados["CTPS"]}')
else:
    dados['contratação']=int(input('Ano de contratação: '))
    dados['Salário']=int(input('Salário: '))
    dados['aposentadoria']=dados['contratação']-nascimento +30
    dados['aposentadoria']
    print("=-"*30)
    print(f'O nome é: {dados["Nome"]}')
    print(f'Tem {dados["idade"]} anos')
    print(f'Número do CTPS: {dados["CTPS"]}')
    print(f'Foi contratado em {dados["contratação"]}')
    print(f'Tem salário igual a R${dados["Salário"]}')
    print(f'Irá se aposentar com {dados["aposentadoria"]}')