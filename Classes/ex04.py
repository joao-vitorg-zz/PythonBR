"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

    a. Atributos: nome, idade, peso e altura
    b. Métodos: Envelhercer, engordar, emagrecer, crescer.
       Obs: Por padrão, a cada ano que nossa pessoa envelhece,
       sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome.title()
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            self.altura += 0.5

    def engordar(self, x):
        self.peso += x

    def emagrecer(self, x):
        self.peso -= x

    def crescer(self, x):
        self.altura += x

    def __str__(self):
        return """
╔════════╤═══════╤═══════╤════════╗
║ Nome   │ Idade │ Peso  │ Altura ║
╟────────┼───────┼───────┼────────╢
║ {:<6.6} │ {:<5} │ {:<5.1f} │ {:<6.1f} ║
╚════════╧═══════╧═══════╧════════╝
""".format(self.nome, self.idade, self.peso, self.altura)


if __name__ == '__main__':
    nome = input('Nome: ')
    idade = float(input('Idade: '))
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))

    pessoa = Pessoa(nome, idade, peso, altura)
    print(pessoa)
