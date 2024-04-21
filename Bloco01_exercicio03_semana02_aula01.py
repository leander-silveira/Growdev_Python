'''

3 - Escreva um programa que receba dois números, exiba as opções:
1 - adição
2 - subtração
Então peça ao usuário para escolher uma das opções. Caso escolha a opção 1 o programa
deve realizar a soma dos dois números lidos e exibir. Caso escolha a opção 2 o programa
deve realizar a subtração dos dois números lidos e exibir.

'''

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Escolha uma opção:")
    print("1 - Adição")
    print("2 - Subtração")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        resultado = adicao(num1, num2)
        print(f"A soma de {num1} e {num2} é: {resultado}")
    elif opcao == '2':
        resultado = subtracao(num1, num2)
        print(f"A subtração de {num1} e {num2} é: {resultado}")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()