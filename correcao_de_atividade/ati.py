def calcular_fibonacci(n):
    return n if n <= 1 else calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)s
    





if __name__ == "__main__":
    try:
        n = int(input("Informe o numero da sequencia de fibonacci: "))
        resul = calcular_fibonacci(n)

        print(f"valor da seuqncia e fibonacci: {resul}")
    except Exception as e:
        print(f"nao foi possivel calcular o valor da sequencia de fibonacci: {e}")
       