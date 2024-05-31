'''
Desafio Dicionários:

Busque o código desenvolvido para o exercicio abaixo e altere o algoritmo para:

Salvar o resultado da eleição em um dícionário.
Exemplo de saida do dicionario: {"Candidato 1": 2, "Candidato 2": 2, "Voto Nulo": 0, "Voto Branco": 1}

Este exercicio foi realizado na lista da semana passada, exercicio de número 4:

"Em uma eleição presidencial existem dois candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:

1,2 = voto para os respectivos candidatos

3 = voto nulo

4 = voto em branco;

Elabore um programa que leia o código de votação de 5 eleitores. Calcule e escreva: total de votos para cada candidato total de votos nulos total de votos em branco"
'''

resultado_eleicao = {"Candidato 1": 0, "Candidato 2": 0, "Voto Nulo": 0, "Voto Branco": 0}

for i in range(5):
    codigo_voto = int(input(f"Digite o código de votação do eleitor {i + 1}: "))

    if codigo_voto == 1:
        resultado_eleicao["Candidato 1"] += 1
    elif codigo_voto == 2:
        resultado_eleicao["Candidato 2"] += 1
    elif codigo_voto == 3:
        resultado_eleicao["Voto Nulo"] += 1
    elif codigo_voto == 4:
        resultado_eleicao["Voto Branco"] += 1
    else:
        print("Código de votação inválido. Voto não será contado.")

print("\nResultado da Eleição:")
for cargo, votos in resultado_eleicao.items():
    print(f"{cargo}: {votos} votos")


