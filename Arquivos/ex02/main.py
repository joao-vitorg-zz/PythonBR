from json import load

"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o
seguinte arquivo, chamado "usuarios.json":
"""


def read_usuarios():
    with open('usuarios.json') as f:
        user = load(f)
        total = sum(user.values())
        media = total / len(user)
        users = [[n, name, byte / 1048576, (byte * 100) / total] for n, (name, byte) in enumerate(user.items())]

    return [total / 1048576, media / 1048576] + users


def write_relatorio():
    table, users = """╔═════════════════════════════════════════════════╗
║                    ACME Inc.                    ║
╠════╤════════════╤══════════════════════╤════════╣
║    │ Usuário    │ Espaço utilizado(MB) │ uso(%) ║
╟────┼────────────┼──────────────────────┼────────╢""", read_usuarios()

    for values in users[2:]:
        table += "\n║ {:<2} │ {:<10.10} │ {:<20.2f} │ {:<6.2f} ║".format(*values)

    table += """\n╟────┴────────────┴──────────────────────┴────────╢
║                                                 ║
║ Espaço total ocupado(MB): {:<21.2f} ║
║ Espaço médio ocupado(MB): {:<21.2f} ║
╚═════════════════════════════════════════════════╝
""".format(*users[:3])

    with open('relatorio.txt', 'w') as f:
        f.write(table)


if __name__ == '__main__':
    write_relatorio()
