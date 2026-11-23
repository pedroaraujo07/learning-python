from abc import ABC, abstractmethod


class Funcionario(ABC):

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, novo_salario):
        if novo_salario >= 0:
            self.salario = novo_salario
        else:
            print("Erro: o valor do salário não pode ser negativo.")
    
    @abstractmethod
    def bonificacao(self):
        pass


class Diretor(Funcionario):

    def __init__(self, nome, salario, departamento="TI"):
        super().__init__(nome, salario)
        self.departamento = departamento

    def bonificacao(self):
        return self.salario * 11.5/100
    

if __name__ == "__main__":

    diretor1 = Diretor("Carlos", 15000, "RH")
    diretor2 = Diretor("Ana", 18000)

    print(f"Diretor 1: {diretor1.get_nome()}")
    print(f"Bonificação: {diretor1.bonificacao()}")

    diretor1.set_salario(17000)
    diretor1.get_salario()

    diretor2.set_salario(-10000)