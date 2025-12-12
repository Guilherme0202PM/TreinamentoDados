"""Exercise 01"""

# ex01.py solicite ao usuário 3 números, armazene esses elementos em uma lista e apresente no final o menor e maior elemento

numbers = []
for i in range(3):
    number = float(input(f"Digite o número {i + 1}: "))
    numbers.append(number)

print(f"Os números digitados foram: {numbers}")
print(f"O maior número digitado foi: {max(numbers)}")
print(f"O menor número digitado foi: {min(numbers)}")