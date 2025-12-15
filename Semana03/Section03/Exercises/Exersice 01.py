"""Exercise 01"""

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def a_partir_de_string(cls, texto):
        partes = [i.strip() for i in texto.split(',')]
        if len(partes) != 3:
            raise ValueError(
                "A string deve conter exatamente três partes: prontuario, nome, email"
            )
        return cls(partes[0], partes[1], partes[2])

    def __eq__(self, outro):
        if not isinstance(outro, Aluno):
            return NotImplemented
        return self.prontuario == outro.prontuario

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if not valor:
            raise ValueError("Prontuário não pode ser vazio.")
        self._prontuario = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio.")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor:
            raise ValueError("Email não pode ser vazio.")
        self._email = valor

aluno = Aluno.a_partir_de_string("SP0101,João da Silva,joao@email.com")
aluno2 = Aluno.a_partir_de_string("SP0102,Maria da Silva,maria@email.com")
aluno3= Aluno("SP0103", "Paulo da Silva", "Paulo@email.com")

print(f"Aluno 1 == Aluno 2: {aluno == aluno2}")  
print(f"Aluno 1 == Aluno 3: {aluno == aluno3}")     
print(f"Prontuário: {aluno.prontuario}, Nome: {aluno.nome}, Email: {aluno.email}")
print(f"Prontuário: {aluno2.prontuario}, Nome: {aluno2.nome}, Email: {aluno2.email}")
print(f"Prontuário: {aluno3.prontuario}, Nome: {aluno3.nome}, Email: {aluno3.email}")