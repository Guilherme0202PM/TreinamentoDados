"""Control Flow Tools: break, continue, and pass"""

# Essas instruções são usadas para alterar o fluxo de execução dos loops:
# 1. `break`: Encerra o loop imediatamente.
# 2. `continue`: Pula a iteração atual e continua para a próxima.
# 3. `pass`: Não faz nada – é usado como um placeholder.

# --- Exemplo 1: break ---
# Interrompe o loop quando uma condição específica é atendida


for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break  # Exit loop
    print("Value:", i)

# --- Exemplo 2: Encontrando a posição de um número em uma lista ---
# Procura um número e interrompe a busca assim que ele é encontrado

search = 5
numbers = [1, 5, 9, 7, 3, 3, 2, 1, 7]
position = -1  # Posição padrão caso o número não seja encontrado

counter = 0
for number in numbers:
    print("Checking position:", counter)
    if number == search:
        position = counter
        break  # Encerra o loop após encontrar o valor
    counter += 1

print("Found at position:", position)

# --- Exemplo 3: continue ---
# Pula valores específicos dentro do loop

print("Skipping number 3 in the list:")
for number in numbers:
    if number == 3:
        continue  # Skip 3
    print(number)

# --- Exemplo 4: pass ---
# Usado como um placeholder quando nenhuma ação é necessária (geralmente para código futuro)

print("Using pass as a placeholder:")
for i in range(5):
    if i == 2:
        pass  #Não faz nada por enquanto
    print("Current number:", i)