from selecao import Selecao
from grupo import Grupo


grupo_a = Grupo("A")
grupo_c = Grupo("C")

brasil = Selecao("Brasil", 5, 5, "América do Sul")

argentina = Selecao("Argentina", 2, 3, "América do Sul")

brasil.partida_grupos(1, 1)
brasil.partida_grupos(3, 0)
brasil.partida_grupos(3, 0)
brasil.partida_mata_mata(2, 1)
brasil.partida_mata_mata(1, 2)



print(brasil)


grupo_c.add_selecao(brasil)
print(grupo_c)
