'''
1 - Crie uma lista com 100 números inteiros.

Pode ser uma sequência, ou caso queira se desafiar faça de números aleatorios.
Os dados não devem ser inseridos manualmente, utilize de um laço de repetição para adicionar os elementos a Lista.
[ ]

2 - Calcule e exiba a soma de todos os números da lista.'''

lista_num_int = []

for i in range(1, 101):
    lista_num_int.append(i)

soma_lista_num_int = sum(lista_num_int)

print("A lista de número interiros é: ", lista_num_int)
print("A soma dos número inteiros da lista é: ", soma_lista_num_int)