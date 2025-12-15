"""Lição 05 - POO: Métodos Especiais"""

# Nesta lição, vamos explorar métodos especiais em classes Python.
# Métodos especiais (também conhecidos como "métodos mágicos" ou "métodos dunder",
# abreviação de "double underscore" — duplo sublinhado)
# permitem definir como objetos de uma classe interagem com funções e operadores embutidos.

# Dois métodos especiais comuns:
# - __str__(self): Define a representação em string "informal" ou amigável para o usuário.
#   É chamado por funções como print() ou str().
#
# - __repr__(self): Define a representação em string "oficial" ou voltada para desenvolvedores.
#   Deve retornar uma string que idealmente consiga recriar o objeto usando eval().
#   É usado em depuração, logs e interpretadores interativos como Jupyter ou o REPL do Python.

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

        def calcular_area(self):
            return self.base * self.altura  
        
        def calcular_perimetro(self):
            return 2 * (self.base + self.altura)
        
        # __str__ retorna uma descrição amigável para o usuário
        def __str__(self):
            return f"Retangulo:{self.base} cm x {self.altura}"
        
        # __repr__ retorna uma string que pode recriar o objeto
        def __repr__(self):
            return f"Retangulo({self.base}, {self.altura})"
        
# Criando uma instância de Rectangle
Retangulo1 = Retangulo(5, 10)

# Exemplo: usando __str__ com print()
print(Retangulo1) # Saída: Rectangle: 5 cm x 10 cm

# Exemplo: __repr__ sendo usado explicitamente
print(repr(Retangulo1))# Saída: Rectangle(5, 10)

# Usando eval(repr(obj)) para recriar um objeto
Retangulo2 = eval(repr(Retangulo1))
print("Retangulo2 area:", Retangulo2.calcular_area())

# Confirmando que o objeto recriado é uma nova instância
# False (são instâncias diferentes)
print("Mesmo objeto?", Retangulo1 is Retangulo2)

# Usando o operador walrus (expressão de atribuição)
print(rect3 := Retangulo(10, 20))# Usa __str__