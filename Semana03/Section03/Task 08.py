"""Lição 08 - Super"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.compras = []

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
