'''
Crie um dicionário com o nome e a idade de três pessoas. Busque por um nome e exiba a idade correspondente.
'''

pessoas = {
    "João": 30,
    "Maria": 25,
    "Pedro": 35
}

nome_busca = input("Digite o nome da pessoa para buscar sua idade: ")

if nome_busca in pessoas:
    print(f"A idade de {nome_busca} é {pessoas[nome_busca]} anos.")
else:
    print("Nome não encontrado.")
