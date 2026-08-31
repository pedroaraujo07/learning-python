from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, nome, salario=0.00, qnt_gerencia=1):
        super().__init__(nome, salario)
        self.qnt_gerencia = qnt_gerencia

    
    def get_qnt_gerencia(self):
        return self.qnt_gerencia
    

    def set_qnt_gerencia(self, novo_qnt_gerencia):
        self.qnt_gerencia = novo_qnt_gerencia
