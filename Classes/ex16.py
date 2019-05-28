from time import time

"""
Crie uma "porta escondida" no programa do programa do bichinho virtual que
mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta,
não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.
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
