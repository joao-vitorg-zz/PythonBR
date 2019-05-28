"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
    a. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
    b. Os métodos são os seguintes: alterarNome, depósito e saque;
    c. No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""


class ContaCorrente:
    def __init__(self, nome, numero, saldo):
        self.nome = nome.title()
        self.numero = numero
        self.saldo = saldo

    def deposito(self, x):
        self.saldo += x

    def saque(self, x):
        if 0 < x <= self.saldo:
            self.saldo -= x
        else:
            print('Saldo insuficiente')

    def transferencia(self, valor, destinatario):
        if isinstance(destinatario, ContaCorrente):
            destinatario.deposito(valor)
            self.saque(valor)

    def __str__(self):
        return """
╔════╤════════╤═══════════╗
║ N. │ Nome   │ Saldo(R$) ║
╟────┼────────┼───────────╢
║ {:<2} │ {:<6.6} │ {:<9.2f} ║
╚════╧════════╧═══════════╝
""".format(self.numero, self.nome, self.saldo)


if __name__ == '__main__':
    nome = input('Nome: ')
    numero = int(input('Número: '))
    saldo = float(input('saldo: '))

    conta = ContaCorrente(nome, numero, saldo)
    print(conta)
