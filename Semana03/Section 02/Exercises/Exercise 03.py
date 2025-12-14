# Exercício 3

def linha_para_dict(linha, chaves):
    dicionario = {}
    for chave, valor in zip(chaves, linha.strip().split(',')):
        dicionario[chave] = valor
    return dicionario

linha = "SP00001,Maria da Silva,[maria@gmail.com](mailto:maria@gmail.com)"
chaves = ['prontuario', 'nome', 'email']
print(linha_para_dict(linha, chaves))