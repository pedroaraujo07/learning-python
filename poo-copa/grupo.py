
from selecao import Selecao


class Grupo:

    def __init__(self, letra):
        self.grupo = []
        self.letra = letra

    def add_selecao(self, selecao):
        self.grupo.append(selecao)


    def __str__(self):
        selecoes_grupo = ""
        for i in self.grupo:
            selecoes_grupo += (f"- {i.nome}\n")
        return (f"Grupo {self.letra}: \n{selecoes_grupo}")