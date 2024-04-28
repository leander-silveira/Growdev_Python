'''

4 - Numa determinada escola, os critérios de aprovação são os seguintes:
- O aluno deve ter, no máximo, 25% de faltas;
- A nota final deve ser igual ou superior a 7,00.
Construa um programa para ler as notas que um aluno tirou nos 4 bimestres, o número total
de aulas e o número de faltas, mostrando ao final a situação do aluno como sendo
“Aprovado”, “Reprovado por Faltas” e “Reprovado por média”, considerando que a
reprovação por faltas se sobrepõe a reprovação por nota.

'''

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media, faltas, total_aulas):
    percentual_faltas = (faltas / total_aulas) * 100

    if percentual_faltas > 25:
        return "Reprovado por Faltas"
    elif media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado por Média"

def main():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota do {i+1}º bimestre: "))
        notas.append(nota)

    total_aulas = int(input("Digite o número total de aulas: "))
    faltas = int(input("Digite o número de faltas: "))

    media = calcular_media(notas)
    situacao = verificar_situacao(media, faltas, total_aulas)

    print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()