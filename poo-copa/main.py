class Selecao:

    def __init__(self, nome, rank, continente):
        self.nome = nome
        self.rank = rank
        self.continente = continente
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0
        self.pontos = 0

    def partida(self, gols_marcados_p, gols_sofridos_p):
        if gols_marcados_p > gols_sofridos_p:
            self.vitorias += 1
            self.pontos += 3
            self.gols_marcados += gols_marcados_p
            self.gols_sofridos += gols_sofridos_p

        elif gols_marcados_p == gols_sofridos_p:
            self.empates += 1
            self.pontos += 1
            self.gols_marcados += gols_marcados_p
            self.gols_sofridos += gols_sofridos_p

        else:
            self.derrotas += 1
            self.gols_marcados += gols_marcados_p
            self.gols_sofridos += gols_sofridos_p

    def __str__(self):
        return (f"Seleção: {self.nome} \nRank: {self.rank}\nContinente: {self.continente} \nVitórias: {self.vitorias} \nEmpates: {self.empates} \nDerrotas: {self.derrotas} \nGols Marcados: {self.gols_marcados} \nGols Sofridos: {self.gols_sofridos} \nPontos: {self.pontos} ")
    
    

brasil = Selecao("Brasil", 5, "América do Sul")

argentina = Selecao("Argentina", 2, "América do Sul")

brasil.partida(1, 1)

brasil.partida(3, 0)

brasil.partida(3, 0)



print(brasil)


