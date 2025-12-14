# === Aula 03 - Métodos de classe e instância ===

# Nesta lição, exploramos a diferença entre métodos de instância e métodos de classe.
# - Métodos de instância operam sobre uma instância da classe (usando 'self').
# - Métodos de classe operam sobre a própria classe (usando 'cls') e são frequentemente usados
#   para criar instâncias de formas alternativas.

# Resumo:
# Métodos de classe como 'build_from_list' e 'from_string' nos permitem criar objetos Rectangle
# a partir de diferentes formatos de dados. Essa é uma forma limpa e reutilizável de lidar com a
# criação de objetos, especialmente quando os dados vêm de fontes externas como arquivos ou
# entrada do usuário.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    @classmethod
    def criar_lista(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def Construtor_lista(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def a_partir_da_string(cls, texto):
        largura, altura = map(float, texto.split(","))
        return cls(largura, altura)

    
retangulo1 = Retangulo(5, 10)
retangulo2 = Retangulo(3, 6)
retangulo3 = Retangulo.criar_lista([10, 15])
retangulo4 = Retangulo.Construtor_lista([10, 15])
retangulo5 = Retangulo.a_partir_da_string("8.5, 12.9")



print("Calcula Area retangulo1", retangulo1.calcular_area())
print("Calcula Area retangulo2", retangulo2.calcular_area())

print("Calcula Area retangulo3", retangulo3.base, retangulo3.altura, retangulo3.calcular_area())

print("Calcula Area retangulo4", retangulo4.base, retangulo4.altura, retangulo4.calcular_area())

print(f"Calcula Area retangulo5: {retangulo5.calcular_area()}")
