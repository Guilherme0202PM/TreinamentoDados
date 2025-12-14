#Ex1.py - Carregar dados de alunos. Implemente a função:

#def carregar_dados_alunos(nome_arquivo):
    #"""Retorna uma tupla de dicionários com dados de alunos."""

     #A função deve:
    # - Receber como parâmetro o nome de um arquivo que contém dados de alunos.
    # - Ler o arquivo linha a linha.
    # - Para cada linha, criar um dicionário com as chaves:
    #   - prontuario
    #   - nome
    #   - email
    
    # Retornar uma tupla, onde cada elemento é um dicionário com os dados de um aluno.

    # Exemplo de arquivo de dados (texto):

    # SP000001,Maria da Silva,maria@gmail.com

    # SP000002,Pedro Gomes,pedro@gmail.com

    # SP000003,João Santos,joao@gmail.com   

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