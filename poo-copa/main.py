from selecao import Selecao
from grupo import Grupo
from partida import Partida


grupo_a = Grupo("A")
mexico = Selecao("México", 10, 0, "América do Norte")
africa_do_sul = Selecao("África do Sul", 54, 0, "África")
coreia = Selecao("Coréia do Sul", 32, 0, "Ásia")
tchequia = Selecao("Tchéquia", 48, 0, "Europa")
grupo_a.add_selecao(mexico)
grupo_a.add_selecao(africa_do_sul)
grupo_a.add_selecao(coreia)
grupo_a.add_selecao(tchequia)
partida_a1 = Partida(mexico, africa_do_sul)
partida_a1.jogar(2, 0)
partida_a2 = Partida(coreia, tchequia)
partida_a2.jogar(2, 1)
partida_a3 = Partida(tchequia, africa_do_sul)
partida_a3.jogar(1, 1)
partida_a4 = Partida(mexico, coreia)
partida_a4.jogar(1, 0)
partida_a5 = Partida(africa_do_sul, coreia)
partida_a5.jogar(1, 0)
partida_a6 = Partida(tchequia, mexico)
partida_a6.jogar(0, 3)

grupo_b = Grupo("B")
canada = Selecao("Canadá", 30, 0, "América do Norte")
bosnia = Selecao("Bósnia", 61, 0, "Europa")
catar = Selecao("Catar", 59, 0, "Ásia")
suica = Selecao("Suíça", 14, 0, "Europa")
grupo_b.add_selecao(canada)
grupo_b.add_selecao(bosnia)
grupo_b.add_selecao(catar)
grupo_b.add_selecao(suica)
partida_b1 = Partida(canada, bosnia)
partida_b1.jogar(1, 1)
partida_b2 = Partida(catar, suica)
partida_b2.jogar(1, 1)
partida_b3 = Partida(suica, bosnia)
partida_b3.jogar(4, 1)
partida_b4 = Partida(canada, catar)
partida_b4.jogar(6, 0)
partida_b5 = Partida(suica, canada)
partida_b5.jogar(2, 1)
partida_b6 = Partida(bosnia, catar)
partida_b6.jogar(3, 1)


grupo_c = Grupo("C")

brasil = Selecao("Brasil", 5, 5, "América do Sul")

argentina = Selecao("Argentina", 2, 3, "América do Sul")


print(grupo_a)
print(mexico)
print(africa_do_sul)
print(coreia)
print(tchequia)

print(grupo_b)
print(canada)
print(bosnia)
print(catar)
print(suica)
