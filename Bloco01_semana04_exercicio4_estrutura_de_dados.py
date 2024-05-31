'''
Crie uma lista com 100 números inteiros.

Pode ser uma sequência.
Os dados não devem ser inseridos manualmente, utilize de um laço de repetição para adicionar os elementos a Lista. 

4 - Pesquise se o número 77 esta presente na lista e exiba:

Quantas vezes esse número aparece na lista
Se aparece em qual ou quais posições(Indice).
'''

lista_num_int = []
count_77 = 0

for i in range(1, 101):
    lista_num_int.append(i)

cont_lista_num_int = lista_num_int.count(77)
indices = [i for i, num in enumerate(lista_num_int) if num == 77]

print("O número 77 aparece", cont_lista_num_int, "vezes na lista.")
print("O número 77 está nos índices", indices)

