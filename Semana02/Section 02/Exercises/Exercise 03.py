"""Exercise 03"""

# O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X. Exemplos válidos: BR0001X BR1236X BR9999X
# Exemplos inválidos: br0001X BR126X BR99999X BR9999Y
# Crie um programa em python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.

identificador = input("Digite o identificador do funcionário (ex: BR0001X): ").strip()

tamanho_correto = len(identificador) == 7
prefixo_BR = identificador.startswith("BR")
sufixo_X = identificador.endswith("X")
eh_numero = identificador[2:6].isdigit()
numero_valido = eh_numero and 1 <= int(identificador[2:6]) <= 9999

if tamanho_correto and prefixo_BR and sufixo_X and numero_valido:
    print("Identificador válido")
else:
    print("Identificador inválido")
