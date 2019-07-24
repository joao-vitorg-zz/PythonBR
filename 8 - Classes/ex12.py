# -*- coding: utf-8 -*-

# Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
# com a diferença de que se adicione um atributo taxaJuros.
# Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
# Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
# Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.


class ContaInvestimento(object):
    def __init__(self, nome, saldo, taxa_juros):
        self.nome = nome.title()
        self.taxa = taxa_juros
        self.montante = saldo
        self.capital = saldo
        self.juros = 0
        self.tempo = 0

    def adicione_juros(self):
        self.tempo += 1
        self.montante = self.capital * (1 + self.taxa / 100) ** self.tempo
        self.juros = self.montante - self.capital

    def __str__(self):
        return """
╔════════╤═════════════╤══════════╤═════════╤════════════╤══════════╗
║ Nome   │ Montante(M) │ Juros(J) │ Taxa(I) │ Capital(C) │ Tempo(T) ║
╟────────┼─────────────┼──────────┼─────────┼────────────┼──────────╢
║ {:<6.6} │ {:<11.2f} │ {:<8.2f} │ {:<7.2f} │ {:<10.2f} │ {:<8} ║
╚════════╧═════════════╧══════════╧═════════╧════════════╧══════════╝
""".format(self.nome, self.montante, self.juros, self.taxa, self.capital, self.tempo)


if __name__ == '__main__':
    conta = ContaInvestimento('Zé', 1000, 10)

    conta.adicione_juros()
    conta.adicione_juros()
    conta.adicione_juros()
    conta.adicione_juros()
    conta.adicione_juros()

    print(conta)
