from futebolista import Futebolista, Jogador, Treinador

if __name__ == "__main__":

#   futebolista = Futebolista("Gabigol", "Brasil", "Santos FC", 30, 100000)
#   Não dá certo pois não é possível instanciar uma superclasse abstrata.


    jogador1 = Jogador("Lamine Yamal", "Espanha", "FC Barcelona", 19, 400000, "PD", 200000000, 120)

    print(f"\n{jogador1.get_nome()} \n-Nacionalidade: {jogador1.get_nacionalidade()} \n-Clube: {jogador1.get_clube()} \n-Idade: {jogador1.get_idade()} \n-Salário: ${jogador1.get_salario():.2f} \n-Posição: {jogador1.get_posicao()} \n-Valor de mercado: ${jogador1.get_valor():.2f} \n-Gols: {jogador1.get_gols()}")


    jogador2 = Jogador("Alisson", "Brasil", "Liverpool FC", 34, 100000, "GK")

    print(f"\n{jogador2.get_nome()} \n-Nacionalidade: {jogador2.get_nacionalidade()} \n-Clube: {jogador2.get_clube()} \n-Idade: {jogador2.get_idade()} \n-Salário: ${jogador2.get_salario():.2f} \n-Posição: {jogador2.get_posicao()} \n-Valor de mercado: ${jogador2.get_valor():.2f} \n-Gols: {jogador2.get_gols()}")


    jogador1.set_nome("Kyllian Mbappé")
    jogador1.set_nacionalidade("França")
    jogador1.set_clube("Real Madrid")
    jogador1.set_idade(27)
    jogador1.set_salario(500000)
    jogador1.set_posicao("ATA")
    jogador1.set_valor(190000000)
    jogador1.set_gols(511)

    print(f"\n{jogador1.get_nome()} \n-Nacionalidade: {jogador1.get_nacionalidade()} \n-Clube: {jogador1.get_clube()} \n-Idade: {jogador1.get_idade()} \n-Salário: ${jogador1.get_salario():.2f} \n-Posição: {jogador1.get_posicao()} \n-Valor de mercado: ${jogador1.get_valor():.2f} \n-Gols: {jogador1.get_gols()}")


    jogador1.bonus()
    print(f"\nSalário do {jogador1.get_nome()} com o bônus: ${jogador1.get_salario():.2f}\n")

    jogador2.aniversario()

    jogador1.gols_partida(3)
    print(f"\nQuantidade de gols do {jogador1.get_nome()} após a última partida: {jogador1.get_gols()} gols")



    treinador1 = Treinador("Luis Enrique", "Espanha", "PSG", 56, 150000, "Pressão Alta", "433", 17)

    print(f"\n{treinador1.get_nome()} \n-Nacionalidade: {treinador1.get_nacionalidade()} \n-Clube: {treinador1.get_clube()} \n-Idade: {treinador1.get_idade()} \n-Salário: ${treinador1.get_salario():.2f} \n-Estilo tático: {treinador1.get_tatica()} \n-Formação: {treinador1.get_formacao()} \n-Títulos: {treinador1.get_titulos()}")


    treinador2 = Treinador("Pep Guardiola", "Espanha", "-", 54, 0, "Tiki-Taka", "433")

    print(f"\n{treinador2.get_nome()} \n-Nacionalidade: {treinador2.get_nacionalidade()} \n-Clube: {treinador2.get_clube()} \n-Idade: {treinador2.get_idade()} \n-Salário: ${treinador2.get_salario():.2f} \n-Estilo tático: {treinador2.get_tatica()} \n-Formação: {treinador2.get_formacao()} \n-Títulos: {treinador2.get_titulos()}")


    treinador1.set_nome("José Mourinho")
    treinador1.set_nacionalidade("Portugal")
    treinador1.set_clube("Real Madrid")
    treinador1.set_idade(64)
    treinador1.set_salario(200000)
    treinador1.set_tatica("Park the bus")
    treinador1.set_formacao(451)
    treinador1.set_titulos(32)

    print(f"\n{treinador1.get_nome()} \n-Nacionalidade: {treinador1.get_nacionalidade()} \n-Clube: {treinador1.get_clube()} \n-Idade: {treinador1.get_idade()} \n-Salário: ${treinador1.get_salario():.2f} \n-Estilo tático: {treinador1.get_tatica()} \n-Formação: {treinador1.get_formacao()} \n-Títulos: {treinador1.get_titulos()}")


    treinador1.bonus()
    print(f"\nSalário do {treinador1.get_nome()} com o bônus: ${treinador1.get_salario():.2f}\n")
    
    treinador2.aniversario()

    treinador1.ganhou_titulo()
    print(f"\nQuantidade de títulos do {treinador1.get_nome()} após a última partida: {treinador1.get_titulos()} títulos\n")
