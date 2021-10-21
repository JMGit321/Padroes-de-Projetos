def decorador(func):
    def inner(*a,**b):
        print("Nome da funcao 1 ",func.__name__)
        print("Resultado com a funcao logo abaixo 1")
        return func(*a,**b)
    return inner


def decorador2(func):
    def inner(*a,**b):
        print("Nome da funcao 2 ",func.__name__)
        print("Resultado com a funcao logo abaixo 2")
        return func(*a,**b)
    return inner
@decorador
@decorador2
def soma(n1,n2):
    print("Soma 1", n1+n2)
    return "soma 2 " + str(n1+n2) 
