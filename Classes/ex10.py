"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
    a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        i.   tipoCombustivel
        ii.  valorLitro
        iii. quantidadeCombustivel
    b. Possua no mínimo esses métodos:
        i.   abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
             quantidade de litros que foi colocada no veículo
        ii.  abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
             mostra o valor a ser pago pelo cliente.
        iii. alterarValor( ) – altera o valor do litro do combustível.
        iV.  alterarCombustivel( ) – altera o tipo do combustível.
        V.   alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaCombustivel:
    def __init__(self, tipo, valor, quantidade):
        self.quantidade = quantidade
        self.valor = valor
        self.tipo = tipo

    def abastecer_por_valor(self, valor):
        self.quantidade -= valor / self.valor

    def abastecer_por_litro(self, litros):
        self.quantidade -= litros

    def __str__(self):
        return """
╔══════════╤═══════════╤════════╗
║ Tipo     │ Valor(R$) │ Quant. ║
╟──────────┼───────────┼────────╢
║ {:<8.8} │ {:<9.2f} │ {:<6.1f} ║
╚══════════╧═══════════╧════════╝
""".format(self.tipo, self.valor, self.quantidade)


if __name__ == '__main__':
    tipo = input('Tipo: ')
    valor = float(input('Valor: '))
    quant = float(input('Quantidade: '))
    bomba = BombaCombustivel(tipo, valor, quant)

    bomba.abastecer_por_valor(10)
    print(bomba)
