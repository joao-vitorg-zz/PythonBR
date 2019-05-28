"""
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento)
que aumente o salário do funcionário em uma certa porcentagem.
"""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome.title()
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)

    def __str__(self):
        return """
╔════════╤═════════════╗
║ Nome   │ Salario(R$) ║
╟────────┼─────────────╢
║ {:<6.6} │ {:<11.2f} ║
╚════════╧═════════════╝
""".format(self.nome, self.salario)


if __name__ == '__main__':
    nome = input('Nome: ')
    salario = float(input('Salário: '))
    funcionario = Funcionario(nome, salario)

    porcentagem = int(input('Aumentar o salário em: '))
    funcionario.aumentar_salario(porcentagem)

    print(funcionario)
