"""Lição 08 - Super"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa): #SUB CLASSE
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []

class Funcionario(Pessoa): #SUB CLASSE
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

cliente = Cliente('João', 'da Silva', '123.456.789-00')
print(cliente.obtem_nome_completo())
print(type(cliente))

funcionario = Funcionario('Maria', 'Santos', '987.654.321-00', 5000)
print(funcionario.obtem_nome_completo())
print(type(funcionario))
