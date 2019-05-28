from time import time

"""
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual,
permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e
por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem
quão rapidamente os níveis de fome e tédio caem.
"""


class Tamagushi:
    def __init__(self, nome):
        self.nome = nome.title()
        self._fome = 100
        self._saude = 100
        self._inicial = time()

    def analiza(self, x):
        if x > 100:
            return 100
        elif x < 0:
            return 0
        else:
            return x

    @property
    def tempo(self):
        return time() - self._inicial

    @property
    def fome(self):
        return self._fome - self.tempo // 0.5

    @fome.setter
    def fome(self, x):
        self._fome = self.analiza(x)

    @property
    def saude(self):
        return self._saude - self.tempo // 1

    @saude.setter
    def saude(self, x):
        self._saude = self.analiza(x)

    @property
    def idade(self):
        return self.tempo // 1

    @property
    def humor(self):
        return self.analiza((self.saude + self.fome) / 2)
