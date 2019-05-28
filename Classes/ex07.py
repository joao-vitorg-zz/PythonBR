from time import time

"""
Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
    a. Atributos: Nome, Fome, Saúde e Idade 
    b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade

    Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, 
    este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, 
    então não devemos criar um atributo para armazenar esta informação 
    por que ela pode ser calculada a qualquer momento.
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

    def __str__(self):
        return """
╔════════╤═════════╤══════════╤══════════╤═══════╗
║ Nome   │ Fome(%) │ Saúde(%) │ Humor(%) │ Idade ║
╟────────┼─────────┼──────────┼──────────┼───────╢
║ {:<6.6} │ {:<7.2f} │ {:<8.2f} │ {:<8.2f} │ {:<5.0f} ║
╚════════╧═════════╧══════════╧══════════╧═══════╝
""".format(self.nome, self.fome, self.saude, self.humor, self.idade)
