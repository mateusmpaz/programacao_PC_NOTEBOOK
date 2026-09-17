class Avaliacao:
    def __init__(self,aluno,disciplina,nota):
        self.nome = aluno
        self.disciplina = disciplina 
        self._nota = nota

    # metodos acessores 
    def get_nota(self): # metodo getter 
        return self._nota


    def set_nota(self, valor): # metodo setter 
        if  0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota invalida!")
