

lista = []

while True:
    n = int(input("Valor inteiro a entrar na lista (0 para sair): "))
    if n == 0:
        break
    lista.append(n)

print(lista)
print(f"Maior valor da lista: {max(lista)}")
print(f"Média aritmética dos valores da lista: {sum(lista) / len(lista)}")

lista[2] = 77
print(lista)

remove = int(input("Valor para remover da lista: "))
lista.remove(remove)
print(lista)


