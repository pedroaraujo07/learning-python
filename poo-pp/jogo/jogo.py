

class Jogo:

    def __init__(self, nome, preco, ano_lancamento, melhor_jogador):
        self.nome = nome
        self.preco = preco
        self.ano_lancamento = ano_lancamento
        self.melhor_jogador = melhor_jogador


    def get_nome(self):
        return self.nome
    
    def get_preco(self):
        return self.preco
    
    def get_ano_lancamento(self):
        return self.ano_lancamento
    
    def get_melhor_jogador(self):
        return self.melhor_jogador


    def set_nome(self, novo_nome):
        self.nome = novo_nome
        
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
        else:
            print("Erro: o preço não pode ser negativo.")

    def set_ano_lancamento(self, novo_ano_lancamento):
        if novo_ano_lancamento >= 1947:
            self.ano_lancamento = novo_ano_lancamento
        else:
            print(f"Erro: em {novo_ano_lancamento}, nenhum jogo havia sido criado ainda.")

    def set_melhor_jogador(self, novo_melhor_jogador):
        self.melhor_jogador = novo_melhor_jogador


    def dados(self):
        print(f"\n{self.get_nome()} \n-Preço: R${self.get_preco():.2f} \n-Ano de lançamento: {self.get_ano_lancamento()} \n-Melhor jogador: {self.get_melhor_jogador()} \n")


    def aumenta_preco(self, aumento):
        if aumento >= 0:
            self.preco += aumento
        else:
            print("Erro: o aumento não pode ser negativo.")


    def idade(self):
        return 2026 - self.get_ano_lancamento()

