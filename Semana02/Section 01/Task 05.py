"""Data Types"""

# Numeric data types: int, float, complex

age = 20
weight = 70.5

print(age, type(age))  # int
print(weight, type(weight))  # float

# String data type
name = 'Pedro'
surname = "Silva"
full_name = name + ' ' + surname
print(full_name)  # str

product = 'Coca-Cola'

print(f'The client {full_name} bought {product}.')

print(name[0], name[1], name[2], name[3])
print(name[0:2])
print(name[0], name[-1])  # First and last character

print(name.upper())  # Convert to uppercase
print(name.lower())  # Convert to lowercase

print(1, 3, 7, 10, sep='-', end='\n')  # Print with hyphen separator

# Boolean data type
is_adult = True
is_minor = False
print(is_adult, type(is_adult))  # bool
print(is_minor, type(is_minor))  # bool

result = 10 < 3
print(result, type(result))  # bool

# Tipo de dados lista
fruits = ['apple', 'banana', 'cherry']
print(fruits)
print(fruits[0])  # Acesse o primeiro elemento
print(fruits[1:3])  # Acessar elementos do índice 1 ao 2

fruits.append('orange')  # Adiciona um elemento ao final da lista
fruits.remove('banana')  # Remove um elemento da lista
print(fruits)
fruits[0] = 'kiwi'  # Modifica um elemento da lista
print(fruits)
print(len(fruits))  # Tamanho da lista

# Tuplas são listas imutáveis
codes = ('A001', 'B002', 'C003')
print(codes)
print(codes[0]) # Acessar o primeiro elemento
# codes[0] = 'D004' # Isso gerará um erro porque tuplas são imutáveis
print(len(codes)) # Comprimento da tupla

# Definir tipo de dados (coleções não ordenadas de elementos únicos)
draw_result = {50, 10, 60, 45}
print(draw_result)
print(50 in draw_result)  # Verificar se um elemento está no conjunto
draw_result.add(70)  # Adicionar um elemento
print(draw_result)
draw_result.remove(10)  # Remover um elemento
print(draw_result)

# Tipo de dados dicionário (pares chave-valor)
employee = {
    'code': 'E001',
    'name': 'Alice',
    'salary': 5000.0
}

print(employee)
print(employee['name'])  # Acessar valor pela chave
employee['salary'] = 5500.0  # Modificar valor pela chave
print(employee)
employee['department'] = 'HR'  # Adicionar um novo par chave-valor
print(employee)
employee.pop('code')  # Remover um par chave-valor
print(employee)

print(employee.keys())  # Obter todas as chaves
print(employee.values())  # Obter todos os valores