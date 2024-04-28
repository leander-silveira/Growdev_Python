'''

8 - Crie um programa para que retorne o somatório de todos os números entre 1 e um valor fornecido pelo usuário. Por exemplo, se o usuário fornecer o número 4, 
o computador deverá calcular o somatório 1+ 2 + 3 + 4 = 10.

'''

def calcular_somatorio(valor):
    somatorio = 0
    
    # Iterar de 1 até o valor fornecido e somar os números
    for i in range(1, valor + 1):
        somatorio += i
    
    return somatorio

# Solicitar ao usuário fornecer um número
numero = int(input("Digite um número inteiro positivo: "))

# Calcular o somatório e exibir o resultado
resultado = calcular_somatorio(numero)
print(f"O somatório de todos os números de 1 até {numero} é: {resultado}")
