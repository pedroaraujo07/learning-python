nomes = []
cont = 0

def create():
    while True:
        nome = input("Digite um nome: ")
        if not nome:
            break
        nomes.append(nome)

def read():
    print(nomes)

def update():
    nomi = input("Digite um novo nome: ")
    posi = int(input(f"Posição do novo nome (1 a {cont}): "))
    if posi > 0 and posi <= cont:
        nomes[posi - 1] = nomi
    else:
        print("Você deve digitar uma posição válida.")

def delete():
    nomx = input("Nome para ser excluido: ")
    if nomx in nomes:
        nomes.remove(nomx)
    else:
        print("Nenhum nome removido")

if __name__ == "__main__":
    while True:
        print("[c] - Create (inserir um item) \n[r] - Read (mostrar toda a lista) \n[u] - Update (substituir um item) \n[d] - Delete (remover um item) \n[e] - Exit (sair)")
        opc = input("Opção: ")
        print()
        match opc:
            case "e":
                print("Encerrando...")
                break
            case "c":
                create()
                print()
            case "r":
                read()
                print()
            case "u":
                cont = len(nomes)
                update()
                print()
            case "d":
                delete()
                print()
            case _:
                print("Opção inválida.\n")
        
