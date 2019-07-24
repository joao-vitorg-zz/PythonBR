# -*- coding: utf-8 -*-

# Classe Bichinho Virtual++: Melhore o programa do bichinho virtual,
# permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e
# por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem
# quão rapidamente os níveis de fome e tédio caem.

from time import time


class Tamagushi(object):
    def __init__(self, nome):
        self.nome = nome.title()
        self._fome = 100
        self._saude = 100
        self._inicial = time()

    @staticmethod
    def _analiza(x):
        return max(min(x, 100), 0)

    @property
    def tempo(self):
        return time() - self._inicial

    @property
    def fome(self):
        return self._fome - self.tempo // 0.5

    @property
    def saude(self):
        return self._saude - self.tempo // 1

    @property
    def idade(self):
        return self.tempo // 1

    @property
    def humor(self):
        return self._analiza((self.saude + self.fome) / 2)

    @fome.setter
    def fome(self, x):
        self._fome = self._analiza(x)

    @saude.setter
    def saude(self, x):
        self._saude = self._analiza(x)
