def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):

    # Diagnostico de acordo com a glicemia do usuario

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
        return "Diabetes"
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
        return "Pre-diabetes"
    else:
        return "Normal"

# Entrada de dados do usuario

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

# Saida do resultado e diagnostico

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
print(f"O diagnostico é: {resultado}")
