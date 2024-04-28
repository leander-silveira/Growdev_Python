'''

11 - Crie um jogo em que o computador escolha um número aleatório entre 1 e 100, e o jogador tenta adivinhá-lo. O programa deve dar dicas se o número é maior ou menor do que o número digitado pelo jogador. O jogo continua até que o jogador acerte o número.

Exemplo de saída:

Bem-vindo ao jogo de adivinhação!
Tente adivinhar o número entre 1 e 100.
Digite sua tentativa: 50
O número é menor.
Digite sua tentativa: 75
O número é maior.
Digite sua tentativa: 63
O número é menor.
Digite sua tentativa: 68

Parabéns! Você acertou o número 68 em 4 tentativas!

'''
import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    
    while True:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1
        
        if tentativa < numero_aleatorio:
            print("O número é maior.")
        elif tentativa > numero_aleatorio:
            print("O número é menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas!")
            break

# Chamando a função principal para iniciar o jogo
jogo_adivinhacao()
