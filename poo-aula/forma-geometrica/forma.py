from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):

    contador = 0

    @classmethod
    def get_contador(cls):
        return cls.contador
    

    def __init__(self, cor):
        self.cor = cor
        FormaGeometrica.contador += 1

    
    def get_cor(self):
        return self.cor
    

    def set_cor(self, novo_cor):
        self.cor = novo_cor


    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetro(self):
        pass



class Quadrado(FormaGeometrica):

    def __init__(self, cor, lado = 0):
        super().__init__(cor)
        self.lado = lado


    def get_lado(self):
        return self.lado
    

    def set_lado(self, novo_lado):
        if novo_lado > 0:
            self.lado = novo_lado
        else:
            print("Erro: o novo lado não pode ter valor negativo")


    def area(self):
        return self.lado ** 2
    

    def perimetro(self):
        return self.lado * 4
    


class Circulo(FormaGeometrica):

    def __init__(self, cor, raio = 0):
        super().__init__(cor)
        self.raio = raio
    

    def get_raio(self):
        return self.raio
    

    def set_raio(self, novo_raio):
        if novo_raio > 0:
            self.raio = novo_raio
        else:
            print("Erro: o novo raio não pode ter valor negativo")


    def area(self):
        return math.pi * (self.raio ** 2)
    

    def perimetro(self):
        return 2 * self.raio * math.pi