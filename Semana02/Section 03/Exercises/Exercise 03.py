# - Solicite ao usuário o mês do ano no formato numérico 1, 2, 3 ..12 e apresente o nome do ano.
# - Exemplo: entrada 3 saída ‘Março’.
# - **Implementar com Dicionário**

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

mes = int(input("Digite o mês do ano: "))
print(f"O mês digitado foi: {meses[mes]}")