from veiculo import Veiculo

if __name__ == "__main__":

    carro1 = Veiculo("Carro", "Toyota", "Corolla", 2016, 90000)

    carro2 = Veiculo("Carro", "Honda", "Civic", 2017, 80000)

    print(f"Modelo carro 1: {carro1.get_modelo()}")
    print(carro2)

    carro1.set_valor(92000)
    print(f"\n\nNovo valor do {carro1.get_modelo()}: {carro1.get_valor()}")

    carro2.set_valor(210000)
    print(f"\n\nNovo valor do {carro2.get_modelo()}: {carro2.get_valor()}")

    carro1.set_valor(float(input(f"\nDigite o novo valor do {carro1.get_modelo()} (em R$): ")))
    print(f"Novo valor do {carro1.get_modelo()}: {carro1.get_valor()}")

    carro2.aumenta_valor(50000)

    print(f"\nNovo valor do {carro2.get_modelo()} após aumento: {carro2.get_valor()}")