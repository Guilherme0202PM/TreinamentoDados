
# ex03.py – Classe Participacao

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo              # identificador da participação
        self.data_inicio = data_inicio    # data de início (string)
        self.data_fim = data_fim          # data de fim (string)
        self.aluno = aluno                # objeto da classe Aluno
        self.projeto = projeto            # objeto da classe Projeto

    def __str__(self):
        return (
            f"Participacao(codigo={self.codigo}, "
            f"data_inicio={self.data_inicio}, "
            f"data_fim={self.data_fim}, "
            f"aluno={self.aluno}, "
            f"projeto={self.projeto})"
        )
