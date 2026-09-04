from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):

    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 4*self.lado
    
    def area(self):
        return self.lado*self.lado

class Circulo(Poligono):

    def __init__(self, raio):
        self.raio = raio

    def perimetro(self):
        return 2*pi*self.raio

    def area(self):
        return pi*self.raio*self.raio
 