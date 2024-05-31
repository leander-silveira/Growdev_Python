'''
Crie um dicionário com os nomes e idades de algumas pessoas. Peça para o usuário digitar um nome e sua nova idade, e atualize o dicionário com essa informação.
'''

pessoas = {
    "João": 30,
    "Maria": 25,
    "Pedro": 35
}

nome = input("Digite o nome da pessoa: ")
nova_idade = int(input("Digite a nova idade: "))

pessoas[nome] = nova_idade

print("Dicionário atualizado:", pessoas)


