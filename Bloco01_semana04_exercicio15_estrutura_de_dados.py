'''
Crie uma lista com os números Impares de 1 a 20 utilizando listas por compreensão.
'''

numeros_impares = [num for num in range(1, 21) if num % 2 != 0]

print(numeros_impares)