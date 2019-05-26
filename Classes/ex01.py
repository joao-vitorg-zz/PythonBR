"""
Classe Bola: Crie uma classe que modele uma bola:

    a. Atributos: Cor, circunferência, material
    b. Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, material, circulo, cor):
        self.material = material.title()
        self.circulo = circulo
        self.cor = cor.title()

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, x):
        self.cor = x

    def __str__(self):
        return """
╔══════════╤═════════╤══════════╗
║ Material │ Círculo │ Cor      ║
╟──────────┼─────────┼──────────╢
║ {0:<8.8} │ {1:<7.2f} │ {2:<8.8} ║
╚══════════╧═════════╧══════════╝
""".format(self.material, self.circulo, self.cor)
