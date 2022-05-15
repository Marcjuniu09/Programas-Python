#57
'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
c= ''
while True:
    c=input('Você é do sexo masculino ou feminino? ')
    if c not in 'MmFf':
        print('Informação inválida, diga seu sexo novamente: ')
    else:
        break
print('Cadastro concluído com sussesso')