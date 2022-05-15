def dobro(num=0):
    f=num*2
    return f

def metade(num=0):
    f=num/2
    return f

def aumento(num=0):
    f=(num/10)*11
    return f 

def format(num=0, cif='R$'):
    return f'{cif}{num:>.2f}'.replace('.', ',')
    
def resum(num):
    print(f'O dobro de  {format(num)} é {format(dobro(num))}')
    print(f'A metade de {format(num)} é {format(metade(num))}')
    print(f'{format(num)} com um aumento de 10% fica igual a: {format(aumento(num))}')
    return