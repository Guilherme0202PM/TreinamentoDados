"""Exercise 01"""

# Solicite ao usuário 3 notas e calcule a média aritmética (sem usar sum())

notas = []
total = 0  

print("Digite três notas para calcular a média aritmética:")

while len(notas) < 3:
    nota = float(input(f"Nota {len(notas) + 1}: "))
    if nota >= 0:
        notas.append(nota)
        total += nota  
    else:
        print("A nota deve ser maior ou igual a 0. Tente novamente.")

average = total / len(notas)

print(f"A média aritmética das notas {notas} é: {average:.2f}")

