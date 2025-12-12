"""Entrada e Saída (I/O)"""
# Entrada e saída em Python
import os

# Saída padrão - sys.stdout
print('Hello, world!')  # Saída no console
# Saída no console com caractere de final personalizado
print('Hello, world', end='!!!!!\n')
# Saída no console com separador personalizado
print('Hello', 'world', sep=' - ', end='!!\n')

# Entrada do usuário
name = input('Digite seu nome: ')  # Obtém entrada do usuário
age = input('Digite sua idade: ')  # Obtém entrada do usuário
print(f'Hello {name}, you are {age} years old.')  # Exibe saída formatada
print(type(name), type(age))  # Mostra os tipos das variáveis

# Observação: input() retorna uma string. Converta para int se operações numéricas forem necessárias.
# Exemplo de conversão da entrada para inteiro
age = int(input('Digite sua idade (novamente): '))  # Obtém entrada e converte para int
print(f'Hello {name}, you are {age} years old.')  # Exibe a saída
print(type(name), type(age))  # Confirma os tipos

# Saída condicional
if age >= 18:
    print(f'{name}, you are an adult.')
else:
    print(f'{name}, you are a minor.')