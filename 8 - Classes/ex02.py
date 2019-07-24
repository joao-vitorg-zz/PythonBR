# -*- coding: utf-8 -*-

# Classe Quadrado: Crie uma classe que modele um quadrado:
#    a. Atributos: Tamanho do lado
#    b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado(object):
    def __init__(self, lado):
        self.lado = lado

    @property
    def area(self):
        return self.lado ** 2

    @property
    def perimetro(self):
        return 4 * self.lado

    def __str__(self):
        return """
╔══════════╤══════════╤═══════════════╗
║ Lado(cm) │ Área(cm) │ Perímetro(cm) ║
╟──────────┼──────────┼───────────────╢
║ {:<8.1f} │ {:<8.1f} │ {:<13.1f} ║
╚══════════╧══════════╧═══════════════╝
""".format(self.lado, self.area, self.perimetro)


if __name__ == '__main__':
    lado = float(input('Lado: '))

    quadrado = Quadrado(lado)
    print(quadrado)
