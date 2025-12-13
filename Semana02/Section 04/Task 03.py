"""Aula 03 - *args e **kwargs: Argumentos Avançados de Funções"""

# Nesta aula, vamos explorar argumentos avançados em funções Python:
# - *args: permite receber um número variável de argumentos posicionais (armazenados como uma tupla)
# - **kwargs: permite receber um número variável de argumentos nomeados (armazenados como um dicionário)

# ---------------------------------------------
# 1. *args (Argumentos Posicionais Variáveis)

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print("1. Usando *args (argumentos posicionais):")
print("sum_numbers(1, 2, 3) =", sum_numbers(1, 2, 3))
print("sum_numbers(4, 5, 6, 7) =", sum_numbers(4, 5, 6, 7))

def world_cup_titles(country, *args):
    print(f"{country} has won the World Cup {len(args)} times:")
    for year in args:
        print(f" - Year: {year}")

print("\nWorld Cup Titles:")
world_cup_titles("Brazil", 1958, 1962, 1970, 1994, 2002)

# ---------------------------------------------
# 2. **kwargs (Argumentos Nomeados Variáveis)

def imprimir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

print("\n2. Usando **kwargs (argumentos nomeados):")
imprimir_info(nome="Gui", idade=23, cidade="Uberlândia")


def calcular_preco(valor, **kwargs):
    percentual_imposto = kwargs.get('tax_percentage', 0)
    desconto = kwargs.get('discount', 0)
    preco_final = valor + (valor * percentual_imposto / 100) - desconto
    return preco_final


print("\nCalculando o preço final com **kwargs:")
print("Preço com imposto de 10% e desconto de 5:",
      calcular_preco(100, tax_percentage=10, discount=5))

# ---------------------------------------------
# 3. Usando *args e **kwargs Juntos

def mostrar_tudo(*argumentos, **kwargs):
    print("Argumentos posicionais (*args):", argumentos)
    print("Argumentos nomeados (**kwargs):", kwargs)

print("\n3. Combinando *args e **kwargs:")
mostrar_tudo(1, 2, 3, nome="Marcos", idade=34)


