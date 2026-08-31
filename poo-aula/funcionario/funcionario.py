

class Funcionario:

    def __init__(self, nome, salario=0.0):
        self.nome = nome
        self.salario = salario

    
    def get_nome(self):
        return self.nome
    
    def get_salario(self):
        return self.salario
    

    def set_nome(self, novo_nome):
        self.nome = novo_nome
        
    def set_salario(self, novo_salario):
        self.salario = novo_salario


    def bonus(self):
        bonus = self.salario * 0.09
        return bonus
