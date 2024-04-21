'''

6 - Escreva um programa que peça ao usuário para fornecer um dia, mês e o ano arbitrários
e determine se esses dados correspondem a uma data válida. Não deixe de considerar que
existem meses com 30 e 31 dias, e que fevereiro pode ter 28 ou 29 dias, dependendo se o
ano for bissexto. Considere que um ano é bissexto quando for divisível por 4.

'''

def verificar_data(dia, mes, ano):
    # Lista de meses com 30 dias
    meses_30 = [4, 6, 9, 11]
    
    # Verifica se o mês está entre 1 e 12
    if mes < 1 or mes > 12:
        return False
    
    # Verifica se o dia está dentro do intervalo correto para cada mês
    if mes in meses_30:
        if dia < 1 or dia > 30:
            return False
    elif mes == 2:  # Fevereiro
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):  # Ano bissexto
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    else:
        if dia < 1 or dia > 31:
            return False
    
    return True

def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    
    if verificar_data(dia, mes, ano):
        print("A data é válida.")
    else:
        print("A data é inválida.")

if __name__ == "__main__":
    main()