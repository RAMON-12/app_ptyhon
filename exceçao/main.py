#tratamento de exceções
try:

    #declaraçao de variaveis
    x = int(input("informe um numero inteiro: "))


    # saida de dados    
    print(f"o numero informado foi: {x}.")
except Exception as e:
    print(f"nao foi possivel ler o numero informado pelo usuario.{e}")
finally:
    print("meu programa foi executado com sucesso!")
    