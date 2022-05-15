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
