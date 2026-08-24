from produto import Produto

if __name__ == "__main__":

    produto1 = Produto("RedBull", 5, 11, 100, 12)
    produto2 = Produto("Água mineral Crystal", 0.5, 2.5, 400, 40)

    print(f"Objeto criado: {produto1}")
    print(f"Objeto criado: {produto2}")

    print(f"\nNome do produto: {produto1.get_nome()}\n-Valor de venda: R${produto1.get_v_venda():.2f}\n")

    produto2.set_nome("Água mineral Minalba")
    produto2.set_v_venda(4)
    print(f"\nNome do produto: {produto2.get_nome()}\n-Valor de venda: R${produto2.get_v_venda():.2f}\n")

    produto1.set_v_venda(float(input(f"Digite o novo valor de venda da {produto1.get_nome()}: ")))
    print(f"Valor de venda da {produto1.get_nome()}: R${produto1.get_v_venda():.2f}\n")

    print(produto2)

    print(produto1)