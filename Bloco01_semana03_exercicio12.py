'''

12 - Escreva um programa que calcula o valor de um investimento após um número específico de anos, considerando juros compostos. O usuário deve fornecer o principal (valor inicial do investimento), a taxa de juros anual (em porcentagem) e o número de anos.

A fórmula para calcular o valor de um investimento após n anos com juros compostos é:

A=P×(1+r)^n

Onde:

A é o valor do investimento após n anos,
P é o principal (valor inicial do investimento),
r é a taxa de juros anual (em decimal), e
n é o número de anos.

Exemplo de saída:

Digite o principal (R$): 1000
Digite a taxa de juros anual (%): 5
Digite o número de anos: 10
O valor do investimento após 10 anos é: R$ 1628.89

'''

def calcular_valor_investimento(principal, taxa_juros, anos):
    # Convertendo a taxa de juros de porcentagem para decimal
    taxa_juros_decimal = taxa_juros / 100
    
    # Calculando o valor do investimento com juros compostos
    valor_investimento = principal * (1 + taxa_juros_decimal) ** anos
    
    return valor_investimento

def main():
    # Solicitando as informações do investimento ao usuário
    principal = float(input("Digite o principal (R$): "))
    taxa_juros = float(input("Digite a taxa de juros anual (%): "))
    anos = int(input("Digite o número de anos: "))
    
    # Calculando o valor do investimento
    valor_final = calcular_valor_investimento(principal, taxa_juros, anos)
    
    # Exibindo o resultado
    print(f"O valor do investimento após {anos} anos é: R$ {valor_final:.2f}")

# Chamando a função principal
main()
