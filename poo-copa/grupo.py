
from selecao import Selecao


class Grupo:

    def __init__(self, letra):
        self.grupo = []
        self.letra = letra

    def add_selecao(self, selecao):
        if selecao in self.grupo:
            print(f"Aviso: {selecao.nome} já está no Grupo {self.letra}!")
            return

        if len(self.grupo) == 4:
            print(f"Aviso: o limite máximo de seleções do Grupo {self.letra} foi atingido!")
            return

        self.grupo.append(selecao)


    def __str__(self):
        selecoes_grupo = ""
        for i in self.grupo:
            selecoes_grupo += (f"- {i.nome}\n")
        return (f"Grupo {self.letra}: \n{selecoes_grupo}")