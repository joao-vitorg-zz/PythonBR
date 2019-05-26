"""
Classe Quadrado: Crie uma classe que modele um quadrado:

    a. Atributos: Tamanho do lado
    b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, lado):
        self.lado = lado

    @property
    def area(self):
        return self.lado ** 2

    @property
    def perimetro(self):
        return 4 * self.lado

    def __str__(self):
        return """
╔══════╤═══════╤═══════════╗
║ Lado │ Área  │ Perímetro ║
╟──────┼───────┼───────────╢
║ {0:<4.1f} │ {1:<5.1f} │ {2:<9.1f} ║
╚══════╧═══════╧═══════════╝
""".format(self.lado, self.area, self.perimetro)
