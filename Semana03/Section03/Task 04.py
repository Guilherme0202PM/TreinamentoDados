class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if altura <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        self._altura = altura

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        if base <= 0:
            raise ValueError("A base deve ser maior que zero.")
        self._base = base
    
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

retangulo1.altura = 10
retangulo1.base = 25 

print("Altura:", retangulo1.altura)
print("Base:", retangulo1.base)
print("Calcula Area retangulo1", retangulo1.calcular_area())
