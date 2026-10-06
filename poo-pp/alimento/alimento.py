

class Alimento:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco


    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
        else:
            print("Erro: o preço não pode ser negativo.")


    def comer(self):
        return f"Você comeu {self.nome}!"



class Fruta(Alimento):

    def __init__(self, nome, preco, cor):
        super().__init__(nome, preco)
        self.cor = cor


    def get_cor(self):
        return self.cor


    def set_cor(self, novo_cor):
        if type(novo_cor) == str:
            self.cor = novo_cor
        else:
            print("Erro: A cor precisa ser um texto, não número ou outro")
