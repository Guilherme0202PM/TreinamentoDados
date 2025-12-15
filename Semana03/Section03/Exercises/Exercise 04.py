from Exersice01 import Aluno
from Exercise02 import Projeto
from Exercise03 import Participacao

class ProjetoParticipacao(Projeto):
    def __init__(self, codigo, titulo, responsavel):
        super().__init__(codigo, titulo, responsavel)
        self.participacoes = []  # Inicializa a lista de participações

    def add_participacao(self, participacao):
        if not isinstance(participacao, Participacao):
            raise ValueError("Participação deve ser uma instância da classe Participacao")
        self.participacoes.append(participacao)

# Testando a classe ProjetoParticipacao
projeto = ProjetoParticipacao.from_string("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
aluno = Aluno.from_string("SP0101,João da Silva,joao@email.com")
participacao = Participacao(1, "2023-01-01", "2023-12-31", aluno, projeto)
projeto.add_participacao(participacao)