import random

# Criação do tabuleiro
tabuleiro = [[0 for _ in range(20)] for _ in range(20)]
navios_colocados = 0

print("Tabuleiro:")
for row in tabuleiro:
    print(row)



# Colocação dos navios no tabuleiro
while navios_colocados < 20:
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    if tabuleiro[x][y] == 0:
        tabuleiro[x][y] = 1
        navios_colocados += 1

print("Tabuleiro com navios:")
for row in tabuleiro:
    print(row)

# Jogo
tentativas = 0
while tentativas < 35:
    print("Tentativa", tentativas + 1)

    x = int(input("Digite a coordenada X (1-20): "))-1
    while x <0 or x > 19:
        print("Coordenadas inválidas. Tente novamente.")
        x = int(input("Digite a coordenada X (1-20): "))-1

    y = int(input("Digite a coordenada Y (1-20): "))-1
    while y <0 or y > 19:
        print("Coordenadas inválidas. Tente novamente.")
        y = int(input("Digite a coordenada X (1-20): "))-1

#    print(x,y)


    if tabuleiro[x][y] == 1:
        print("Você acertou um navio!")
        tabuleiro[x][y] = 0
        if sum(sum(row) for row in tabuleiro) == 0:
            print("Parabéns, você afundou todos os navios!")
            break
    else:
        print("Você errou!")

    tentativas += 1
else:
    print("Você excedeu o limite de tentativas. Game over.")