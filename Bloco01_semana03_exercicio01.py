'''

1- Escrever um programa que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.

'''

def contar_negativos():
    contador_negativos = 0
    
    for i in range(5):
        valor = float(input(f"Insira o {i+1}º valor: "))
        
        if valor < 0:
            contador_negativos += 1
    
    print(f"Existem {contador_negativos} valores negativos entre os 5 valores inseridos.")

contar_negativos()