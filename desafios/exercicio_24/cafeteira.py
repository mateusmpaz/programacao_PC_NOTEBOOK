from abc import ABC, abstractmethod 

class BebidaQuente(ABC):

    def preparar(self):
        print("---INICIANDO O PREPARO---")
        print(self.ferver_agua())
        print(self.misturar())
        print(self.servir())
        print("---BEBIDA PRONTA---\n")

    def ferver_agua(self):
        return "1. Fervendo água a 100 graus Celsius"

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):


    def misturar(self):
        return "2. Passando agua pressurizada pelo po de café moído"

    def servir(self):
        return "3. Servindo em xícara pequena"

class Cha(BebidaQuente):


    def misturar(self):
        return "2. Mergulhando o sachê de ervas na agua "

    def servir(self):
        return "3. Servindo na canelca de porcelana com limao"


class Leite(BebidaQuente):

    
    def misturar(self):
        return "2. Passando vapor pressurizado pelo bico do leite "

    def servir(self):
        return "3. Servindo na caneca grande, já com café "
