# === Aula 01 - Introdução a Orientação a objetos ===

# paradigma de programação

# calcular a área e o perimetro de um retangulo
# area = base * altura
# perimetro = 2 * (base + altura)
# Estrutura parar armazenar os valores necessários para os calculos

retangulo1 = {
    'base': 10.0,
    'altura': 5.0
}

retangulo2 = {
    'base': 6.0,
    'altura': 3.0
}

# Realizar os cálculos
def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']

def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])

print("Sem POO:")
print(f"Área do retângulo 1: {calcular_area(retangulo1)}")
print(f"Perímetro do retângulo 1: {calcular_perimetro(retangulo1)}")
print(f"Área do retângulo 2: {calcular_area(retangulo2)}")
print(f"Perímetro do retângulo 2: {calcular_perimetro(retangulo1)}")
print("------------------------------------------------")


# -----------------------------------------------
# Parte 2 - Com POO (usando classes e objetos)

# Define uma classe chamada Retângulo
# A classe tem os atributos: largura e altura
# A classe tem os métodos: calcular_area e calcular_perimetro
# (Funções que operam sobre os dados do objeto)
# Isso nos permite encapsular os dados e o comportamento
# relacionados aos retângulos em uma única entidade.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
# Cria instâncias (objetos) da classe Retângulo
retangulo3 = Retangulo(5, 10)
retangulo4 = Retangulo(3, 6)

print("Com POO:")
print(f"Área do retângulo 3: {retangulo3.calcular_area()}")
print(f"Perímetro do retângulo 3: {retangulo3.calcular_perimetro()}")
print(f"Área do retângulo 4: {retangulo4.calcular_area()}")
print(f"Perímetro do retângulo 4: {retangulo4.calcular_perimetro()}")
