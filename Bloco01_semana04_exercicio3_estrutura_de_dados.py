'''
Crie uma lista com 100 números inteiros.

Pode ser uma sequência.
Os dados não devem ser inseridos manualmente, utilize de um laço de repetição para adicionar os elementos a Lista. 

3 - Exiba o maior e o menor número da lista.
'''

lista_num_int = []

for i in range(1, 101):
    lista_num_int.append(i)

maior_num_lista_num_int = max(lista_num_int)
menor_num_lista_num_int = min(lista_num_int)

print("O maior número da lista de números interiros é: ", maior_num_lista_num_int)
print("O menor número da lista de números interiros é: ", menor_num_lista_num_int)