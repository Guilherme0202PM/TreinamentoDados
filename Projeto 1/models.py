class Transacao:
    def __init__(self, id, tipo, categoria, descricao, data, valor):
        self.id = id
        self.data = data
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria
        self.tipo = tipo