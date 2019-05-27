"""
Classe Retangulo: Crie uma classe que modele um retangulo:

    a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
       de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e
       de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura

    @property
    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def piso(self, largura, altura):
        pisos = self.area / (largura * altura)
        return """
╔════════════╗
║ Pisos(qty) ║
╟────────────╢
║ {0:<10.1f} ║
╚════════════╝
""".format(pisos)

    def __str__(self):
        return """
╔═════════╤════════╤════════╤═══════════╗
║ Largura │ Altura │  Área  │ Perímetro ║
╟─────────┼────────┼────────┼───────────╢
║ {0:<7.1f} │ {1:<6.1f} │ {2:<6.1f} │ {3:<9.1f} ║
╚═════════╧════════╧════════╧═══════════╝
""".format(self.largura, self.altura, self.area, self.perimetro)


if __name__ == '__main__':
    largura = float(input('Largura: '))
    altura = float(input('Altura: '))

    retangulo = Retangulo(largura, altura)
    print(retangulo)

    p_largura = float(input('Largura do piso: '))
    p_altura = float(input('Alturado piso: '))
    print(retangulo.piso(p_largura, p_altura))
