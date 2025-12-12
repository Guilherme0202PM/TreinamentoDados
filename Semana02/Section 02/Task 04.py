""" While Loops """

# A while loop runs a block of code as long as the condition remains True.
# Used when the number of repetitions is not known in advance.

# Example: Ask the user for a positive number
# The loop continues until the user enters a valid value
number = -1

while number <= 0:
    number = int(input("Enter a positive number: "))

print("Valid number entered:", number)

# Example: # Increment count by 1
count = 0
while count < 10:
    print(count)
    count += 1  

# Example: Decrement count by 1
count = 10
while count >= 0:
    print(count)
    count -= 1

# Exemplo: Leitura de um arquivo linha por linha usando um loop while
# Isso é útil ao trabalhar com arquivos grandes

# with open('example.txt', 'r') as file:
#     line = file.readline()   # Lê a primeira linha
#     while line:              # Continua enquanto houver linhas para ler
#         print(line.strip())  # Imprime a linha sem espaços em branco extras
#         line = file.readline()  # Lê a próxima linha
