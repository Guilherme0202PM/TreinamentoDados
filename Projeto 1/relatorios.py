
def exibir_transacoes(transacoes):
    for t in transacoes:
        print(t.id, t.tipo, t.categoria, t.data, t.valor)
        
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
    
    print(saldo)