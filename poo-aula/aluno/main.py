from aluno import Aluno

if __name__ == "__main__":

    aluno1 = Aluno("Pedro", 700, 18)

    aluno2 = Aluno("Carlos", 800, 18)

    print(f"Endereço hexadecimal Aluno 1: {aluno1}")
    print(f"Endereço hexadecimal Aluno 2: {aluno2}")

    print(f"\nAluno 1:\nNome: {aluno1.get_nome()} \nIdade: {aluno1.get_idade()} \nMensalidade: {aluno1.get_mensalidade()}")

    print(aluno2)

    aluno2.set_nome("Vini")

    print(aluno2)