
def area(b, h):
    return (b * h / 2)

def circulo(r):
    return (3.14 * r**2)

if __name__ == "__main__":
    print("--------------------------------")
    print("CALCULADORA DE ÁREA DE TRIÂNGULO")
    print("--------------------------------")
    medida = input("Medida a ser usada (m, cm, ...): ")
    base = float(input("Valor da base do triângulo: "))
    altura = float(input("Valor da altura do triângulo: "))
    print(f"Área do triângulo: {area(base, altura)}{medida}")

    print()
    escolha1 = input('Digite "s" calcular também a área do círculo: ')
    if escolha1 == "s":
        print()
        print("------------------------------")
        print("CALCULADORA DE ÁREA DE CÍRCULO")
        print("------------------------------")
        medida2 = input("Medida a ser usada (m, cm, ...): ")
        raio = float(input("Valor do raio do círculo: "))
        print(f"Área do círculo: {circulo(raio)}{medida2}")
    