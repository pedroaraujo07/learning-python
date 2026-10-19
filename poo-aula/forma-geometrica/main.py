from forma import FormaGeometrica, Quadrado, Circulo


quadrado1 = Quadrado("Azul", 7)
quadrado2 = Quadrado("Amarelo")

print(f"\nQuadrado 1 \n-Cor: {quadrado1.get_cor()} \n-Medida do lado: {quadrado1.get_lado()} \n-Área: {quadrado1.area()} \n-Perímetro: {quadrado1.perimetro()}\n")
print(f"Quadrado 2 \n-Cor: {quadrado2.get_cor()} \n-Medida do lado: {quadrado2.get_lado()} \n-Área: {quadrado2.area()} \n-Perímetro: {quadrado2.perimetro()}\n")

quadrado2.set_cor("Verde")

print(f"Cor do quadrado 2 atualizada: {quadrado2.get_cor()}\n")

quadrado1.set_lado(10)
quadrado2.set_lado(-1)



circulo1 = Circulo("Azul", 5)
circulo2 = Circulo("Amarelo")

circulo2.set_raio(10)

print(f"Círculo 1 \n-Cor: {circulo1.get_cor()} \n-Medida do raio: {circulo1.get_raio()} \n-Área: {circulo1.area():.2f} \n-Perímetro: {circulo1.perimetro():.2f}\n")
print(f"Círculo 2 \n-Cor: {circulo2.get_cor()} \n-Medida do raio: {circulo2.get_raio()} \n-Área: {circulo2.area():.2f} \n-Perímetro: {circulo2.perimetro():.2f}\n")

circulo2.set_cor("Verde")

print(f"Cor do circulo 2 atualizada: {circulo2.get_cor()}\n")

circulo1.set_raio(10)
circulo2.set_raio(-1)


print(f"\nTotal de formas: {FormaGeometrica.get_contador()}\n")