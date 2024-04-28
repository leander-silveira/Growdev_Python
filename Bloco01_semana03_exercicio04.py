'''

4 - Em uma eleição presidencial existem dois candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:

1,2 = voto para os respectivos candidatos
3 = voto nulo
4 = voto em branco;

Elabore um programa que leia o código de votação de 5 eleitores. Calcule e escreva: total de votos para cada candidato total de votos nulos total de votos em branco

'''

def contar_votos():
    votos_candidato1 = 0
    votos_candidato2 = 0
    votos_nulos = 0
    votos_branco = 0
    
    for i in range(5):
        codigo = int(input(f"Insira o código de votação do {i+1}º eleitor (1 para candidato 1, 2 para candidato 2, 3 para voto nulo, 4 para voto em branco): "))
        
        if codigo == 1:
            votos_candidato1 += 1
        elif codigo == 2:
            votos_candidato2 += 1
        elif codigo == 3:
            votos_nulos += 1
        elif codigo == 4:
            votos_branco += 1
        else:
            print("Código inválido! Por favor, insira um código válido.")
    
    print("\nResultados da eleição:")
    print(f"Total de votos para o candidato 1: {votos_candidato1}")
    print(f"Total de votos para o candidato 2: {votos_candidato2}")
    print(f"Total de votos nulos: {votos_nulos}")
    print(f"Total de votos em branco: {votos_branco}")

contar_votos()

