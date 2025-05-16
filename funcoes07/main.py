# declaraçao de funçaos recursivas
def calcular_fatorial (n):
    return 1 if n == 0 else n  * calcular_fatorial(n - 1)


if __name__ == "__main__":
    try:
        n = int(input("informe um numero interio possitivo: "))
        result = calcular_fatorial(n)

        print(f"o fatorial de {n} e {result}.")
    except Exception as e:
        print(f"nao foi possivel calcular o fatorial: {e}.")