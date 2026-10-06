from alimento import Alimento
from alimento import Fruta


if __name__ == "__main__":

    alimento1 = Alimento("Pão de forma", 15)
    alimento2 = Alimento("Manteiga", 10)

    print(f"\n{alimento1.get_nome()} \n-Preço: {alimento1.get_preco()}")

    alimento2.set_nome("Mortadela")
    alimento2.set_preco(20)
    print(f"\n{alimento2.get_nome()} \n-Preço: {alimento2.get_preco()}")



    fruta1 = Fruta("Banana", 5, "Amarelo")
    fruta2 = Fruta("Morango", 8, "Vermelho")

    print(f"\n{fruta1.get_nome()} \n-Preço: {fruta1.get_preco()} \n-Cor: {fruta1.get_cor()}")

    fruta2.set_nome("Uva Roxa")
    fruta2.set_preco(4)
    fruta2.set_cor("Roxo")

    print(f"\n{fruta2.get_nome()} \n-Preço: {fruta2.get_preco()} \n-Cor: {fruta2.get_cor()}")


    print(fruta1.comer())
    alimento1.comer()