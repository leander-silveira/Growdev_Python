'''
6 - Crie uma tupla com os dias da semana e peça para o usuário digitar um número de 1 a 7. Exiba o dia correspondente.
'''

dias_da_sem = ("do", "seg", "ter", "quart", "quint", "sex", "sáb")


num = int(input("digite número de 1 a 7: "))


if 1 <= num <= 7:
    #dia_correspondente = dias_da_sem[num - 1]
    print("O dia correspondente é:", dias_da_sem[num - 1])
else:
    print("error")
