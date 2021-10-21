from aplicacao import Aplicaçao
from HTML import HTML_Relatorio
from PRINTER import Printer_Relatorio

class relatorio(object):
    def __init__(self):
        sair = False
        while(not sair):
            aplicacao = Aplicaçao()
            relatorio = aplicacao.geraRelatorio
            if(type(relatorio) is HTML_Relatorio):
                print("Cabeçalho do relatorio HTML:")
                print("")
                print(relatorio.cabeçalho)
                print("")
                print("Corpo do relatorio HTML:")
                print("")
                print(relatorio.corpo)
                print("")

            if(type(relatorio) is Printer_Relatorio):
                print("Cabeçalho do relatorio Printer:")
                print("")
                print(relatorio.cabeçalho)
                print("")
                print("Corpo do relatorio Printer:")
                print("")
                print(relatorio.corpo)
                print("")
            op = str(input("Deseja sair ou continuar?\n"))
            if(op=="sair"):
                print("Programa encerrado")
                sair = True
                

r = relatorio()

