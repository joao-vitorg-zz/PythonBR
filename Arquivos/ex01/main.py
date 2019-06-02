"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos.
"""


def read_entrada():
    valido, invalido = '[Endereços válidos:]\n', '[Endereços inválidos:]\n'
    with open('entrada.txt') as entrada:
        for ip in entrada.read().splitlines():
            if int(max(ip.split('.'), key=int)) <= 255:
                valido += ip + '\n'
            else:
                invalido += ip + '\n'

    return valido, invalido


def write_saida():
    valido, invalido = read_entrada()
    with open('saida.txt', 'w') as saida:
        saida.write(valido + '\n')
        saida.write(invalido)


if __name__ == '__main__':
    write_saida()
