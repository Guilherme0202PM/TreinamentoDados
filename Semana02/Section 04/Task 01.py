""" Aula 01 - Introdução a Funções """

# Funções são blocos de código que executam tarefas específicas.

# Benefícios:
# - Evitam repetição
# - Tornam o código modular
# - Melhoram a legibilidade
# - Facilitam a manutenção

# ------------------------------------------
# 1. Funções Embutidas (Built-in Functions)
# ------------------------------------------

# São funções que já estão disponíveis em Python

print("Olá", 123, True)  # Exibe na tela

names = ['Alice', 'Bob', 'Carlos']
# Retorna o tamanho da lista
length = len(names)
print("Nomes:", names, "Tamanho:", length)

# ------------------------------------------
# 2. Funções Definidas pelo Usuário
# ------------------------------------------

# Podemos definir nossas próprias funções para resolver partes de um problema.

# Exemplo 1 - Sem parâmetros e sem retorno

def Saudacoes():
    print("Hello! Welcome to our system.")

Saudacoes()


# Exemplo 2 - Com parâmetro, sem retorno

def saudacoesUsuario(name):
    print(f"Hello, {name}! Nice to see you.")

saudacoesUsuario("João")
user = "Marina"
saudacoesUsuario(user)

# Exemplo 3 - Com parâmetros e valor de retorno

def calculate_average(n1, n2, n3):
    avg = (n1 + n2 + n3) / 3
    return avg

# Chamando com valores literais
average = calculate_average(7.5, 8.0, 9.0)
print("Average:", average)

# Chamando com variáveis
a = 6.0
b = 5.0
c = 8.0
avg2 = calculate_average(a, b, c)
print("Average 2:", avg2)

