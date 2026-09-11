from abc import ABC, abstractmethod
import random 

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []


    def atacar(self,alvo,forca= 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]    
            print(f"{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com um {golpe} de força {forca}")
            alvo.receber_dano(forca)
        else:
            print("O ataque nao pode acontecer")


    def receber_dano(self,dano):    
        fator = random.randint(0,dano)
        self.vida -= fator

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nome} recebeu dano de {fator}")


    @abstractmethod
    def curar(self):
        pass



class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de Machado", "Pulo Giratorio"]

    def curar(self):
        fator = random.randint(0,100)
        self.vida += fator 
        print(f"{self.nome} curou {fator} pontos de vida")


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "chamas cinzentas", "Nevoa sombria"]



    def curar(self):
        fator = random.randint(0,100)
        self.vida += fator 
        print(f"{self.nome} curou {fator} pontos de vida")