'''
Conversão de graus Celsius para Fahrenheit – Crie um programa que converta graus
Celsius em Fahrenheit.
O programa deve solicitar ao usuário que insira uma temperatura em graus Celsius e, em
seguida, exiba a temperatura convertida em Fahrenheit. Após construir esse programa,
modifique-o para que converta graus Fahrenheit em graus Celsius.

'''

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    escolha = input("Escolha a conversão que deseja realizar:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n")

    if escolha == '1':
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {resultado}°F")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"A temperatura em Celsius é: {resultado}°C")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()