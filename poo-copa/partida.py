
from selecao import Selecao

class Partida:

    def __init__(self, selecao1, selecao2):
        self.selecao1 = selecao1
        self.selecao2 = selecao2


    def jogar(self, gols1, gols2):
            
        if self.selecao1.cont_fgrupos <= 3:
            self.selecao1.partida_grupos(gols1, gols2)
            self.selecao2.partida_grupos(gols2, gols1)
        else:
            self.selecao1.partida_mata_mata(gols1, gols2)
            self.selecao2.partida_mata_mata(gols2, gols1)

        