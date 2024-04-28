'''

2 - A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:

a) média do salário da população;
b) média do número de filhos;
c) maior salário;
d) percentual de pessoas com salário até R$2000,00.

Escreva um programa que receba as informações necessárias de 5 pessoas conforme a descrição e responda às questões a, b, c e d anteriores.

'''

def main():
    total_salario = 0
    total_filhos = 0
    maior_salario = 0
    contador_salario_ate_2000 = 0
    
    for i in range(5):
        salario = float(input(f"Informe o salário da {i+1}ª pessoa: R$"))
        num_filhos = int(input(f"Informe o número de filhos da {i+1}ª pessoa: "))
        
        total_salario += salario
        total_filhos += num_filhos
        
        if salario > maior_salario:
            maior_salario = salario
        
        if salario <= 2000:
            contador_salario_ate_2000 += 1
    
    media_salario = total_salario / 5
    media_filhos = total_filhos / 5    
    percentual_salario_ate_2000 = ((contador_salario_ate_2000 / 5) * 100)
    

    print(f"\nMédia do salário da população: R${media_salario:.2f}")
    print(f"Média do número de filhos: {media_filhos:.2f}")
    print(f"Maior salário: R${maior_salario:.2f}")
    print(f"Percentual de pessoas com salário até R$2000,00: {percentual_salario_ate_2000:.2f}%")

main()