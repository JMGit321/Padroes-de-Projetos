class aviao(object):

    def __init__(self):
        try:
            aviao.id+=1
        except:
            aviao.id = 0
        self._id_aviao = aviao.id
        self._nome_aviao = None
        self._qtd_pass = 0
        self._velocidade = 0

    def setnome_aviao(self,nome):
        self._nome_aviao = nome
    def setqtd_pass(self,qtd):
        if(qtd<1 ):
            print("Valor invalido para a quantidade de passageiros")
        else:
            self._qtd_pass = qtd
    def setvelocidade(self,velocidade):
        if(velocidade<1):
            print("Velocidade invalida para o avião")
        else:
            self._velocidade = velocidade
    def getvelocidade(self):
        return self._velocidade
    def getnome_aviao(self):
        return self._nome_aviao
    def getqtd_pass(self):
        return self._qtd_pass
    def getid_aviao(self):
        return self._id_aviao
    qtd_pass = property(getqtd_pass,setqtd_pass)
    velocidade = property(getvelocidade,setvelocidade)
    nome_aviao = property(getnome_aviao,setnome_aviao)
    id_aviao = property(getid_aviao)
