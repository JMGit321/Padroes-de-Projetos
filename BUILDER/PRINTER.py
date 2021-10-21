class Printer_Relatorio(object):
    def __init__(self,cabeçalho,corpo):
        self._cabeçalho = cabeçalho
        self._corpo = corpo

    def setcabeçalho(self,texto):
        self._cabeçalho = texto
    def setcorpo(self,texto):
        self._corpo = texto
    def getcabeçalho(self):
        return self._cabeçalho
    def getcorpo(self):
        return self._corpo

    corpo = property(getcorpo,setcorpo)
    cabeçalho = property(getcabeçalho,setcabeçalho)
    
