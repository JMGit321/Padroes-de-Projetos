

def p_decorador(func):
    def nova_func(*a,**b):
        print("brincando no decorator")
        print("p1",*a)
       
        
        return func(*a,**b)
    return nova_func

def p_decorador2(func):
    def nova_func(*a,**b):
        print("dentro do dentro ")
        return func(*a)
    return nova_func
    

@p_decorador
@p_decorador2
def devolve_trecho(num1,num2,num3):
    print("aqui %g" % (num1*num2*num3))

devolve_trecho(1,2,5)
