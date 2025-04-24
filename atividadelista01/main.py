
# declaraçao de lista
lista_compras = []

try:
    while True:
        # usuário informa o nome do item
        item = input("Informe o nome do item ou deixe em branco para exibir a lista: ")

        # verifica se o nome foi inserido
        if item != "":
            # usuário informa a quantidade
            quantidade = input(f"Informe a quantidade para '{item}': ")
            # adiciona o item e a quantidade na lista
            lista_compras.append((item, quantidade))
            continue
        else:
            break

    # ordenar a lista apenas pelo nome do item
    lista_compras.sort()

except Exception as e:
    print(f"Não foi possível inserir dados na lista: {e}.")
finally:
    # exibe a lista ordenada
    print(f"Lista de compras ordenada:")
    for item, quantidade in lista_compras:
        print(f"{item} - {quantidade}")