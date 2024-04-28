'''

10 - Crie uma calculadora simples que realiza operações de adição, subtração, multiplicação, divisão e exponenciação. O programa deve continuar pedindo operações até que o usuário escolha sair.

'''

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def exponenciacao(x, y):
    return x ** y

def main():
    while True:
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Exponenciação")
        print("6 - Sair")

        escolha = input("Digite o número correspondente à operação desejada: ")

        if escolha == '6':
            print("Encerrando o programa...")
            break

        if escolha not in ('1', '2', '3', '4', '5'):
            print("Opção inválida! Por favor, escolha uma opção válida.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", adicao(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicacao(num1, num2))
        elif escolha == '4':
            print("Resultado:", divisao(num1, num2))
        elif escolha == '5':
            print("Resultado:", exponenciacao(num1, num2))

# Chamando a função principal para iniciar a calculadora
main()
