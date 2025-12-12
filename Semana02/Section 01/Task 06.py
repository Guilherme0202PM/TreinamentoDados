"""Conversão de Tipos"""
# Conversão implícita e explícita de tipos em Python

# Conversão implícita (automática)
num1 = 10  # (int)
num2 = 3.5  # (float)
result = num1 + num2  # int + float -> float
print(result, type(result))  # Saída: 13.5 <class 'float'>

# Conversão explícita (manual)
num3 = 20  # (int)
num4 = 4.0  # (float)
result2 = num3 + int(num4)  # int + int -> int
print(result2, type(result2))  # Saída: 24 <class 'int'>

# Conversão de string (type casting)
# sum = '15' + 10  # Isso geraria um erro porque '15' é uma string
sum = float('15.3') + 10  # Converte a string para float antes de somar
print(sum, type(sum))  # Saída: 25.3 <class 'float'>

num_str = '12'
num_int = int(num_str)  # Converte string para inteiro
print(num_int, type(num_int))  # Saída: 12 <class 'int'>

# Convertendo um número para string
name = 'Guilherme'
height = 1.93

# message = name + ' is ' + str(height) + ' meters tall.'
# Usando f-string para melhor legibilidade
message = f'{name} is {height} meters tall.'
print(message)  # Saída: Guilherme is 1.93 meters tall.
