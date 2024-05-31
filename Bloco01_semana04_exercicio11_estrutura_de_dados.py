'''
Crie um dicionário com os nomes de algumas frutas e suas respectivas cores. Exiba na tela somente as frutas que são vermelhas.
'''

dicionario_frutas_cores = {
    "maçã": "vermelho",
    "banana": "amarelo",
    "morango": "vermelho",
    "uva": "roxo",
    "laranja": "laranja"
}

print("frutas que são vermelhas:")
for fruta, cor in dicionario_frutas_cores.items():
    if cor == "vermelho":
        print(fruta)
