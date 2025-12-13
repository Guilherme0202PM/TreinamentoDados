"""Aula 02 - Argumentos de Funções: Posicionais, Nomeados, Padrão e Desempacotamento"""

# Uma função é um bloco de código que executa uma tarefa específica.
# Argumentos são as entradas que passamos para uma função para controlar seu comportamento.

# ---------------------------------------------
# 1. Argumentos Posicionais
# Argumentos passados de acordo com a ordem


def add(a, b):
    return a + b


def divide(dividend, divisor):
    return dividend / divisor


print("Positional arguments:")
print("add(10.0, 3.5) =", add(10.0, 3.5))
print("add(2.0, 6.5) =", add(2.0, 6.5))
print("divide(10.0, 2.0) =", divide(10.0, 2.0))

# ---------------------------------------------
# 2. Argumentos Nomeados (Keyword Arguments)
# Argumentos passados usando o nome do parâmetro
print("\nKeyword arguments:")
print("add(a=3.0, b=6.2) =", add(a=3.0, b=6.2))
print("add(b=5.0, a=7.8) =", add(b=5.0, a=7.8))
print("divide(divisor=3.0, dividend=10.0) =",
      divide(divisor=3.0, dividend=10.0))

# ---------------------------------------------
# 3. Argumentos Padrão
# Se não forem fornecidos, o valor padrão é utilizado


def saudacao(name, saudacao="Hello"):
    return f"{saudacao}, {name}!"


print("\nDefault arguments:")
print(saudacao("João", "Hi"))
print(saudacao("Maria", "Good morning"))
print(saudacao("Pedro"))  # Usa a saudação padrão
print(saudacao(saudacao="Hey", name="Carla"))  # A ordem não importa com argumentos nomeados
print(saudacao(name="Lucas"))  # Apenas o nome foi fornecido
