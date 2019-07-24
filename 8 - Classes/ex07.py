# -*- coding: utf-8 -*-

# Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#    a. Atributos: Nome, Fome, Saúde e Idade
#    b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
#    Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
#    este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
#    então não devemos criar um atributo para armazenar esta informação
#    por que ela pode ser calculada a qualquer momento.

from time import time


class Tamagushi(object):
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

    def alimetar(self):
        self._fome = self.analiza(self.fome + 20)

    @property
    def saude(self):
        return self._saude - self.tempo // 1

    def curar(self):
        self._saude = self.analiza(self.saude + 10)

    @property
    def idade(self):
        return self.tempo // 1

    @property
    def humor(self):
        return self.analiza((self.saude + self.fome) / 2)
