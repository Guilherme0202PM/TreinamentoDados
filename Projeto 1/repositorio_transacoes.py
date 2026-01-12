# repositorio_transacoes.py
import csv
from models import Transacao
import shutil
import os


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

def garantir_copia_csv(caminho_original: str, caminho_copia: str) -> None:
    """
    Cria uma cópia do arquivo CSV original caso ela ainda não exista.
    """
    if not os.path.exists(caminho_copia):
        shutil.copy(caminho_original, caminho_copia)

def _proximo_id(caminho_csv: str) -> int:
    """
    Calcula o próximo ID com base no maior ID existente no CSV.
    Se estiver vazio (sem linhas), começa em 1.
    """
    transacoes = carregar_transacoes(caminho_csv)
    if not transacoes:
        return 1
    maior_id = max(t.id for t in transacoes)
    return maior_id + 1

def registrar_transacao(caminho_copia: str, transacao: Transacao) -> Transacao:
    """
    Registra uma transação no CSV da cópia, atribuindo ID automático.
    Retorna a transação já com o ID preenchido.
    """
    transacao.id = _proximo_id(caminho_copia)

    with open(caminho_copia, "a", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([
            transacao.id,
            transacao.tipo,
            transacao.categoria,
            transacao.descricao,
            transacao.data,
            transacao.valor
        ])

    return transacao