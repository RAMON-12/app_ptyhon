# importa bliblioteca
import os
import time

# tratamento de exeções
try:
    
    #declaraçao de variaveis
    n = int(input("informe um numero inteiro positivo: "))

    # laço de repetição
    for n in range(n, -1, -1):
        os.system("cls")
        print(f"{n}...")
        time.sleep(1)
    print("BOMMMM!!!")
    print("a cobra vai fumar!!!")
    
except Exception as e:
    print(f"nao possivel realizar a contagem regressiva: {e}.")
