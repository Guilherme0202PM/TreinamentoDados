import os
from models import Transacao
from repositorio_transacoes import carregar_transacoes, garantir_copia_csv, registrar_transacao
from relatorios import exibir_transacoes, exibir_saldo


BASE_DIR = os.path.dirname(__file__)
caminho = os.path.join(BASE_DIR, "data", "transacoes_projeto1lipai.csv")
caminho_copia = os.path.join(BASE_DIR, "data", "transacoes_projeto1lipai_copia.csv")

garantir_copia_csv(caminho, caminho_copia)

transacoes = carregar_transacoes(caminho_copia)

exibir_transacoes(transacoes)
exibir_saldo(transacoes)

print("tipo Receita(1) ou Despesa(2)")
op = input("Escolha: ").strip()

tipo = "receita" if op == "1" else "despesa"

categoria = input("Categoria: ").strip()
descricao = input("Descrição: ").strip()
data = input("Data (YYYY-MM-DD): ").strip()
valor = float(input("Valor: ").replace(",", ".").strip())

nova = Transacao(0, tipo, categoria, descricao, data, valor)

nova = registrar_transacao(caminho_copia, nova)
print(f"Transação salva com ID {nova.id}.")