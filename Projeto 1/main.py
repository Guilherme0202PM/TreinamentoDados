import os
from repositorio_transacoes import carregar_transacoes

BASE_DIR = os.path.dirname(__file__)
caminho = os.path.join(BASE_DIR, "data", "transacoes_projeto1lipai.csv")

transacoes = carregar_transacoes(caminho)

for t in transacoes:
    print(t.id, t.tipo, t.categoria, t.data, t.valor)
