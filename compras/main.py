# limpando a biblioteca 
import os

# declaração de lista
lista = []

# tratamento de exceção  
try:
    # loop infinito
    while True:
        # input
        item = input("Informe o nome do item ou deixe em branco para encerrar:") 
        os.system("cls")  # limpa o terminal 

        # verificar se o item está vazio ou não 
        if item != "":
            lista.append(item)  # inserir o item na lista 
            print(f"{item} inserido na lista com sucesso")  # mensagem de confirmação 
            continue
        else:
            break
    # ordena lista
    lista.sort()

except Exception as e:
    print(f"Não foi possível inserir item na lista. Erro: {e}")
finally:
   print("Lista de iten:\n")
    # imprime a lista
   for item in lista:
        print(item)