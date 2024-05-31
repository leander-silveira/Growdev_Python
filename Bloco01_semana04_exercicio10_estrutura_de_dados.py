'''
Crie uma lista com alguns números repetidos. Converta essa lista em um set para remover as duplicatas e exiba o resultado.
'''

lista_numeros = [1, 2, 3, 4, 5, 2, 3, 6, 7, 4, 8, 9, 5]

set_numeros = set(lista_numeros) # Conversão da lista em um set para remover duplicatas

print("original:", lista_numeros)
print("set sem duplicatas:", set_numeros)
