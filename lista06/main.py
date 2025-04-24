# declaração de lista 
nomes = []

# tratamento de exceção
try:
    while True:
        # usuário informa o nome
        item = input("Informe um nome ou deixe em branco para exibir a lista: ") 

        # verifica se o nome foi inserido
        if item != "":
            # adiciona o nome na lista
            nomes.append(item)
            continue
        else:
            break
    #ordenar a lista
    nomes.sort()
    
except Exception as e:
    print(f"Não foi possível inserir dados na lista: {e}.")
finally:
    for item in nomes:
        print(item)
