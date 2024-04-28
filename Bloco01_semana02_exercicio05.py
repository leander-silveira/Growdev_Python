'''

5 - Após construir o programa anterior, crie mais duas versões dele para prever as seguintes
situações:
- Um aluno pode ficar em recuperação se possuir frequência suficiente (superior a
75%) e média superior a 5 mas inferior a 7;
- Caso um aluno reprove por média e faltas, sua situação deve ser “Reprovado por
Média e Faltas” (ao invés de simplesmente “Reprovado por Faltas” como antes).

'''


def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media, faltas, total_aulas):
    percentual_faltas = (faltas / total_aulas) * 100

    if percentual_faltas > 25:
        return "Reprovado por Faltas"
    elif media >= 7.0:
        return "Aprovado"
    elif media >= 5.0 and media < 7.0 and percentual_faltas <= 25:
        return "Recuperação"
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

    if situacao == "Recuperação":
        print("O aluno está em Recuperação.")
        print("Por favor, entre em contato com o professor para maiores informações.")
    else:
        print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()