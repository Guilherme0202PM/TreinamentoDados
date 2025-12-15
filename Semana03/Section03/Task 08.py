"""Lição 08 - Super"""

#O problema do código está na criação do objeto Programador. A classe Programador exige cinco parâmetros no construtor: nome, sobrenome, cpf, salario e bonus. No entanto, o objeto foi criado passando apenas quatro valores, sem o bônus. Isso causa um erro porque o parâmetro bonus é obrigatório. Para corrigir, é necessário informar também o valor do bônus ao criar o objeto Programador.

#O super é uma função usada em classes que herdam de outras classes. Ele serve para acessar métodos da classe pai a partir da classe filha. No código, o super está sendo utilizado para chamar o método init da classe Pessoa dentro das classes Cliente, Funcionario e Programador. Isso garante que os atributos nome, sobrenome e cpf sejam corretamente inicializados sem repetir código.

#Além disso, o super também é usado no método calcular_pagamento da classe Programador para reaproveitar o cálculo de pagamento feito na classe Funcionario e depois adicionar o bônus específico do programador. O benefício do uso do super é evitar duplicação de código, manter a hierarquia de herança organizada e facilitar a manutenção e a extensão do sistema.
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

    def calcular_pagamento(self):
        return self.salario - ((10/100) * self.salario)
    
class Programador(Funcionario): #SUB CLASSE
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcular_pagamento(self):
        pagamento = super().calcular_pagamento()
        return pagamento + self.bonus
    

cliente = Cliente('João', 'da Silva', '123.456.789-00')
print(cliente.obtem_nome_completo())
print(type(cliente))

funcionario = Funcionario('Maria', 'Santos', '987.654.321-00', 5000)
print(funcionario.obtem_nome_completo())
print(type(funcionario))

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

    def calcular_pagamento(self):
        return self.salario - ((10/100) * self.salario)
    
class Programador(Funcionario): #SUB CLASSE
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcular_pagamento(self):
        pagamento = super().calcular_pagamento()
        return pagamento + self.bonus
    
    
cliente = Cliente('João', 'da Silva', '123.456.789-00')
print(cliente.obtem_nome_completo())
print(type(cliente))

funcionario = Funcionario('Maria', 'Santos', '987.654.321-00', 5000)
print(funcionario.obtem_nome_completo())
print(type(funcionario))

programador = Programador('Clara', 'Santos', '987.654.321-00', 5000, 1000)
print(programador.obtem_nome_completo())
print(type(programador))
print(programador.calcular_pagamento())

