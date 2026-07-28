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
        self.cont_mata_mata = 0
        self.fase = "Fase de grupos"


    def partida_grupos(self, gols_marcados_fgrupos, gols_sofridos_fgrupos):
        self.gols_marcados += gols_marcados_fgrupos
        self.gols_sofridos += gols_sofridos_fgrupos
        if gols_marcados_fgrupos > gols_sofridos_fgrupos:
            self.vitorias += 1
            self.pontos += 3

        elif gols_marcados_fgrupos == gols_sofridos_fgrupos:
            self.empates += 1
            self.pontos += 1

        else:
            self.derrotas += 1

    
    def partida_mata_mata(self, gols_marcados_mata, gols_sofridos_mata):
        self.cont_mata_mata += 1
        self.gols_marcados += gols_marcados_mata
        self.gols_sofridos += gols_sofridos_mata

        if gols_marcados_mata > gols_sofridos_mata:
            self.vitorias += 1

        elif gols_marcados_mata == gols_sofridos_mata:
            self.empates += 1

        else:
            self.derrotas += 1

        if self.cont_mata_mata == 1:
            self.fase = "16 Avos de Final"
        elif self.cont_mata_mata == 2:
            self.fase = "Oitavas de Final"
        elif self.cont_mata_mata == 3:
            self.fase = "Quartas de Final"
        elif self.cont_mata_mata == 4:
            self.fase = "Semifinal"
        elif self.cont_mata_mata == 5:
            self.fase = "Final"

    def campeao(self):
        self.fase = "Campeão"
        


    def __str__(self):
        return (f"Seleção: {self.nome} \nRank: {self.rank} \nCopas: {self.copas} \nContinente: {self.continente} \nVitórias: {self.vitorias} \nEmpates: {self.empates} \nDerrotas: {self.derrotas} \nGols Marcados: {self.gols_marcados} \nGols Sofridos: {self.gols_sofridos} \nPontos na Fase de Grupos: {self.pontos} \nFase em que parou: {self.fase}")
    
    