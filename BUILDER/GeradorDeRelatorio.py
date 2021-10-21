from HTML import HTML_Relatorio
from PRINTER import Printer_Relatorio
class GeradorDeRelatorio(object):

    def __init__(self):
        self._cabeçalho = None
        self._corpo = None
    
    def com_cabeçalho(self,cabeçalho):
        self._cabeçalho = cabeçalho
        return self
    def com_corpo(self,corpo):
        self._corpo = corpo
        return self
    def constroi(self,tipo):
        if(self._cabeçalho is None):
            print("Cabeçalho vazio, digiteo")
        if(self._corpo is None):
            print("Corpo do texto vazio, digiteo")
        if(tipo=="HTML"):
            return HTML_Relatorio(
                cabeçalho = "<head> " +self._cabeçalho + " </head>",
corpo = "<body> "+self._corpo+" <body>")
        if(tipo=="Printer"):
            return Printer_Relatorio(cabeçalho = "ASC(10) " + self._cabeçalho,
                                     corpo = "ASC(13) " + self._corpo)
        
