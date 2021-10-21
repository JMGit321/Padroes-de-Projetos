from aviao import aviao
from rota import rota
class voo(object):
    def __init__(self,aviao,rota):
        try:
            self._id_voo+=1
        except:
            self._id_voo = 0
        self._id_aviao = aviao.getid_aviao()
        self._id_rota = rota.id_rota
        self._duracao_voo = 0
        self._hora_chegada = 0
    def sethora_chegada(self,hora_chegada):
        self._hora_chegada = hora_chegada
    def gethora_chegada(self):
        return self._hora_chegada
    def setduracao_voo(self,rota):
        self._duracao_voo = self._hora_chegada - rota.gethora_saida()
    def getduracao_voo(self):
        return self._duracao_voo
    def getid_voo(self):
        return self._id_voo
    def getid_rota(self):
        return self._id_rota
    id_voo = property(getid_voo)
    id_aviao = property(aviao.getid_aviao)
    id_rota = property(getid_rota)
    hora_chegada = property(gethora_chegada,sethora_chegada)
    duracao_voo = property(getduracao_voo,setduracao_voo)
    
        
