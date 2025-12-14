#ex03.py – Convertendo uma linha em dicionário genérico. Com base nos códigos dos exercícios anteriores, crie a função:

#def linha_para_dict(linha, chaves):
#"""Recebe uma linha e uma lista de chaves e retorna um dicionário."""

#A função deve receber:

#Uma linha do arquivo (string, por exemplo: SP00001,Maria da Silva,[maria@gmail.com](mailto:maria@gmail.com))

#Uma lista de chaves, por exemplo: ['prontuario', 'nome', 'email']

#Exemplo 1

#Linha: SP00001,Maria da Silva,[maria@gmail.com](mailto:maria@gmail.com)
#Chaves: ['prontuario', 'nome', 'email']

#Saída:
#{
#'prontuario': 'SP00001',
#'nome': 'Maria da Silva',
#'email': '[maria@gmail.com](mailto:maria@gmail.com)'
#}

#Exemplo 2

#Linha: banana,3
#Chaves: ['item', 'quantidade']

#Saída:
#{
#'item': 'banana',
#'quantidade': '3'
#}

#Considere que todos os valores presentes no dicionário serão strings (não é necessário converter para int/float neste exercício, exceto quando explicitamente pedido em outros enunciados, como no código de projeto no ex02).

#Dica: esta função é genérica. Ela poderá ser reutilizada em outros exercícios (como ex01 e ex02) para evitar duplicar código.

def linha_para_dict(linha, chaves):
    dicionario = {}
    for chave, valor in zip(chaves, linha.strip().split(',')):
        dicionario[chave] = valor
    return dicionario

linha = "SP00001,Maria da Silva,[maria@gmail.com](mailto:maria@gmail.com)"
chaves = ['prontuario', 'nome', 'email']
print(linha_para_dict(linha, chaves))