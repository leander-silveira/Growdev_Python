'''

6 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

'''

def fibonacci(n):
    fibonacci_series = [1, 1]  # Inicializa a série de Fibonacci com os dois primeiros termos

    # Gera a série de Fibonacci até o n-ésimo termo
    while len(fibonacci_series) < n:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]  # Calcula o próximo termo
        fibonacci_series.append(next_term)  # Adiciona o próximo termo à série

    return fibonacci_series

n = int(input("Digite o valor de n para gerar a série de Fibonacci até o n-ésimo termo: "))
serie_fibonacci = fibonacci(n)
print(f"A série de Fibonacci até o {n}º termo é: {serie_fibonacci}")
