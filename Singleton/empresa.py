from voo import voo
from passageiro import passageiro
from rota import rota
from passagem import passagem
from aviao import aviao

class empresa(object):
    __instance = None
    __nomes = []
    def __new__(cls,nome):
        if empresa.__instance is None :
           empresa.__instance = object.__new__(cls)
           empresa.__instance.__nome = nome
           empresa.__nomes.append(nome)
           empresa.__instance.__voos = []
           empresa.__instance.__rotas = []
           empresa.__instance.__passageiros = []
           empresa.__instance.__passagens = []
           empresa.__instance.__avioes = []
           return empresa.__instance
        if (empresa.__instance is not None):
            conf = False
            for x in empresa.__nomes:
                if(nome==x):
                    conf =True
            if(not conf):
               __instance = None
               empresa.__nomes.append(nome)
               empresa.__instance = object.__new__(cls)
               empresa.__instance.__nome = nome
               empresa.__instance.__voos = []
               empresa.__instance.__rotas = []
               empresa.__instance.__passageiros = []
               empresa.__instance.__passagens = []
               empresa.__instance.__avioes = []
               return empresa.__instance
            else:
                print("Nao pode ter duas empresas com o mesmo nome")
        

    def getnome_empresa(self):
        return self.__nome
    def setpassageiros(self,passageiro):
        self.__passageiros.append(passageiro)
    
    def setvoos(self,voo):
        self.__voos.append(voo)
    
    def setrotas(self,rota):
        self.__rotas.append(rota)
    
    def setavioes(self,aviao):
        self.__avioes.append(aviao)
    
    def setpassagens(self,passagem):
        self.__passagens.append(passagem)
    def listar_passageiros(self):
        for x in self.__passageiros:
            print("Nome:",x.nome_passageiro)
            print("Id:",x.id_passageiro)
            print("Email:",x.email)
            print("Telefone:",x.telefone)
    def listar_rotas(self):
        for x in self.__rotas:
            print("Id da rota:",x.id_rota)
            print("Hora de saida:",x.hora_saida)
            print("Cidade de origem:",x.cidade_origem)
            print("Cidade de destino:",x.cidade_destino)
    def listar_avioes(self):
        for x in self.__avioes:
            print("Id aviao:",x.id_aviao)
            print("Nome aviao:",x.nome_aviao)
            print("Velocidade do aviao:",x.velocidade)
            print("Capacidade do aviao",x.qtd_pass)
    def listar_passagens(self):
        for x in self.__passagens:
            print("Id da passagem:",x.passagem,"Id passageiro:",x.passageiro)
            print("Id voo:",x.getid_voo())
    def listar_voos(self):
        for x in self.__voos:
            print("Id do voo:",x.id_voo)
            print("Id do aviao:",x.id_aviao)
            print("Id da rota:",x.id_rota)
            print("Hora de chegada:",x.hora_chegada)
            print("Duraçao do voo:",x.duracao_voo)
    nome = property(getnome_empresa)
    listar_voo = property(listar_voos)
    listar_passagem = property(listar_passagens)
    listar_aviao = property(listar_avioes)
    listar_passageiro = property(listar_passageiros)
    listar_rota = property(listar_rotas)
    cad_passageiros = property(setpassageiros)
    cad_voos = property(setvoos)
    cad_rotas = property(setrotas)
    cad_avioes = property(setavioes)
            
    
    
