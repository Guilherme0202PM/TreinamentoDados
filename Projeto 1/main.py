import os

BASE_DIR = os.path.dirname(__file__)
caminho = os.path.join(BASE_DIR, "data", "transacoes_projeto1lipai.csv")

with open(caminho, "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
