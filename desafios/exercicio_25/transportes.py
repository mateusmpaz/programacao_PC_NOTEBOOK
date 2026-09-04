from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia,fator):
        self.distancia = distancia
        self.fator = fator

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self,distancia):
        super().__init__(distancia, 0.5)

    def calc_frete(self):
        return self.fator * self.distancia


class Caminhao(Transporte):
    def __init__(self,distancia):
        super().__init__(distancia, 1.2)

    def calc_frete(self):
        if self.distancia < 50:
            return "Distancia precisa ser no minimo 50km"
        else:
            return self.fator * self.distancia


class Drone(Transporte):
    def __init__(self,distancia):
        super().__init__(distancia, 9.5)

    def calc_frete(self):
        if self.distancia >10:
            return "Distancia precisa ser menor que 10km"
        else:
            return self.fator * self.distancia

