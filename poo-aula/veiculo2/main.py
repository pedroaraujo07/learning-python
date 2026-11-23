

class Veiculo:

    def __init__(self, placa, preco):
        self.placa = placa
        self.preco = preco


    def get_preco(self):
        return self.preco


    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
        else:
            print("Erro: o valor do preço não pode ser negativo.")


    def aumentaPreco(self, aumento_preco):
        self.preco += aumento_preco

    
class Onibus(Veiculo):

    def __init__(self, placa, preco, capacidade=12):
        super().__init__(placa, preco)
        self.capacidade = capacidade

    
    def mostraDados(self):
        print(f"Placa: {self.placa} \nPreço: R${self.preco:.2f} \nCapacidade: {self.capacidade} pessoas")



if __name__ == "__main__":

    onibus1 = Onibus("PZD9182", 60000, 14)
    onibus2 = Onibus("JAM9271", 80000)

    onibus2.set_preco(85000)
    onibus1.mostraDados()

    print(onibus2.get_preco())