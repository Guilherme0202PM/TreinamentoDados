# Utilizando as diretrizes de Índice de Massa Corporal(IMC) da Organização Mundial de Saúde(OMS), crie uma calculadora em python que solicita ao usuário seu peso(Kg) e sua altura(m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar a situação atual do indivíduo('normal', 'perder peso', 'ganhar peso') com base na classificação Peso normal.


# Calculadora de IMC baseada nas diretrizes da OMS

# Calcula o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# Retorna a classificação e a situação com base no IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Excesso de peso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

# Retorna apenas a situação com base na classificação
def definir_situacao(classificacao):
    if classificacao == "Peso normal":
        return "normal"
    elif classificacao == "Baixo peso":
        return "ganhar peso"
    else:
        return "perder peso"

# Dicionário do usuário
usuario = {
    "peso": 0,
    "altura": 0,
    "imc": 0,
    "classificacao": "",
    "situacao": ""
}

# Entrada de dados
usuario["peso"] = float(input("Digite seu peso em kg: "))
usuario["altura"] = float(input("Digite sua altura em metros: "))

# Processamento
usuario["imc"] = calcular_imc(usuario["peso"], usuario["altura"])
usuario["classificacao"] = classificar_imc(usuario["imc"])
usuario["situacao"] = definir_situacao(usuario["classificacao"])

# Saída
print(f"Seu IMC é: {usuario['imc']:.2f}")
print("Classificação:", usuario["classificacao"])
print("Situação:", usuario["situacao"])
