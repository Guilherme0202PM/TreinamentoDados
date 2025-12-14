# === Aula 02 - Atributos de classe e instância ===

# Classe pessoa possui
# atributos de instância: nome e email
class Pessoa:
    especie = "Homo Sapiens"
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


pessoa1 = Pessoa("Maria da Silva", "maria@email.com")
pessoa2 = Pessoa("João Santos", "joao@email.com")

# Modificando o atributo de classe
# Someente pessoa1 sera alterada
pessoa1.especie = "alienígena"

# Modidica todos os objetos da Classe
Pessoa.especie = "Alienígena do Passado"

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(Pessoa.especie)