#Exercício 1
def carregar_dados_alunos(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        for linha in arquivo:
            prontuario, nome, email = linha.strip().split(',')
            aluno = {
                'prontuario': prontuario,
                'nome': nome,
                'email': email
            }
            alunos.append(aluno)
        return tuple(alunos)

#
import os

nome_arquivo = 'alunos.txt'

if not os.path.exists(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(
            "SP000001,Maria da Silva,maria@gmail.com\n"
            "SP000002,Pedro Gomes,pedro@gmail.com\n"
            "SP000003,João Santos,joao@gmail.com\n"
        )
#

dados_alunos = carregar_dados_alunos(nome_arquivo)

# Exibindo os dados carregados
for aluno in dados_alunos:
    print(aluno)