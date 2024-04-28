'''

9 - As Organizações XTC resolveram dar um aumento de salário aos seus colaboradores e
lhe contrataram para desenvolver o programa que calcula os reajustes. Faça um programa
que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
no salário atual:
- salários até R$ 280,00 (incluindo): aumento de 20%
- salários entre R$ 280,00 e R$ 700,00: aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
- salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.

'''

# Função para calcular o reajuste salarial
def calcular_reajuste(salario):
    if salario <= 280:
        percentual_aumento = 20
    elif salario <= 700:
        percentual_aumento = 15
    elif salario <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    aumento = salario * percentual_aumento / 100
    novo_salario = salario + aumento

    return percentual_aumento, aumento, novo_salario

# Função para exibir os resultados na tela
def exibir_resultados(salario, percentual_aumento, aumento, novo_salario):
    print("Salário antes do reajuste: R$", salario)
    print("Percentual de aumento aplicado:", percentual_aumento, "%")
    print("Valor do aumento: R$", aumento)
    print("Novo salário após o aumento: R$", novo_salario)

# Programa principal
if __name__ == "__main__":
    salario_atual = float(input("Digite o salário atual do colaborador: R$ "))
    percentual_aumento, aumento, novo_salario = calcular_reajuste(salario_atual)
    exibir_resultados(salario_atual, percentual_aumento, aumento, novo_salario)
