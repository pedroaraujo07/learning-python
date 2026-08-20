

class Atleta:

    def __init__(self, nome, esporte, idade, salario):
        self.nome = nome
        self.esporte = esporte
        self.idade = idade
        self.salario = salario


    def get_nome(self):
        return self.nome
    
    def get_esporte(self):
        return self.esporte
    
    def get_idade(self):
        return self.idade
    
    def get_salario(self):
        return self.salario


    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def set_esporte(self, novo_esporte):
        self.esporte = novo_esporte
    
    def set_idade(self, novo_idade):
        self.idade = novo_idade
    
    def set_salario(self, novo_salario):
        self.salario = novo_salario


    def aumenta_salario(self, aumento_salario):
        self.salario += aumento_salario


    def melhor_do_mundo(self):
        return(f"Para mim, o {self.nome} é o melhor atleta do mundo!")



if __name__ == "__main__":

    atleta1 = Atleta("Neymar Jr", "Futebol", 34, 4100000.00)

    atleta2 = Atleta("Stephen Curry", "Basquete", 38, 5210000.00)

    atleta3 = Atleta("Charles Oliveira", "MMA", 36, 750000.00)


    print(f"\n{atleta1.get_nome()} \n-Esporte: {atleta1.get_esporte()} \n-Idade: {atleta1.get_idade()} \n-Salário Mensal: {atleta1.get_salario():.2f} \n")
    
    print(f"\n{atleta2.get_nome()} \n-Esporte: {atleta2.get_esporte()} \n-Idade: {atleta2.get_idade()} \n-Salário Mensal: {atleta2.get_salario():.2f} \n")
    
    print(f"\n{atleta3.get_nome()} \n-Esporte: {atleta3.get_esporte()} \n-Idade: {atleta3.get_idade()} \n-Salário Mensal: {atleta3.get_salario():.2f} \n")


    atleta3.set_nome("Sandrey")
    atleta3.set_esporte("Futevôlei")
    atleta3.set_idade(26)
    atleta3.set_salario(35000.00)

    print(f"\n{atleta3.get_nome()} \n-Esporte: {atleta3.get_esporte()} \n-Idade: {atleta3.get_idade()} \n-Salário Mensal: {atleta3.get_salario():.2f} \n")


    atleta3.aumenta_salario(5000)
    print(f"{atleta3.get_salario():.2f}")

    print(atleta1.melhor_do_mundo())