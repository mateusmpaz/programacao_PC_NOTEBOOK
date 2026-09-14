from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self,nome):
        self.nome = nome
        self.salario = 0

    salario_min = 1612
    inss = 7.5

    def analisar_salario(self):
        print(f"o Salario de {self.nome} corresponde a {self.salario/self.salario_min:.2f} salarios minimos")


    @abstractmethod
    def calc_sal(self):
        pass

class Horista(Funcionario):
    def __init__(self, nome, valor_hora= 7.37,horas_trab=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.salario = self.valor_hora * self.horas_trab * ((100-self.inss)/100)
        print (f"o salario de {self.nome} e R${self.salario:.2f}")


class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calc_sal(self):
        self.salario = self.salario_bruto * ((100-self.inss)/100)
        print (f"o salario de {self.nome} e R${self.salario:.2f}")