def calcular_area_comodos():
    # Definição da area total é zero no começo
    total_area = 0

    while True:
        # Entrada de dados que o usuario fornece

        largura = float(input("Digite a largura do cômodo (em metros): "))
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

        # Calculo Matematico da area do comodo

        area_comodo = largura * comprimento
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

        # Calculo Matematico de soma da area do comodo com a area total

        total_area += area_comodo

        # Questiona o usuario se ele deseja adicionar mais comodos

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()
        if mais_comodos != 's':
            break

    return total_area

# Processa as informações e exibe o resultado

area_total = calcular_area_comodos()
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")
