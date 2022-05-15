#112
'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.




def a(num):
    while True:
        try:
            i=int(input('Digite um número inteiro: '))
            return i
            break           
        except: 
            print('ERRO! Digite um número inteiro')
def b(num):
    while True:
        try:
            r=float(input('Digite um número real: '))
            return r
            break
        except:
            print('ERRO! Digite um número real')
        
a=a('')
b=b('')
print(f'Você digitou o número inteiro {a} e o numero real {b} ')'''


#115a
'''Vamos criar um menu em Python, usando modularização.'''
def menu():
    print('='*23)
    print('     Menu Principal     ')
    print('='*23)
    print('1- Ver pessoas cadastradas')
    print('2- Cadastrar nova pessoa')
    print('3- Sair do sistema')
    print('='*23)

l=[]
dados=[]
while True:
    menu() 
    try:
        a=int(input('Sua opção: '))
        if a==1:
            print('Pessoas cadastradas')


        elif a==2: 
            dados.append(str(input('Nome: ')))
            try:
                d2=int(input('Idade: '))
            except:
                print('Por favor digite uma idade válida')
            dados.append(d2)
            dados[:]
            l.append(dados[:])
            dados.clear

            
        elif a==3:
            print('='*20)
            print('Programa finalizado')
            print('='*20)
            break
        else:
            print('Por favor digite um número de 1 a 3')
    except:
        print('Por favor digite somente números de 1 a 3')