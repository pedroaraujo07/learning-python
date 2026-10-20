from abc import ABC, abstractmethod


class Futebolista(ABC):

    def __init__(self, nome, nacionalidade, clube, idade, salario = 10000):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.clube = clube
        self.idade = idade
        self.salario = salario


    def get_nome(self):
        return self.nome
    
    def get_nacionalidade(self):
        return self.nacionalidade
    
    def get_clube(self):
        return self.clube
    
    def get_idade(self):
        return self.idade
    
    def get_salario(self):
        return self.salario


    def set_nome(self, novo_nome):
        self.nome = novo_nome
         
    def set_nacionalidade(self, novo_nacionalidade):
        self.nacionalidade = novo_nacionalidade
         
    def set_clube(self, novo_clube):
        self.clube = novo_clube
         
    def set_idade(self, novo_idade):
        if novo_idade > 0:
            self.idade = novo_idade
        else:
            print("Erro: a idade não pode ser um valor negativo.")
         
    def set_salario(self, novo_salario):
        if novo_salario > 0:
            self.salario = novo_salario
        else:
            print("Erro: o salário não pode ser um valor negativo.")


    def aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome} pelos seus {self.idade} anos!")


    @abstractmethod
    def bonus(self):
        ...



class Jogador(Futebolista):

    def __init__(self, nome, nacionalidade, clube, idade, salario, posicao, valor = 1000000, gols = 0):
        super().__init__(nome, nacionalidade, clube, idade, salario)
        self.posicao = posicao
        self.valor = valor
        self.gols = gols


    def get_posicao(self):
        return self.posicao
     
    def get_valor(self):
        return self.valor
     
    def get_gols(self):
        return self.gols


    def set_posicao(self, novo_posicao):
        self.posicao = novo_posicao
             
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("Erro: o valor não pode ser negativo.")
             
    def set_gols(self, novo_gols):
        if novo_gols > 0:
            self.gols = novo_gols
        else:
            print("Erro: os gols não podem ter um valor negativo.")


    def bonus(self):
        if self.gols > 100:
            self.salario *= 1.10


    def gols_partida(self, q_gols):
        self.gols += q_gols



     
class Treinador(Futebolista):

    def __init__(self, nome, nacionalidade, clube, idade, salario, tatica, formacao, titulos = 0):
        super().__init__(nome, nacionalidade, clube, idade, salario)
        self.tatica = tatica
        self.formacao = formacao
        self.titulos = titulos


    def get_tatica(self):
        return self.tatica
     
    def get_formacao(self):
        return self.formacao
     
    def get_titulos(self):
        return self.titulos


    def set_tatica(self, novo_tatica):
        self.tatica = novo_tatica
             
    def set_formacao(self, novo_formacao):
        self.formacao = novo_formacao
             
    def set_titulos(self, novo_titulos):
        if novo_titulos > 0:
            self.titulos = novo_titulos
        else:
            print("Erro: os títulos não podem ter um valor negativo.")


    def bonus(self):
        if self.titulos > 5:
            self.salario *= 1.10


    def ganhou_titulo(self):
        self.titulos += 1
     