# Utilizando as diretrizes de Índice de Massa Corporal(IMC) da Organização Mundial de Saúde(OMS), crie uma calculadora em python que solicita ao usuário seu peso(Kg) e sua altura(m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar a situação atual do indivíduo('normal', 'perder peso', 'ganhar peso') com base na classificação Peso normal.


# Calculadora de IMC baseada nas diretrizes da OMS

# Calcula o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# Retorna a classificação e a situação com base no IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso", "ganhar peso"
    elif imc < 25:
        return "Peso normal", "normal"
    else:
        return "Acima do peso", "perder peso"


# Programa principal
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao, situacao = classificar_imc(imc)

print(f"Seu IMC é: {imc:.2f}")
print("Classificação:", classificacao)
print("Situação:", situacao)
