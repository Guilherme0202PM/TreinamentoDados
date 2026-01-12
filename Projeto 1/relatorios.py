
def exibir_transacoes(transacoes):
    for t in transacoes:
        print(t.id, t.tipo, t.categoria, t.data, t.valor)
