magro = 999
m50 = 0
soma = 0
gordo = -1
p50 = 0


for i in range (1, 6 + 1, 1):
    peso = float(input(f"Digite o peso da {i}ª pessoa (em kg): "))
    soma += peso
    if peso < magro:
        magro = peso
    if peso >= 50:
        p50 += peso
        m50 += 1
    if peso > gordo:
        gordo = peso

print(f"Média artitmética do peso das pessoas: {soma/i}kg")
print(f"Peso da pessoa mais magra: {magro}kg")
print(f"Peso da pessoa mais gorda: {gordo}kg")
print(f"Quantidade de pessoas com 50kg ou mais: {m50}")
print(f"Média de peso das pessoas com 50kg ou mais: {p50 / m50}")
