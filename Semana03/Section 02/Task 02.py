# arquivos.py
# Comentário: nome do arquivo Python (apenas informativo)

###
#Exemplo 1: Abertura de arquivo em modo escrita
arq = open('arquivo.txt', 'w')# Abre (ou cria) o arquivo "arquivo.txt" no modo escrita ('w')

lista = ['Olá', 'Caio', 'Tudo']# Cria uma lista de strings

arq.write()# ERRO: o método write() precisa receber um texto como argumento

arq.writelines()# ERRO: o método writelines() precisa receber uma lista ou iterável de textos

###
#Exemplo 2: Abertura de arquivo em modo escrita
arq = open('arquivo.txt', 'w')

arq.write('Caio\nMarcos\nJoão')

arq.close()

###
#Exemplo 3: Abertura de arquivo em modo leitura

with open('arquivo.txt', 'rb') as arq:
    # Abre o arquivo "arquivo.txt" em modo leitura binária ('rb')

    x = arq.read()
    # Lê todo o conteúdo do arquivo e armazena em x
    # Nesse modo, o conteúdo é do tipo bytes

    print(type(x.decode()))
    # Converte os bytes para string usando decode()
    # Mostra o tipo do dado após a conversão (str)
