from GeradorDeRelatorio import GeradorDeRelatorio
class Aplicaçao(object):
    @property
    def geraRelatorio(self):
        cabeçalho = str(input("Digite o cabeçalho\n"))
        corpo = str(input("Digite o corpo\n"))
        print("Digite HTML para Relatorio HTML")
        print("Digite Printer para Relatorio printer")
        tipo = str(input("Digite o tipo do relatorio\n"))
        relatorio = (GeradorDeRelatorio().com_cabeçalho(cabeçalho).com_corpo(corpo).constroi(tipo))
        return relatorio
        
