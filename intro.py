# Função para calcular juros e descontos
def calculo_juros_descontos():
    # Solicitação do valor e da porcentagem ao usuário
    valor = float(input("Informe o valor: "))
    porcentagem = float(input("Informe a porcentagem: "))

    # Cálculo do valor com desconto e valor com juros
    valor_porcentagem = (porcentagem * valor) / 100
    valor_desconto = valor - valor_porcentagem
    valor_juros = valor + valor_porcentagem

    # Exibição dos resultados
    print(f"\n{valor} com {porcentagem}% de desconto é {valor_desconto}\n")
    print(f"{valor} com {porcentagem}% de juros é {valor_juros}\n")


# Chamada da função
calculo_juros_descontos()
