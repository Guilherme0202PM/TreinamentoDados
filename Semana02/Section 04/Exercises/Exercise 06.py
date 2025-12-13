#Exercise 06

# - Crie um programa em python que recebe como entrada o comprimento, altura e a largura(cm) de um aquário e calcule as seguintes informações.
# - O volume do aquário em litros
# - A potência do termostato necessária para manter a temperatura adequada dentro do aquário
# - A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
# - Neste exercício você deve definir a estrutura de dados que represente as entradas do usuário e também as funções que resolvam os diferentes cálculos e apresentar os resultados finais para o usuário.


# Função para calcular o volume do aquário em litros
# Função para calcular o volume do aquário (em litros)
def calcular_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000  # Volume em litros


# Função para calcular a potência do termostato
def calcular_potencia(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)  # Fórmula da potência


# Função para calcular a filtragem por hora
def calcular_filtragem(volume):
    return volume * 2, volume * 3  # Faixa de filtragem (2x a 3x o volume)


# Estrutura de dados para armazenar os dados do aquário
aquario = {
    'comprimento': 0,
    'altura': 0,
    'largura': 0,
    'temperatura_desejada': 0,
    'temperatura_ambiente': 0,
    'volume': 0,
    'potencia': 0,
    'filtragem_min': 0,
    'filtragem_max': 0
}

# Entrada dos dados
aquario['comprimento'] = float(input("Digite o comprimento do aquário (cm): "))
aquario['altura'] = float(input("Digite a altura do aquário (cm): "))
aquario['largura'] = float(input("Digite a largura do aquário (cm): "))
aquario['temperatura_desejada'] = float(input("Digite a temperatura desejada (°C): "))
aquario['temperatura_ambiente'] = float(input("Digite a temperatura ambiente (°C): "))

# Cálculos
aquario['volume'] = calcular_volume(aquario['comprimento'], aquario['altura'], aquario['largura'])
aquario['potencia'] = calcular_potencia(aquario['volume'], aquario['temperatura_desejada'], aquario['temperatura_ambiente'])
aquario['filtragem_min'], aquario['filtragem_max'] = calcular_filtragem(aquario['volume'])

# Exibindo os resultados
print(f"\nVolume do aquário: {aquario['volume']:.2f} litros")
print(f"Potência do termostato necessária: {aquario['potencia']:.2f} W")
print(f"Quantidade de filtragem por hora: {aquario['filtragem_min']:.2f} a {aquario['filtragem_max']:.2f} litros")
