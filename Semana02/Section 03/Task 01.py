""" Lists """

# Listas são um dos tipos de dados mais utilizados em Python.
# Uma lista é uma coleção que é:
# - Ordenada (os elementos possuem um índice definido)
# - Mutável (pode ser alterada)
# - Iterável (pode ser usada em loops)
# - Permite valores duplicados
# - Pode armazenar elementos de diferentes tipos de dados
# - Pode conter listas aninhadas (listas dentro de listas)
# - De tamanho dinâmico (pode crescer ou diminuir)

# Creating a list
names = ['Maria', 'Pedro', 'João','Marcelo']
print("Original list:", names)
print("Type:", type(names))

# Accessing elements by index
print("Primeiro nome:", names[0])                 # Maria
print("Primeiros dois nomes:", names[0:2])        # Maria, Pedro
print("Primeiros dois nomes (forma simplificada):", names[:2])  # Maria, Pedro
print("Do segundo nome em diante:", names[1:])    # Pedro, João


# Modifying elements
names[0] = 'Maria da Silva'
names[1:] = ['Pedro da Silva', 'João Santos']
print("Modified list:", names)

# Getting the length of the list
size = len(names)
print("List size:", size)

# Adding elements to the list

# .append() - adiciona um elemento ao final da lista
names.append('Maria Lucia')
print("After append:", names)

# .insert(index, element) - insere um elemento em uma posição específica
names.insert(0, 'Guilherme Mundim')  # insert at the beginning
print("After insert at position 0:", names)

names.insert(2, 'Ana Carolins')          # insert at position 2
print("After insert at position 2:", names)

# .extend() - adiciona múltiplos elementos de outra lista
more_names = ['Kaio Silva', 'Carlos Gomes']
print("List size before extend:", len(names))
names.extend(more_names)
print("List size after extend:", len(names))
print("After extend:", names)

# Removing elements from the list

# .remove(value) - remove a primeira ocorrência do valor
names.remove('Maria da Silva')
print("After remove:", names)

# del keyword - remove pelo índice
del names[0]
print("After del [0]:", names)

# del também pode ser usado para remover a lista inteira da memória
# del names

# .clear() - remove todos os elementos da lista
# names.clear()
print("After clear (commented out):", names)

# Percorrendo uma lista
print("Iterating with for-in:")
for name in names:
    print(name)

print("Iterating with index:")
for i in range(len(names)):
    print(f"Position {i}: {names[i]}")