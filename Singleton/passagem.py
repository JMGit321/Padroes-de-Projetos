from voo import voo
from passageiro import passageiro
class passagem(object):
        def __init__(self,passageiro,voo):
            try:
                self._id_passagem+=1
            except:
                self._id_passagem = 0
            self._id_passageiro = passageiro.getid_passageiro()
            self._id_voo = voo.getid_voo()
        def getid_passagem(self):
            return self._id_passagem
        def get_id_passageiro(self):
                return self._id_passageiro
        def getid_voo(self):
                return self._id_voo
        passagem = property(getid_passagem)
        passageiro = property(get_id_passageiro)
