import os
from repositorio_transacoes import carregar_transacoes, garantir_copia_csv
from relatorios import exibir_transacoes


BASE_DIR = os.path.dirname(__file__)
caminho = os.path.join(BASE_DIR, "data", "transacoes_projeto1lipai.csv")
caminho_copia = os.path.join(BASE_DIR, "data", "transacoes_projeto1lipai_copia.csv")

garantir_copia_csv(caminho, caminho_copia)

transacoes = carregar_transacoes(caminho_copia)

exibir_transacoes(transacoes)

