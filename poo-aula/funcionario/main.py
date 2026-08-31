from funcionario import Funcionario
from gerente import Gerente

if __name__ == "__main__":

    funcionario1 = Funcionario("Pedro", 100000.00)
    funcionario2 = Funcionario("Vinícius", 1621.00)

    gerente1 = Gerente("Pedro", 300000.00, 2)
    gerente2 = Gerente("Arrascaeta", 20000.00, 1)

    print(f"Funcionário 1: {funcionario1}")

    print(f"\nFuncionário {funcionario1.get_nome()} \n-Salário: R${funcionario1.get_salario():.2f}\n")

    funcionario2.set_nome("Carlos")
    funcionario2.set_salario(200000.00)

    print(f"\nFuncionário {funcionario2.get_nome()} \n-Salário: R${funcionario2.get_salario():.2f}\n")

    print(f"\nGerente {gerente1.get_nome()} \n- Salário: R${gerente1.get_salario():.2f} \n- Quantidade de Funcionários Gerenciados: {gerente1.get_qnt_gerencia()} \n")

    gerente2.set_nome("Bruno Henrique")

    print(f"Bônus f1: R${funcionario1.bonus():.2f}")
    print(f"Bônus g1: R${gerente1.bonus():.2f}")

