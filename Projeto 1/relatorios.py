
def exibir_transacoes(transacoes):
    print("Relatorio de todas as Transacoes")
    for t in transacoes:
        print(t.id, t.tipo, t.categoria, t.data, t.valor)
    print()

"""
def exibir_saldo(transacoes):
    saldo = 0.0
    for t in transacoes:
        saldo += t.valor
    
    print(saldo)
"""

def exibir_saldo(transacoes):
    saldo = 0.0
    for t in transacoes:
        if t.tipo == "receita":
            saldo += t.valor
        else:
            saldo -= t.valor
    
    print("Saldo Atual: ",saldo)
    print()


def exibir_saldo_por_categoria(transacoes):
    saldos = {}

    for t in transacoes:
        if t.categoria not in saldos:
            saldos[t.categoria] = 0.0

        if t.tipo == "receita":
            saldos[t.categoria] += t.valor
        else:
            saldos[t.categoria] -= t.valor

    print("Saldo por Categoria:")
    for categoria, saldo in saldos.items():
        print(f"{categoria}: {saldo}")

    print()

def exibir_saldo_por_mes(transacoes):
    saldos = {}

    for t in transacoes:
        mes = t.data[:7]  # YYYY-MM

        if mes not in saldos:
            saldos[mes] = 0.0

        if t.tipo == "receita":
            saldos[mes] += t.valor
        else:
            saldos[mes] -= t.valor

    print("Saldo por Mês:")
    for mes, saldo in saldos.items():
        print(f"{mes}: {saldo}")

    print()
