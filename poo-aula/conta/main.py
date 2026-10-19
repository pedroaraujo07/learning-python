from conta import Conta
from conta import PessoaFisica
from conta import PessoaJuridica

if __name__ == "__main__":

    pf1 = PessoaFisica("Pedro", 10, "Homem")
    pf2 = PessoaFisica("Carlos", 5)
    pf3 = PessoaFisica("Vinícius")


    print(f"\n{pf1.get_nome()}: \n-Saldo: {pf1.get_saldo()} reais \n-Gênero: {pf1.get_genero()}\n")

    pf1.set_nome("Lucas")
    pf2.set_saldo(8)
    pf3.set_genero("Homem")

    pj1 = PessoaJuridica("PH Imports", 45000, "MEI")
    pj2 = PessoaJuridica("FutCore", 60000)
    pj2 = PessoaJuridica("GreenBet")

    

    