'''
Crie uma lista com as letras da frase "Sou estudante de dados", utilizando listas por compreensão.
'''

frase = "Sou estudante de dados"

letras = [letra for letra in frase if letra != " "]

print(letras)
