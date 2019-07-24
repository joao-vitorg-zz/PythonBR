# -*- coding: utf-8 -*-

# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o
# seguinte arquivo, chamado "usuarios.json"
# coloque os arquivos na pasta usuários.
# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.

import webbrowser as web
from os import scandir


class ACME(object):
    def __init__(self):
        user = {folder.name: self.folder_size(folder) for folder in scandir('usuarios') if folder.is_dir()}
        self.total, self.media, self.users = sum(user.values()), 0, ()
        if self.total:
            self.media = self.total / len(user)
            self.users = [[name, byte, (byte * 100) / self.total] for name, byte in user.items()]
            self.users.sort(key=lambda x: x[2], reverse=True)
        elif len(user) > 0:
            self.users = [[name, 0, 0] for name in user]

        self.write_html()
        web.open('web/index.html')

    def folder_size(self, folder):
        total = 0
        for entry in scandir(folder):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += self.folder_size(entry.path)
        return total

    def write_html(self):
        html = """<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
        <title>ACME</title>
    </head>
    <body>
        <table>
            <tr>
                <th>ID</th>
                <th>Usuário</th>
                <th>Espaço utilizado</th>
                <th>Percentual</th>
            </tr>"""

        for n, values in enumerate(self.users, 1):
            html += """
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{:.2f} B</td>
                <td>{:.2f}%</td>
            </tr>""".format(n, *values)

        html += """
        </table>
        <br>
        <table>
            <tr>
                <th>Espaço total ocupado</th>
                <th>Espaço médio ocupado</th>
            </tr>
            <tr>
                <td>{:.2f} B</td>
                <td>{:.2f} B</td>
            </tr>
        </table>
    </body>
</html>
""".format(self.total, self.media)

        with open('web/index.html', 'w') as f:
            f.write(html)


if __name__ == '__main__':
    ACME()
