'''
2- Escreva um programa que receba um número e escreva “Par” caso esse número seja par
e escreva “Impar” caso esse número seja impar.

'''

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def main():
    numero = int(input("Digite um número: "))
    resultado = verificar_par_impar(numero)
    print(f"O número {numero} é {resultado}.")

if __name__ == "__main__":
    main()
