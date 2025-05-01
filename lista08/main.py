# importando a biblioteca 
import os

#declaraçao de listas 
cidades = ["Brasilia", "Sao paulo", "Rio de janeiro", "Curitiba", "Recife", "Fortaleza", "Salvador", ]

# tratamento de exceção
try:
    # looop infinito 
    while True:
        #exibe a lista 
        for i in range(len(cidades)):
            print(f"cidade do codigo: {i}: {cidades[i]}.")

            # ususuario informa  se  deseja alterar algum valor
            alterar = input("\nDeseja alterar o  alguma valor? (s/n): ")
            match alterar:
                case "s":
                    # usuario informa a posicao do valor que deseja alterar
                    codigo_cidade = int(input("\nInforme o código da cidade que deseja alterar: "))
                    
                    # usuario informa o novo valor
                    nova_cidade = input("Informe o novo nome da cidade: ")

                    cidades[codigo_cidade] = nova_cidade  # troca o valor
                    os.system("cls")  # limpa o terminal
                    continue
                case "n":
                    break
                case _:
                    print("Opção inválida.")
                    break

except Exception as e:
    print(f"Não foi possível alterar  valor na lista. {e}.")

