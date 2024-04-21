'''

8 - Faça um programa que leia as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos
obedece à tabela abaixo:
Média de Aproveitamento
- Entre 9.0 e 10.0 Conceito - A
- Entre 7.5 e 8.9 - B
- Entre 6.0 e 7.4 - C
- Entre 4.0 e 5.9 - D
- Entre 0 e 3.9 - E

O programa deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem:
APROVADO se o conceito for A, B ou C.
REPROVADO se o conceito for D ou E.

'''

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def atribuir_conceito(media):
    if 9.0 <= media <= 10.0:
        return 'A'
    elif 7.5 <= media < 9.0:
        return 'B'
    elif 6.0 <= media < 7.5:
        return 'C'
    elif 4.0 <= media < 6.0:
        return 'D'
    else:
        return 'E'

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = calcular_media(nota1, nota2)
    conceito = atribuir_conceito(media)

    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Média: {media:.2f}")
    print(f"Conceito: {conceito}")

    if conceito in ['A', 'B', 'C']:
        print("Situação: APROVADO")
    else:
        print("Situação: REPROVADO")

if __name__ == "__main__":
    main()
