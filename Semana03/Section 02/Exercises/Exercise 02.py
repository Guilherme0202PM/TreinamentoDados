
def carregar_dados_projetos(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        projetos = []
        for linha in arquivo:
            codigo, titulo, responsavel = linha.strip().split(',')
            projeto = {
                'codigo': int(codigo),
                'titulo': titulo,
                'responsavel': responsavel
            }
            projetos.append(projeto)
        return tuple(projetos)


import os

nome_arquivo = "projetos.txt"

if not os.path.exists(nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(
            "1,Site Institucional,Ana Silva\n"
            "2,API de Pagamentos,Carlos Souza\n"
            "3,App Mobile,Mariana Lima\n"
        )

dados_projetos = carregar_dados_projetos(nome_arquivo)

for projeto in dados_projetos:
    print(projeto)
