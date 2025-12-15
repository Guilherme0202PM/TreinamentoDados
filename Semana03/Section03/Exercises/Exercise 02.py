"""Exercise 02"""

class Projeto:

    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @classmethod
    def from_string(cls, string):
        codigo, titulo, responsavel = string.split(',')
        return cls(codigo, titulo, responsavel)

    def __eq__(self, outro):
        if not isinstance(outro, Projeto):
            return NotImplemented
        return self.codigo == outro.codigo

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = int(value)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError("Título não pode ser vazio")
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError("Responsável não pode ser vazio")
        self._responsavel = value


projeto1 = Projeto.from_string(
    "1,Laboratório de Desenvolvimento de Software,Pedro Gomes"
)
projeto2 = Projeto.from_string(
    "1,Laboratório de Desenvolvimento de Software,Pedro Gomes"
)
projeto3 = Projeto.from_string(
    "2,Projeto de Pesquisa,João Silva"
)

print(f"Projeto 1 == Projeto 2: {projeto1 == projeto2}")
print(f"Projeto 1 == Projeto 3: {projeto1 == projeto3}")

print(f"Projeto 1: {projeto1.codigo}, {projeto1.titulo}, {projeto1.responsavel}")
print(f"Projeto 2: {projeto2.codigo}, {projeto2.titulo}, {projeto2.responsavel}")
print(f"Projeto 3: {projeto3.codigo}, {projeto3.titulo}, {projeto3.responsavel}")