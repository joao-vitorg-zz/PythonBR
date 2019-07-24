# -*- coding: utf-8 -*-

# Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista.
# Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho,
# exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação
# para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
# Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

from random import randint
from time import time


class Tamagushi(object):
    def __init__(self, nome):
        self.nome = nome.title()
        self._fome = randint(50, 101)
        self._saude = randint(50, 101)
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

    def alimetar(self):
        self._fome = self._analiza(self.fome + 20)

    def curar(self):
        self._saude = self._analiza(self.saude + 10)


class Fazenda(object):
    def __init__(self, nbichinhos, ):
        self.bichinhos = [Tamagushi(n) for n in nbichinhos]

    def alimentar(self):
        for bichinho in self.bichinhos:
            bichinho.alimetar()

    def curar(self):
        for bichinho in self.bichinhos:
            bichinho.curar()
