"""
Classe Bola: Crie uma classe que modele uma bola:

    a. Atributos: Cor, circunferência, material
    b. Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, material, circulo, cor):
        self.material = material.title()
        self.circulo = circulo
        self._cor = cor.title()

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, x):
        self._cor = x

    def __str__(self):
        return """
╔══════════╤═════════╤══════════╗
║ Material │ Círculo │ Cor      ║
╟──────────┼─────────┼──────────╢
║ {0:<8.8} │ {1:<7.2f} │ {2:<8.8} ║
╚══════════╧═════════╧══════════╝
""".format(self.material, self.circulo, self.cor)


if __name__ == '__main__':
    material = input('Material: ')
    circulo = float(input('Circulo: '))
    cor = input('Cor: ')

    bola = Bola(material, circulo, cor)
    print(bola)
