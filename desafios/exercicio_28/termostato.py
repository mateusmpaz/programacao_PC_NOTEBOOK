class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,valor):
        if valor < 16:
            raise ValueError("A temperatura deve estar entre 16°C e 30°C")
        if valor * 2 != int(valor * 2):
            raise ValueError("A temperatura deve variar de 0.5°C em 0.5°C")
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.__temperatura:.1f} graus Celsius"