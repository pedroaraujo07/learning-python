from jogo import Jogo

if __name__ == "__main__":

    jogo1 = Jogo("Rocket League", 0, 2015, "Zen")
    jogo2 = Jogo("EAFC 26", 300, 2025, "RvPLegend")
    jogo3 = Jogo("Rainbow Six", 100, 2015, "Cyber")
    jogo4 = Jogo("Fortnite", 0, 2017, "Peterbot")

    jogo1.dados()
    jogo2.dados()
    jogo3.dados()
    jogo4.dados()

    jogo1.aumenta_preco(float(input(f"Valor do aumento do preço do {jogo1.get_nome()}: ")))
    print(f"Preço do {jogo1.get_nome()}: R${jogo1.get_preco():.2f}")

    jogo1.set_preco(10)
    print(f"Preço do {jogo1.get_nome()}: R${jogo1.get_preco():.2f}")

    jogo1.set_preco(-10)
    print(f"Preço do {jogo1.get_nome()}: R${jogo1.get_preco():.2f}")

    jogo2.set_ano_lancamento(2026)
    print(f"Ano de lançamento do {jogo2.get_nome()}: {jogo2.get_ano_lancamento()}")

    jogo2.set_ano_lancamento(1920)
    print(f"Ano de lançamento do {jogo2.get_nome()}: {jogo2.get_ano_lancamento()}")

    print(f"Idade do {jogo3.get_nome()}: {jogo3.idade()} anos")