

class Veiculo:

    def __init__(self, tipo, marca, modelo, ano, valor):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def get_tipo(self):
        return self.tipo    

    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo    

    def get_ano(self):
        return self.ano

    def get_valor(self):
        return(f"R${self.valor:.2f}")    
    
    
    def set_tipo(self, novo_tipo):
        self.tipo = novo_tipo

    def set_marca(self, novo_marca):
        self.marca = novo_marca

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def set_valor(self, novo_valor):
        self.valor = novo_valor


    def aumenta_valor(self, valor_aumentado):
        self.valor += valor_aumentado

    
    def __str__(self):
        return(f"\nTipo: {self.get_tipo()} \nMarca: {self.get_marca()} \nModelo: {self.get_modelo()} \nAno: {self.get_ano()} \nValor: {self.get_valor()}")