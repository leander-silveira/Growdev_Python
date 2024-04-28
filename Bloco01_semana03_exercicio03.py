'''

3 - Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano. Construa um programa que calcule e imprima quantos anos serão necessários para que Zé 
seja maior que Chico.

'''

def calcular_anos():
    altura_chico = 150  
    altura_ze = 110 
    crescimento_chico = 2  
    crescimento_ze = 3  
    anos = 0

    while altura_ze <= altura_chico:
        altura_chico += crescimento_chico
        altura_ze += crescimento_ze
        anos += 1

    return anos

anos_necessarios = calcular_anos()
print(f"Serão necessários {anos_necessarios} anos para que Zé seja maior que Chico.")
