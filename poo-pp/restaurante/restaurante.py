from abc import ABC, abstractmethod


class Restaurante(ABC):

    total_restaurantes = 0

    @classmethod
    def get_total(cls):
        return cls.total_restaurantes

    def __init__(self, nome, preco_medio, pessoas_dia, rating = 4.5):
        self.nome = nome
        self.preco_medio = preco_medio
        self.pessoas_dia = pessoas_dia
        self.rating = rating
        Restaurante.total_restaurantes += 1


    def get_nome(self):
        return self.nome
     
    def get_preco_medio(self):
        return self.preco_medio
     
    def get_pessoas_dia(self):
        return self.pessoas_dia
     
    def get_rating(self):
        return self.rating


    def set_nome(self, novo_nome):
        self.nome = novo_nome
        
    def set_preco_medio(self, novo_preco_medio):
        self.preco_medio = novo_preco_medio

    def set_pessoas_dia(self, novo_pessoas_dia):
        self.pessoas_dia = novo_pessoas_dia

    def set_rating(self, novo_rating):
        if novo_rating >= 0:
            self.rating = novo_rating
        else:
            print("Erro: o valor do rating não pode ser negativo.")


    @abstractmethod
    def descricao(self):
        ...

    @abstractmethod
    def luxo(self):
        ...


    def faturamento_diario(self):
        return self.preco_medio * self.pessoas_dia




class Pizzaria(Restaurante):

    def __init__(self, nome, preco_medio, pessoas_dia, rating, tipo_borda, tipo_forno, gramatura_massa = 80, q_sabores = 10):
        super().__init__(nome, preco_medio, pessoas_dia, rating)
        self.tipo_borda = tipo_borda
        self.tipo_forno = tipo_forno
        self.gramatura_massa = gramatura_massa
        self.q_sabores = q_sabores


    def get_tipo_borda(self):
        return self.tipo_borda
         
    def get_tipo_forno(self):
        return self.tipo_forno
         
    def get_gramatura_massa(self):
        return self.gramatura_massa
         
    def get_q_sabores(self):
        return self.q_sabores
    
    
    def set_tipo_borda(self, novo_tipo_borda):
        self.tipo_borda = novo_tipo_borda
            
    def set_tipo_forno(self, novo_tipo_forno):
        self.tipo_forno = novo_tipo_forno
    
    def set_gramatura_massa(self, novo_gramatura_massa):
        self.gramatura_massa = novo_gramatura_massa
    
    def set_q_sabores(self, novo_q_sabores):
        if novo_q_sabores >= 0:
            self.q_sabores = novo_q_sabores
        else:
            print("Erro: a quantidade de sabores não pode ser negativa.")


    def descricao(self):
        print(f"Pizzaria com forno {self.tipo_forno} e {self.q_sabores} sabores no cardápio!")

    def luxo(self):
        if self.preco_medio > 60:
            print("Pizzaria de Luxo!")
        else:
            print("Pizzaria Comum.")





class Hamburgueria(Restaurante):

    def __init__(self, nome, preco_medio, pessoas_dia, rating, tipo_pao, tipo_chapa, gramatura_carne = 100, q_hamburguers = 8):
        super().__init__(nome, preco_medio, pessoas_dia, rating)
        self.tipo_pao = tipo_pao
        self.tipo_chapa = tipo_chapa
        self.gramatura_carne = gramatura_carne
        self.q_hamburguers = q_hamburguers


    def get_tipo_pao(self):
        return self.tipo_pao
         
    def get_tipo_chapa(self):
        return self.tipo_chapa
         
    def get_gramatura_carne(self):
        return self.gramatura_carne
         
    def get_q_hamburguers(self):
        return self.q_hamburguers
    
    
    def set_tipo_pao(self, novo_tipo_pao):
        self.tipo_pao = novo_tipo_pao
            
    def set_tipo_chapa(self, novo_tipo_chapa):
        self.tipo_chapa = novo_tipo_chapa
    
    def set_gramatura_carne(self, novo_gramatura_carne):
        self.gramatura_carne = novo_gramatura_carne
    
    def set_q_hamburguers(self, novo_q_hamburguers):
        if novo_q_hamburguers >= 0:
            self.q_hamburguers = novo_q_hamburguers
        else:
            print("Erro: a quantidade de hambúrgueres não pode ser negativa.")


    def descricao(self):
        print(f"Hamburgueria com pão {self.tipo_pao} e {self.q_hamburguers} hambúrgueres no cardápio!")

    def luxo(self):
        if self.preco_medio > 60:
            print("Hamburgueria de Luxo!")
        else:
            print("Hamburgueria Comum.")    