# importa bliblioteca
import os

# declara a lista 
cidades = ["São Paulo", "Rio de Janeiro",
            "Belo Horizonte",
            "Goiania", "Brasília","palmas",
            "brasilia","goinaia","brasilia"]

# tratamento de exceção
try:
    #loo p infinito
    while True:
        # limpa o terminal
        os.system("cls")
        #usuario informa o valor da pesquisa
        pesquisa = input("Informe a cidade a ser pesquisada: ").title()


        result = cidades.count(pesquisa)

        # motra resultado na tela
        if result > 0:
            print(f"(pesquisa) foi eonctrado  na lista {result} vezes.")
        else:
            print(f"(pesquisa) não foi encontrado na lista.")
        #perguntamos se o deseja uma nova pesquisa
        continuar = input("Deseja continuar a pesquisa? (s/n): ")
        #verifica se o usuario deseja continuar
        match continuar:
            case "s":
                continue  # continua o loop
            case "n":
                exit()  # encerra o programa
            case _:
                print("Opção invalida.")
                break
except Exception as e:
    print(f"Não foi possível realizar a busca.  {e}.")

