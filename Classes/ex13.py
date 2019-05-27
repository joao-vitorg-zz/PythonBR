"""
Classe Funcionário: Implemente a classe Funcionário.
Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
Escreva um pequeno programa que teste sua classe.
"""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome.title()
        self.salario = salario

    def get_nome(self):
        return self.nome

    def set_nome(self, x):
        self.nome = x

    def get_salario(self):
        return self.salario

    def set_salario(self, x):
        self.salario = x

    def __str__(self):
        return """
╔════════╤═══════════╗
║ Nome   │ Salario   ║
╟────────┼───────────╢
║ {:<6.6} │ {:<9.2f} ║
╚════════╧═══════════╝
""".format(self.nome, self.salario)


if __name__ == '__main__':
    funcionario = Funcionario('', 0)

    nome = input('Nome: ')
    salario = float(input('Salário: '))

    funcionario.set_nome(nome)
    funcionario.set_salario(salario)

    print(funcionario)
