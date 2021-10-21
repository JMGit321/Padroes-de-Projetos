import logging


class fatLog:
    def __init__(self,fatorial):
       self.fatorial = fatorial
    def __call__(self):
         
         if(type(self.fatorial.n) is str):
            logging.basicConfig(filename='registro_em_arquivo.log',level=logging.ERROR)
            f = open('registro_em_arquivo.log','a')
            f.write("Tipo: ERROR,O usuario digitou letras para o fatorial\n")
            f.close()
         else:
            if(self.fatorial.n < 0):
                logging.basicConfig(filename='registro_em_arquivo.log',level=logging.ERROR)
                f = open('registro_em_arquivo.log','a')
                f.write("Tipo: ERROR:,Usuario digitou  um numero menor que 0 para o fatorial\n")
                f.close()
               

