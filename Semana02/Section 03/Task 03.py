"""Conjuntos (Sets)"""

# Sets são um tipo de dado embutido em Python que representam
# uma coleção não ordenada de elementos únicos.

# Características dos sets:
# - Não ordenados: não possuem índice ou posição definida
# - Mutáveis: é possível adicionar ou remover elementos
# - Iteráveis: podem ser usados em loops (por exemplo, for)
# - Não permitem valores duplicados
# - Podem armazenar elementos de diferentes tipos de dados

# Criando um set
games = {'Pokemon', 'Hollow Knight', 'Cuphead'}
print("Set original de jogos:", games)
print("Tipo:", type(games))

# Valores duplicados são automaticamente removidos
numbers = {1, 5, 7, 4, 3, 3, 1}
print("Set sem duplicatas:", numbers)

# Percorrendo um set
print("Iterando sobre 'numbers':")
for num in numbers:
    print(num)

# Teste de pertencimento
print("O número 2 está em 'numbers'?", 2 in numbers)  # False
print("O número 1 está em 'numbers'?", 1 in numbers)  # True

# Adicionando elementos a um set
print("Jogos antes do add:", games)
games.add('Undertale')
print("Jogos após adicionar 'Undertale':", games)

# Adicionando um novo número ao set 'numbers'
numbers.add(8)
print("Numbers após adicionar 8:", numbers)

# Combinando sets com update()
other_numbers = {3, 4, 9, 11, 1, 5}
print("Outros números:", other_numbers)

numbers.update(other_numbers)
print("Numbers após update com other_numbers:", numbers)

# Removendo elementos
# Remove 'Pokemon' do set
games.remove('Pokemon')
print("Jogos após remover 'Pokemon':", games)

# Remover um item inexistente usando `discard()` evita erros
games.discard('Zelda')  # Seguro: não faz nada se 'Zelda' não estiver no set
print("Jogos após tentar descartar 'Zelda':", games)

# Removendo todos os elementos
# games.clear()
# print("Jogos após clear:", games)