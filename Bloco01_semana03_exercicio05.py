'''

5 - Escreva um programa que receba o nome de 10 pessoas e para cada pessoa, o lugar para o qual ela já viajou. Sendo que existem 3 possibilidades:

Rio de Janeiro
Bahia
Minas Gerais

Após, informar qual foi o destino mais visitado e qual o menos visitado.

'''

def main():
    destinos = ['Rio de Janeiro', 'Bahia', 'Minas Gerais']
    contagem_destinos = {'Rio de Janeiro': 0, 'Bahia': 0, 'Minas Gerais': 0}
    
    # Pedindo o nome e destino de viagem para 10 pessoas
    for i in range(10):
        nome = input(f"Informe o nome da {i+1}ª pessoa: ")
        print("Destinos disponíveis:")
        for j, destino in enumerate(destinos, start=1):
            print(f"{j}. {destino}")
        escolha = int(input("Informe o número correspondente ao destino para o qual a pessoa viajou: "))
        
        # Atualizando a contagem de destinos
        contagem_destinos[destinos[escolha - 1]] += 1
    
    # Encontrando o destino mais visitado e o menos visitado
    destino_mais_visitado = max(contagem_destinos, key=contagem_destinos.get)
    destino_menos_visitado = min(contagem_destinos, key=contagem_destinos.get)
    
    # Exibindo os resultados
    print(f"\nO destino mais visitado foi: {destino_mais_visitado} ({contagem_destinos[destino_mais_visitado]} visitas)")
    print(f"O destino menos visitado foi: {destino_menos_visitado} ({contagem_destinos[destino_menos_visitado]} visitas)")

main()
