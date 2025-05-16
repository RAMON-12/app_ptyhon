import os
import math

# Função para calcular o número de Fibonacci na posição 'n'
def fibonacci(n):
    if n <= 0:
        return "A posição deve ser um número positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Função para calcular a sequência de Fibonacci até o 'n'-ésimo termo
def fibonacci_sequence(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.append(fibonacci(i))
    return sequence

if __name__ == "__main__":
    try:
        while True:
            print("1 - Calcular número específico da sequência de Fibonacci")
            print("2 - Calcular sequência de Fibonacci até o termo n")
            print("3 - Sair do programa")
            opcao = input("Informe a opção desejada: ")

            match opcao:
                case "1":
                    os.system("cls")
                    n = int(input("Informe a posição do número de Fibonacci desejado: "))
                    result = fibonacci(n)
                    print(f"O número de Fibonacci na posição {n} é: {result}")
                    continue

                case "2":
                    os.system("cls")
                    n = int(input("Informe o número de termos da sequência de Fibonacci: "))
                    result = fibonacci_sequence(n)
                    print(f"A sequência de Fibonacci até o {n}º termo é: {result}")
                    continue

                case "3":
                    print("Programa encerrado com sucesso.")
                    break

                case _:
                    print("Opção inválida, tente novamente.")
                    continue
    except Exception as e:
        print(f"Não foi possível fazer o cálculo: {e}.")

    






