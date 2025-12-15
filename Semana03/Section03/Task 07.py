# === Aula 07 - Relacionamentos entre classes ===

#O relacionamento entre classes ocorre quando uma classe utiliza ou depende de outra para representar melhor um conceito do mundo real. Em vez de concentrar tudo em uma única classe, as responsabilidades são divididas, tornando o código mais organizado e fiel ao domínio do problema.

#Neste exercício, o relacionamento aparece porque a classe Pessoa possui objetos das classes Telefone e Endereco. Isso representa uma relação do tipo tem-um (agregação), onde uma pessoa é composta por um telefone e pode ter um ou mais endereços, ilustrando na prática como classes podem se relacionar para modelar informações mais complexas.

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f"Endereco(cep={self.cep}, numero={self.numero})"

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f"Telefone(ddd={self.ddd}, numero={self.numero})"
    
class Pessoa:
    def __init__(self, cpf, nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = []

    def adicionar_endereco(self, cep, numero):
        self.enderecos.append(Endereco(cep, numero))

    def print_endereco(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)


    def __str__(self):
        return f"Pessoa(cpf={self.cpf}, nome={self.nome}, telefone={self.telefone})"

telefone = Telefone("11", "11 1111-1111")

pessoa1 = Pessoa("11233213", "João da Silva", telefone)
pessoa1.adicionar_endereco('11111111',123)
pessoa1.adicionar_endereco('145d4f111',89)

#ou
#pessoa = Pessoa("11233213", "João da Silva", Telefone("11", "11 1111-1111"))

pessoa2 = Pessoa("11233213", "Maria da Silva", telefone)
pessoa2.adicionar_endereco('11122211',55)



print(pessoa1)
print(pessoa1.cpf, pessoa1.nome, pessoa1.telefone)

print(pessoa1.telefone.ddd, pessoa1.telefone.numero)

print(pessoa2)

pessoa1.print_endereco()
pessoa2.print_endereco()