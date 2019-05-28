"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

    a. Um veículo tem um certo consumo de combustível (medidos em km/litro) e
       uma certa quantidade de combustível no tanque.
    b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
    c. Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância,
       reduzindo o nível de combustível no tanque de gasolina.
    d. Forneça um método obterGasolina(), que retorna o nível atual de combustível.
    e. Forneça um método adicionarGasolina(), para abastecer o tanque.
"""


class Carro:
    def __init__(self, combustivel, consumo):
        self.combustivel = combustivel
        self.consumo = consumo

    def andar(self, km):
        quantidade = km * self.consumo
        if self.combustivel >= quantidade:
            self.combustivel -= quantidade
        else:
            print('Combustível insuficiente')

    def obter_gasolina(self):
        return self.combustivel

    def abastecer(self, litros):
        self.combustivel += litros

    def restante(self):
        return round(self.combustivel / self.consumo, 2)

    def __str__(self):
        return """
╔═══════════╤═══════════════╤══════════════╗
║ Tanque(L) │ Consumo(Km/l) │ Restante(Km) ║
╟───────────┼───────────────┼──────────────╢
║ {:<9.2f} │ {:<13.2f} │ {:<12.2f} ║
╚═══════════╧═══════════════╧══════════════╝
""".format(self.combustivel, self.consumo, self.restante())


if __name__ == '__main__':
    combustivel = float(input('Combustível inicial: '))
    consumo = float(input('Consumo: '))

    carro = Carro(combustivel, consumo)
    print(carro)
