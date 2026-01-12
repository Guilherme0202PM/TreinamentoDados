# repositorio_transacoes.py
import csv
from models import Transacao

def carregar_transacoes(caminho_csv: str) -> list[Transacao]:
    transacoes: list[Transacao] = []

    with open(caminho_csv, "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)  # lê usando o cabeçalho
        for linha in leitor:
            t = Transacao(
                id=int(linha["id"]),
                tipo=linha["tipo"].strip(),
                categoria=linha["categoria"].strip(),
                descricao=linha["descricao"].strip(),
                data=linha["data"].strip(),          # ISO: YYYY-MM-DD
                valor=float(linha["valor"])
            )
            transacoes.append(t)

    return transacoes
