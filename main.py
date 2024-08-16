def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
    # Calculo Matematico da taxa de juros diária a partir da taxa anual
    taxa_juros_diaria = taxa_juros_anual / 365 / 100

    # Calculo Matematico de somaa do valor dos juros acumulados pelo atraso
    juros = valor_principal * taxa_juros_diaria * dias_atraso

    # Calcula o valor total a ser pago
    valor_total = valor_principal + juros

    return valor_total, juros

# Dados de entrada (NÃO FORNECIDOS PELO USUARIO!!!)
# Pré setados

valor_principal = 1000.00
taxa_juros_anual = 5.0
dias_atraso = 30

# Calculo Matematico dos juros

valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)

# Exibe o resultado

print(f"Valor total a ser pago: R${valor_total:.2f}")
print(f"Valor dos juros: R${juros:.2f}")
