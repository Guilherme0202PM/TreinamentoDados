from models import Transacao

def aumentar_valor(transacao: Transacao, incremento: float) -> None:
    transacao.valor += incremento

t = Transacao(1, "receita", "salário", "pagamento", "2026-01-12", 1000.0)
aumentar_valor(t, 12)
print(t.valor)  # 1010.0
