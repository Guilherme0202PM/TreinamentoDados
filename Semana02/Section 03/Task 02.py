"""Tuplas"""

# Tuplas são coleções muito semelhantes às listas, porém são imutáveis.
# Isso significa que, uma vez criada, a tupla não pode ser modificada.
# Características:
# - Ordenadas (os elementos possuem um índice definido)
# - Imutáveis (não podem ser alteradas)
# - Iteráveis (podem ser usadas em loops)
# - Permitem valores duplicados
# - Podem conter diferentes tipos de dados
# - Podem conter tuplas aninhadas (tuplas dentro de tuplas)

# Criando uma tupla
names = ('Maria', 'Pedro', 'João')
print("Original tuple:", names)
print("Type:", type(names))

# Acessando elementos pelo índice
print("First name:", names[0])            # Maria
print("First two names:", names[0:2])     # Maria, Pedro
print("First two names (shortcut):", names[:2])  # Maria, Pedro
print("From second name onward:", names[1:])     # Pedro, João

# Obtendo o tamanho da tupla
size = len(names)
print("Tuple size:", size)

# Tuplas são imutáveis: os elementos não podem ser adicionados, removidos ou modificados.
# names[0] = 'Maria da Silva'  # ❌ Isso gerará um erro do tipo TypeError

# Percorrendo uma tupla usando for-in
print("Iterating with for-in:")
for name in names:
    print("Name:", name)

# Percorrendo uma tupla usando índice
print("Iterating with index:")
for i in range(len(names)):
    print(f"Index {i}:", names[i])

# Criando outra tupla (os parênteses são opcionais na criação)
names2 = 'Ana', 'Lucia', 'Marcos'
print("Another tuple:", names2)
print("Type:", type(names2))

# Desempacotamento de tupla (tuple unpacking)
# Isso significa atribuir cada elemento da tupla a uma variável
name1, name2, name3 = names2
print("Unpacked names:", name1, name2, name3)

# Concatenação de tuplas
all_names = names + names2
print("Concatenated tuple:", all_names)
print("Type of result:", type(all_names))
