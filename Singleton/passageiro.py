class passageiro(object):
    def __init__(self):
        try:
            passageiro.id +=1
        except:
            passageiro.id = 0
        self._id_passageiro = passageiro.id
        self._nome_passageiro = None
        self._telefone = None
        self._email = None
    def setnome(self,nome):
        self._nome_passageiro = nome
    def settelefone(self,telefone):
        self._telefone = telefone
    def setemail(self,email):
        self._email = email
    def getemail(self):
        return self._email
    def gettelefone(self):
        return self._telefone
    def getnome_passageiro(self):
        return self._nome_passageiro
    def getid_passageiro(self):
        return self._id_passageiro

    nome_passageiro = property(getnome_passageiro,setnome)
    id_passageiro = property(getid_passageiro)
    email = property(getemail,setemail)
    telefone = property(gettelefone,settelefone)
