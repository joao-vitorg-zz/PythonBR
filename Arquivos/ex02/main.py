from json import load

"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o
seguinte arquivo, chamado "usuarios.json":
"""


def get_user():
    with open('usuarios.json') as f:
        user = load(f)
        total = sum(user.values())
        media = total / len(user)
    return user, total, media


def format_user(user, total):
    for n, (name, byte) in enumerate(user.items(), 1):
        mb = byte / 1048576
        yield n, name, mb, (byte * 100) / total


def set_relatorio():
    user, total, media = get_user()

    table = """╔═════════════════════════════════════════════════╗
║                    ACME Inc.                    ║
╠════╤════════════╤══════════════════════╤════════╣
║    │ Usuário    │ Espaço utilizado(MB) │ uso(%) ║
╟────┼────────────┼──────────────────────┼────────╢"""

    for values in format_user(user, total):
        table += "\n║ {:<2} │ {:<10.10} │ {:<20.2f} │ {:<6.2f} ║".format(*values)

    table += """\n╟────┴────────────┴──────────────────────┴────────╢
║                                                 ║
║ Espaço total ocupado(MB): {:<21.2f} ║
║ Espaço médio ocupado(MB): {:<21.2f} ║
╚═════════════════════════════════════════════════╝
""".format(total / 1048576, media / 1048576)

    with open('relatorio.txt', 'w') as f:
        f.write(table)


if __name__ == '__main__':
    set_relatorio()
