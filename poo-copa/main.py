class Selecao:

    def __init__(self, nome, rank, continente):
        self.nome = nome
        self.rank = rank
        self.continente = continente
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.pontos = 0

    def ganhar_partida(self, quant_v):
        self.vitorias += 1 * quant_v
        self.pontos += 3 * quant_v

    def empatar_partida(self, quant_e):
        self.empates += 1 * quant_e
        self.pontos += 1 * quant_e

    def perder_partida(self, quant_d):
        self.derrotas += 1 * quant_d

    def __str__(self):
        return (f"Seleção: {self.nome} \nRank: {self.rank}\nContinente: {self.continente} \nVitórias: {self.vitorias} \nEmpates: {self.empates} \nDerrotas: {self.derrotas} \nPontos: {self.pontos} ")
    
    

brasil = Selecao("Brasil", 5, "América do Sul")

argentina = Selecao("Argentina", 2, "América do Sul")

brasil.ganhar_partida(2)

brasil.empatar_partida(1)

print(brasil)


