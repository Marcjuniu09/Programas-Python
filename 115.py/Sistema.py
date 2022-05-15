from menu import menu
from time import sleep


nome=[]
idade=[]
while True:
    menu() 
    try:
        a=int(input('Sua opção: '))
        if a==1:
            with open('nome.txt','r') as arquivo:
                for valor in nome:
                    print(nome)
            with open('idade.txt','r') as arquivo:
                for valor in idade:
                    print(idade)

        elif a==2: 

            d1=str(input(' Nome:'))
            nome.append(d1)
            with open('nome.txt','a') as arquivo:
                for valor in nome:
                    arquivo.write(str(valor))
            try:
                d2=int(input('Idade: '))
                idade.append(d2)
                with open('idade.txt','a') as arquivo:
                    for valor in idade:
                        arquivo.write(str(valor))
            except:
                print('Por favor digite uma idade válida')

            
        elif a==3:
            print('='*20)
            print('Programa finalizado')
            print('='*20)
            break
        else:
            print('Por favor digite um número de 1 a 3')
    except:
        print('Por favor digite somente números de 1 a 3')  
    sleep(1)