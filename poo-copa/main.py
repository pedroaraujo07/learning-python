from selecao import Selecao
from grupo import Grupo
from partida import Partida


grupo_a = Grupo("A")


grupo_c = Grupo("C")

brasil = Selecao("Brasil", 5, 5, "América do Sul")

argentina = Selecao("Argentina", 2, 3, "América do Sul")





print(brasil)


grupo_c.add_selecao(brasil)
print(grupo_c)
