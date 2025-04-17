#tratamento de exeções
try:
   #declaraçao de variaveis
   n = int(input("informe um numero inteiro positivo: "))

   # laço for 
   for n in range(n, -1,-1):
    print(n)

except Exception as e:
    print(f"nao possivel realizar a contagem: {e}.")


