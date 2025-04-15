#tratamento de exceções
try:
    # declaraçao de variaveis
    n = int(input("informe um numero positivo: "))
    #loop
    while n > 0:
        print(n)
        n -= 1
except Exception as e:
    print(f"numero invalido. {e}.")
