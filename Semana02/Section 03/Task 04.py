"""Dicionários"""

# Dicionários são um tipo de dado embutido em Python que armazenam dados
# no formato chave-valor.

# Características dos dicionários:
# - Não ordenados: não possuem ordem fixa (até o Python 3.6; a partir daí,
#   a ordem de inserção é preservada)
# - Mutáveis: podem ser alterados após a criação
# - Iteráveis: podem ser usados em loops
# - As chaves devem ser únicas e imutáveis (por exemplo, strings, números, tuplas)
# - Os valores podem ser de qualquer tipo de dado e podem se repetir

# Criando um dicionário
car = {
    'brand': 'Ford',
    'model': 'Ka',
    'year': 2017
}

print("Car dictionary:", car)
print("Type:", type(car))

# Acessando valores usando chaves
print("Brand:", car['brand'])         # Acesso direto
print("Model (with get):", car.get('model'))  # Acesso seguro

# Obtendo chaves, valores e pares chave-valor
print("Keys:", car.keys())
print("Values:", car.values())
print("Key-value pairs:", car.items())

# Verificando se uma chave existe
print("'color' in car?", 'color' in car)

# Adicionando um novo par chave-valor
car['color'] = 'Red'
print("After adding 'color':", car)

# Removendo um par chave-valor usando pop
removed_brand = car.pop('brand')
print("Removed brand:", removed_brand)
print("After removing 'brand':", car)

print("---- Iterando sobre o dicionário ----")
# Iterando sobre as chaves
for key in car:
    print("Key:", key)

# Iterando sobre os valores
for value in car.values():
    print("Value:", value)

# Iterando sobre os pares chave-valor
for key, value in car.items():
    print(f"{key}: {value}")

# -----------------------------
# Trabalhando com uma lista de dicionários

student1 = {
    'name': 'Maria',
    'age': 20,
    'major': 'statistics'
}

student2 = {
    'name': 'João',
    'age': 22,
    'major': 'Computer Science'
}

# Adicionando novos pares chave-valor (notas)
student1['grades'] = [10.0, 9.5, 8.0]
student2['grades'] = [7.5, 8.0, 9.0]

# Lista de dicionários
students = [student1, student2]

print("---- Students ----")
for student in students:
    print(f"Name: {student['name']}, Major: {student['major']}")
    for grade in student['grades']:
        print(f"  Grade: {grade}")
