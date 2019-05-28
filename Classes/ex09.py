"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

    a. Possua uma classe chamada Ponto, com os atributos x e y.
    b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
    c. Possua uma função para imprimir os valores da classe Ponto
    d. Possua uma função para encontrar o centro de um Retângulo.
    e. Você deve criar alguns objetos da classe Retangulo.
    f. Cada objeto deve ter um vértice de partida, por exemplo, o
       vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
    g. A função para encontrar o centro do retângulo deve retornar o
       valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
    h. O valor do centro do objeto deve ser mostrado na tela
    i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return """
╔═══════╤═══════╗
║ X(cm) │ Y(cm) ║
╟───────┼───────╢
║ {:<5.1f} │ {:<5.1f} ║
╚═══════╧═══════╝
""".format(self.x, self.y)


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro(self):
        x = self.largura / 2
        y = self.altura / 2
        return Ponto(x, y)

    def __str__(self):
        return """
╔═════════════╤════════════╗
║ Largura(cm) │ Altura(cm) ║
╟─────────────┼────────────╢
║ {:<11.1f} │ {:<10.1f} ║
╚═════════════╧════════════╝
      Centro{}
""".format(self.largura, self.altura, self.centro())


if __name__ == '__main__':
    largura = float(input('Largura: '))
    altura = float(input('Altura: '))

    retangulo = Retangulo(largura, altura)
    print(retangulo)
