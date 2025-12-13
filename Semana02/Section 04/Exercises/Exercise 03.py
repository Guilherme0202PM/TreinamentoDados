#Exercise 03

# Crie uma função que recebe uma tupla de números como parâmetro(numeros) e retorna a soma dos números

def somar_numeros(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


entrada = input("Digite os números separados por espaço: ")
valores_str = entrada.split(" ")

numeros = []

for valor in valores_str:
    numeros.append(float(valor))

numeros = tuple(numeros)

resultado = somar_numeros(numeros)
print("Soma dos números:", resultado)
