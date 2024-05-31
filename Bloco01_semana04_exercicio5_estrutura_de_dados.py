'''
Crie uma lista com 100 números inteiros.

Pode ser uma sequência.
Os dados não devem ser inseridos manualmente, utilize de um laço de repetição para adicionar os elementos a Lista. 

5 - Ordene a lista de forma descendente e exiba.
'''

lista_num_int = []


for i in range(1, 101):
    lista_num_int.append(i)

lista_num_int.sort(reverse=True)

print("Lista em ordem decrescente: ", lista_num_int)