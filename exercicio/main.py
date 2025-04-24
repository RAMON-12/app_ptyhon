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
    # ordena a lista em ordem alfabética
    nomes.sort()
    for item in nomes:
        print(item)
        #TODO - atividade
... cri um programa que receiba do ususruai uma lista de compra e ordenee alista em ordm alfaberica ons so que nome do intem deixe e a quantade de fora .
...