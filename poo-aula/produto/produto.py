

class Produto:

    def __init__(self, nome, v_compra, v_venda, q_estoque=100, q_minima=5):
        self.nome = nome
        self.v_compra = v_compra
        self.v_venda = v_venda
        self.q_estoque = q_estoque
        self.q_minima = q_minima


    def get_nome(self):
        return self.nome
    
    def get_v_compra(self):
        return self.v_compra
    
    def get_v_venda(self):
        return self.v_venda
    
    def get_q_estoque(self):
        return self.q_estoque
    
    def get_q_minima(self):
        return self.q_minima
    

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_v_venda(self, novo_v_venda):
        if novo_v_venda >= 0:
            self.v_venda = novo_v_venda
        else:
            print("Erro: Valores negativos não são permitidos!")


    def calcula_lucro(self):
        return self.v_venda - self.v_compra


    def __str__(self):
        return(f"\n{self.get_nome()}\n-Valor de compra: R${self.get_v_compra():.2f}\n-Valor de venda: R${self.get_v_venda():.2f} \n-Lucro: R${self.calcula_lucro():.2f} \n-Quantidade em estoque: {self.get_q_estoque()}\n-Quantidade mínima: {self.get_q_minima()}\n")