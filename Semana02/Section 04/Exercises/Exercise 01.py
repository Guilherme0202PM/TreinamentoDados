#Exercise 01

# Crie uma função que recebe três números como parâmetro(n1, n2, n3) e imprime na saída padrão a soma dos números
def sum(n1, n2, n3):
    print(n1 + n2 + n3)

n1, n2, n3 = map(int, input("Digite 3 números separados por espaços: ").split())
sum(n1, n2, n3)
