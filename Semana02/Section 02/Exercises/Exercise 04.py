"""Exercise 04"""

# Implemente o `ex03.py` mas ao final do programa deve ser apresentado ao usuário todos os problemas que o identificador informado possui(implementar como list de erros):
#     - Ex: identificador informado: B9999999X
#     - erros
#     - O identificar não inicia com a sequencias ‘BR’
#     - O identificador não apresenta números inteiros entre 0001 e 9999

while True:
    identificador = input("Digite o identificador do funcionário (ex: BR0001X): ").strip()

    tamanho_correto = len(identificador) == 7
    prefixo_BR = identificador.startswith("BR")
    sufixo_X = identificador.endswith("X")
    eh_numero = identificador[2:6].isdigit()
    
    if eh_numero:
        numero_valido = 1 <= int(identificador[2:6]) <= 9999
    else:
        numero_valido = False
     
    erros = []

    if not tamanho_correto:
        erros.append("Seu código não possui 7 dígitos")

    if not prefixo_BR:
        erros.append("Seu prefixo é diferente de BR")

    if not sufixo_X:
        erros.append("Seu sufixo é diferente de X")

    if not eh_numero:
        erros.append("Os caracteres 3-6 não são números")
    elif not numero_valido:
        erros.append("O número não está entre 0001 e 9999")

    if len(erros) == 0:
        print("Seu código é válido!")
        break  
    else:
        print("Seu código é inválido pois:")
        for erro in erros:
            print("- ", erro)
        print()