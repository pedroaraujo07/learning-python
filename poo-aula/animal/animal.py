

class Animal:
    def __init__(self, nome, especie, raca, sexo, idade):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.sexo = sexo
        self.idade = idade

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_idade(self):
        return self.idade