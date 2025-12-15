"""Lição 06 - eq hash"""


# Este código demonstra como funciona a comparação de igualdade e o uso de hash em Python,
# tanto para tipos primitivos (como strings) quanto para objetos definidos pelo usuário.
#
# No início, é mostrado que duas strings com o mesmo conteúdo são consideradas iguais
# quando comparadas com o operador ==.
#
# Em seguida, é definida a classe Pessoa, que sobrescreve métodos especiais do Python:
# - __eq__: define quando dois objetos Pessoa devem ser considerados iguais.
#   Neste caso, duas pessoas são iguais se possuírem o mesmo CPF.
# - __hash__: define o valor de hash do objeto, também baseado no CPF.
#   Isso permite que objetos Pessoa sejam usados corretamente em estruturas baseadas em hash,
#   como sets e dicionários.
# - __repr__: define uma representação textual do objeto, facilitando a visualização no print.
#
# O código cria três objetos Pessoa, sendo dois com o mesmo CPF.
# Ao inserir esses objetos em um set, o Python utiliza __hash__ e __eq__
# para garantir que não existam duplicatas com base no CPF.
#
# Por fim, o código compara objetos Pessoa usando == e mostra a diferença de comportamento
# entre um set (que elimina duplicatas com base no hash) e uma lista (que permite duplicatas).
#
# Tecnologia / Conceito principal utilizado:
# - Programação Orientada a Objetos
# - Métodos especiais (__eq__, __hash__, __repr__)
# - Estruturas baseadas em hash (set)
# - Comparação de objetos personalizada


nome1 = "Joaquim"
nome2 = "Joaquim"

print(nome1 == nome2)

class Pessoa:
    def __int__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f"Pessoa({self.cpf}, {self.nome})"

pessoa1 = Pessoa("100100100-10", "Joaquim")
pessoa2 = Pessoa("100100100-10", "Joaquim")
pessoa3 = Pessoa("100100100-11", "Maria")

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)

print(pessoa1 == pessoa2)

pessoas_listas = [pessoa1, pessoa2, pessoa3]
print(pessoas_listas)

print(pessoas_listas.count(pessoa1))