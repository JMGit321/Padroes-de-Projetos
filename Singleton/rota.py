class rota(object):
   
    def __init__(self):
        try:
            rota.id +=1
        except:
            rota.id=0
        self._id_rota = rota.id
        self._cidade_origem = None
        self._cidade_destino = None
        self._hora_saida = 0
    def setcidade_origem(self,cidade_origem):
            self._cidade_origem = cidade_origem
    def setcidade_destino(self,cidade_destino):
        if(cidade_destino == self._cidade_origem):
            print("Cidade de destino não pode ser a de origem,digite outra")
        else:
            self._cidade_destino = cidade_destino
    def sethora_saida(self,hora):
        self._hora_saida = hora
    def gethora_saida(self):
        return self._hora_saida
    def getcidade_origem(self):
        return self._cidade_origem
    def getcidade_destino(self):
        return self._cidade_destino
    def getid_rota(self):
        return self._id_rota
    cidade_origem = property(getcidade_origem,setcidade_origem)
    cidade_destino = property(getcidade_destino,setcidade_destino)
    hora_saida = property(gethora_saida,sethora_saida)
    id_rota = property(getid_rota)
    
