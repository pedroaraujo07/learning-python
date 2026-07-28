class Selecao:

    def __init__(self, nome, rank, copas, continente):
        self.nome = nome
        self.rank = rank
        self.copas = copas
        self.continente = continente
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0
        self.pontos = 0
        self.c_mata_mata = 0
        self.fase = "Fase de grupos"


    def partida(self, gols_marcados1, gols_sofridos1):
        self.gols_marcados += gols_marcados1
        self.gols_sofridos += gols_sofridos1
        if gols_marcados1 > gols_sofridos1:
            self.vitorias += 1
            self.pontos += 3

        elif gols_marcados1 == gols_sofridos1:
            self.empates += 1
            self.pontos += 1

        else:
            self.derrotas += 1

    
    def mata_mata(self, gols_marcados2, gols_sofridos2):
        self.c_mata_mata += 1
        self.gols_marcados += gols_marcados2
        self.gols_sofridos += gols_sofridos2

        if gols_marcados2 > gols_sofridos2:
            self.vitorias += 1

        elif gols_marcados2 == gols_sofridos2:
            self.empates += 1

        else:
            self.derrotas += 1

        if self.c_mata_mata == 1:
            self.fase = "16 Avos de Final"
        elif self.c_mata_mata == 2:
            self.fase = "Oitavas de Final"
        elif self.c_mata_mata == 3:
            self.fase = "Quartas de Final"
        elif self.c_mata_mata == 4:
            self.fase = "Semifinal"
        elif self.c_mata_mata == 5:
            self.fase = "Final"


    def campeao(self):
        self.fase = "Campeão"
        


    def __str__(self):
        return (f"Seleção: {self.nome} \nRank: {self.rank} \nCopas: {self.copas} \nContinente: {self.continente} \nVitórias: {self.vitorias} \nEmpates: {self.empates} \nDerrotas: {self.derrotas} \nGols Marcados: {self.gols_marcados} \nGols Sofridos: {self.gols_sofridos} \nPontos na Fase de Grupos: {self.pontos} \nFase em que parou: {self.fase}")
    
    

brasil = Selecao("Brasil", 5, 5, "América do Sul")

argentina = Selecao("Argentina", 2, 3, "América do Sul")

brasil.partida(1, 1)
brasil.partida(3, 0)
brasil.partida(3, 0)
brasil.mata_mata(2, 1)
brasil.mata_mata(1, 2)



print(brasil)


