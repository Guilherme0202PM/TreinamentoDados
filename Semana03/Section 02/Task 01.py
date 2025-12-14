# open("caminho", "r")

# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura + Escrita

arquivo = open("Aula12/test3.txt", "x")

#Retorna True ou False #Indica se o arquivo foi aberto em um modo que permite leitura
print(arquivo.readable()) 

#Lê todo o conteúdo do arquivo de uma vez
#Retorna uma string
#Após a leitura, o cursor vai para o final do arquivo
print(arquivo.read())

#Lê uma única linha por vez, cada chamada lê a próxima linha
#Retorna uma string (inclui \n, se existir)
print(arquivo.readline())


# lista = arquivo.readlines()

# print(lista)

# print(lista[3])

# arquivo.write("Python\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

#arquivo.close()


#Exclusao de arquivos
import os

# if os.path.exists("Aula12/test2.txt"):
#     os.remove("Aula12/test2.txt")
# else:
#     print("Arquivo não existe")

os.rmdir("Aula12/nova_pasta")
