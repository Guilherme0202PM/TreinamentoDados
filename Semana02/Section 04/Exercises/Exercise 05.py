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
usuario["classificacao"], usuario["situacao"] = classificar_imc(usuario["imc"])

# Saída
print(f"Seu IMC é: {usuario['imc']:.2f}")
print("Classificação:", usuario["classificacao"])
print("Situação:", usuario["situacao"])
