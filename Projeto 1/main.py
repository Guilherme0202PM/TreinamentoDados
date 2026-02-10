import os
from models import Transacao
from repositorio_transacoes import carregar_transacoes, garantir_copia_csv, registrar_transacao
from relatorios import exibir_transacoes, exibir_saldo

def cadastrar_transacao_cli(caminho_copia):
    print("tipo Receita(1) ou Despesa(2)")
    op = input("Escolha: ").strip()
    tipo = "receita" if op == "1" else "despesa"

    categoria = input("Categoria: ").strip()
    descricao = input("Descrição: ").strip()
    #data = input("Data (YYYY-MM-DD): ").strip()
    data = ler_data_padronizada()
    valor = float(input("Valor: ").replace(",", ".").strip())

    nova = Transacao(0, tipo, categoria, descricao, data, valor)
    nova = registrar_transacao(caminho_copia, nova)

    print(f"Transação salva com ID {nova.id}.")

def ler_data_padronizada():
    while True:
        entrada = input("Data (YYYYMMDD ou qualquer variação): ").strip()

        # Remove tudo que não for número
        somente_numeros = ""
        for c in entrada:
            if c.isdigit():
                somente_numeros += c

        # Verifica se tem exatamente 8 dígitos
        if len(somente_numeros) != 8:
            print("Erro: a data deve conter exatamente 8 números.")
            continue

        # Formata para YYYY-MM-DD
        ano = somente_numeros[:4]
        mes = somente_numeros[4:6]
        dia = somente_numeros[6:8]

        data_formatada = f"{ano}-{mes}-{dia}"
        return data_formatada






BASE_DIR = os.path.dirname(__file__)
caminho = os.path.join(BASE_DIR, "data", "transacoes_projeto1lipai.csv")
caminho_copia = os.path.join(BASE_DIR, "data", "transacoes_projeto1lipai_copia.csv")

garantir_copia_csv(caminho, caminho_copia)

transacoes = carregar_transacoes(caminho_copia)

# ===== MENU (switch-like) =====
while True:
    print("\n=== MENU ===")
    print("0 - Não quero fazer nada")
    print("1 - Listar transações")
    print("2 - Mostrar saldo")
    print("3 - Cadastrar transação")
    print("4 - Recarregar transações do CSV")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "0":
            # Não faz nada (só volta pro menu)
            pass

        case "1":
            exibir_transacoes(transacoes)

        case "2":
            exibir_saldo(transacoes)

        case "3":
            cadastrar_transacao_cli(caminho_copia)
            # Atualiza a lista em memória após cadastrar
            transacoes = carregar_transacoes(caminho_copia)

        case "4":
            transacoes = carregar_transacoes(caminho_copia)
            print("Transaç1ões recarregadas do arquivo.")

        case "9":
            print("Saindo...")
            break

        case _:
            print("Opção inválida. Tente novamente.")

