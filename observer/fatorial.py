from fatob import FatOb
from fatlog import fatLog
class fatorial:
    def __init__(self):
        self.observers = []
        self.n = 0
        self.calculo = 1
    
    
    def calcula(self,n):
       self.n = n
       self._update_observers()
       for x in range(1,self.n+1):
            self.calculo*=x
       
    @property
    def saida(self):
        return self.calculo
    def _update_observers(self):
        for x in self.observers:
            x()
    
    def attach(self,observer):
        self.observers.append(observer)


def timer(func):
    import time
    def wraper(*a,**b):
        t1 = time.time()
        func(*a,**b)
        t2 = time.time()
        print("Tempo de execução:",t2-t1)
    return wraper

@timer
def main():
    op = 1
    while(op!=0):
        n = input("Digite um numero para o fatorial\n")
        try:
            n = int(n)
        except:
            pass
        i = fatorial()
        o = FatOb(i)
        u = fatLog(i)
        i.attach(u)
        i.attach(o)
        try:
                
                i.calcula(n)
                if(i.n<0):
                    pass
                else:
                    print("Fatorial  resultante:",i.calculo)
        except:
            pass
        print("Deseja sair ou continuar, digite 0 para sair ou qualquer numero para continuar?")
        op = int(input(""))
        if(op==0):
            print("Programa encerrado")

main()
