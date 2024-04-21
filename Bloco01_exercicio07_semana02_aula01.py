'''

7- Construa um programa que leia uma data qualquer (dia, mês e ano) e calcule a data do
próximo dia. Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias. Lembre-se
que um ano é bissexto quando for divisível por 4.

'''

def is_bissexto(ano):
    # Retorna True se o ano for bissexto, False caso contrário
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def calcular_proximo_dia(dia, mes, ano):
    # Lista de meses com 30 dias
    meses_30 = [4, 6, 9, 11]
    
    # Verifica se o mês é fevereiro em um ano bissexto
    if mes == 2 and is_bissexto(ano):
        dias_no_mes = 29
    elif mes == 2:  # Fevereiro em ano não bissexto
        dias_no_mes = 28
    elif mes in meses_30:  # Meses com 30 dias
        dias_no_mes = 30
    else:  # Meses com 31 dias
        dias_no_mes = 31
    
    # Verifica se o dia é o último dia do mês
    if dia == dias_no_mes:
        # Se for o último dia do ano, avança para o próximo ano e mês de janeiro
        if mes == 12:
            return 1, 1, ano + 1
        else:
            return 1, mes + 1, ano
    else:
        # Avança para o próximo dia no mesmo mês e ano
        return dia + 1, mes, ano

def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    
    proximo_dia, proximo_mes, proximo_ano = calcular_proximo_dia(dia, mes, ano)
    
    print(f"A data do próximo dia é: {proximo_dia}/{proximo_mes}/{proximo_ano}")

if __name__ == "__main__":
    main()