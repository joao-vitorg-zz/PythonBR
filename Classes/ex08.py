"""
Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e
pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e
verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro.
É possível criar um macaco canibal?
"""


class Macaco:
    def __init__(self, nome):
        self.nome = nome.title()
        self.bucho = []

    def comer(self, x):
        self.bucho.append(x)

    def digerir(self):
        self.bucho = []

    def ver_bucho(self):
        bucho = "╔\n"
        for x in self.bucho:
            bucho += "║ " + str(x) + '\n'
        bucho += "╚"
        return bucho

    def __str__(self):
        return self.nome


if __name__ == '__main__':
    harambe = Macaco('Harambe')
    donkey = Macaco('Donkey')

    donkey.comer('Banana')
    donkey.comer('Coco')
    donkey.comer('Maça')
    donkey.comer(harambe)

    print(donkey.ver_bucho())
