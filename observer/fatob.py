
class FatOb:
    def __init__(self,fatorial):
        self.fatorial = fatorial

    def __call__(self):
            if(type(self.fatorial.n) is str):
                print("Nao digite letras, somente numeros")
            else:
                if(self.fatorial.n<0):
                    print("Digite somente numeros maiores que 0")



