def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
    # Da start nas váriaveis

    total_notas = 0
    num_alunos = len(notas)
    aprovados = []
    reprovados = []

    # Analise de cada nota para checkar se o aluno foi aprovado ou reprovado

    for aluno, nota in notas.items():
        total_notas += nota
        if nota >= nota_minima_aprovacao:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)

    # Calculo Matematico da media da turma

    media_turma = total_notas / num_alunos

    return media_turma, aprovados, reprovados

# Entrada de dados dos alunos (NÃO FORNECIDOS PELO USUARIO!!!)
# Pré Definido

notas = {
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

# Media minima para aprovação

nota_minima_aprovacao = 70

# Calcula a média
# Faz a lista de aprovados e reprovados

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

# Exibe os resultados

print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")
