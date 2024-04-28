'''

9 - Escreva um programa que leia a idade e salário de 10 pessoas. Informe em seguida: Qual é a média de idade entre as pessoas? Quantas pessoas há por faixa etária, considerando: 
jovens < 18 18 <= adultos < 60 idosos >= 60 Em seguida, mostre qual é a faixa etária que acumula o maior salário.

'''

def calcular_faixa_etaria(idade):
    if idade < 18:
        return "jovem"
    elif idade < 60:
        return "adulto"
    else:
        return "idoso"

def main():
    # Inicializando contadores e variáveis
    total_idade = 0
    contador_jovens = 0
    contador_adultos = 0
    contador_idosos = 0
    salario_jovens = 0
    salario_adultos = 0
    salario_idosos = 0
    maior_salario = 0
    faixa_etaria_maior_salario = ""

    # Pedindo idade e salário de 10 pessoas
    for i in range(10):
        idade = int(input(f"Informe a idade da {i+1}ª pessoa: "))
        salario = float(input(f"Informe o salário da {i+1}ª pessoa: "))
        
        # Calculando média de idade
        total_idade += idade
        
        # Contabilizando pessoas por faixa etária
        faixa_etaria = calcular_faixa_etaria(idade)
        if faixa_etaria == "jovem":
            contador_jovens += 1
            salario_jovens += salario
        elif faixa_etaria == "adulto":
            contador_adultos += 1
            salario_adultos += salario
        else:
            contador_idosos += 1
            salario_idosos += salario
        
        # Verificando faixa etária com maior salário
        if salario > maior_salario:
            maior_salario = salario
            faixa_etaria_maior_salario = faixa_etaria
    
    # Calculando média de idade
    media_idade = total_idade / 10
    
    # Determinando qual faixa etária acumula o maior salário
    if faixa_etaria_maior_salario == "jovem":
        salario_maior_salario = salario_jovens
    elif faixa_etaria_maior_salario == "adulto":
        salario_maior_salario = salario_adultos
    else:
        salario_maior_salario = salario_idosos
    
    # Exibindo resultados
    print(f"\nMédia de idade entre as pessoas: {media_idade:.2f}")
    print(f"Pessoas jovens (< 18 anos): {contador_jovens}")
    print(f"Pessoas adultas (18 <= idade < 60): {contador_adultos}")
    print(f"Pessoas idosas (idade >= 60 anos): {contador_idosos}")
    print(f"A faixa etária que acumula o maior salário é: {faixa_etaria_maior_salario} (Salário total: R${salario_maior_salario:.2f})")

# Chamando a função principal
main()

