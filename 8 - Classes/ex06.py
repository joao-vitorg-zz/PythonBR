# -*- coding: utf-8 -*-

# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
#    a. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
#    b. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.


class TV(object):
    def __init__(self, canal=1, volume=1):
        self.volume = volume
        self.canal = canal

    def set_canal(self, x):
        if 0 <= x <= 100:
            self.canal = x

    def set_voume(self, x):
        if 0 <= x <= 100:
            self.volume = x

    def up_volume(self):
        self.volume += 1

    def down_volume(self):
        self.volume -= 1

    def __str__(self):
        return """
╔═══════╤════════╗
║ Canal │ Volume ║
╟───────┼────────╢
║ {:<5} │ {:<6} ║
╚═══════╧════════╝
""".format(self.canal, self.volume)


if __name__ == '__main__':
    canal = int(input('Canal: '))
    volume = int(input('Volume: '))

    tv = TV(canal, volume)
    print(tv)
