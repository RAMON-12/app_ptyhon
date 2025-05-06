import os

dados = {
    "nome": "denis",
    "idade": 30,
    "cpf": "123456789",
}

try:
    while True:


        for chave in dados:
            print(f"{chave.title()}: {dados.get(chave)}.")

        # o usuario informa se deseja adicionar uma nova chave ou encerra o programa
        prosseguir = input("deseja inseri novos dados? (s/n): ")

        match prosseguir:
            case "s":
                # usuario informa os dados
                nova_chave = input("\ninforme o nome da nova chave: ")
                dados[nova_chave] = input(f"informe o valor de {nova_chave}: ")
                continue
            case "n":
                break
            case _:
                print("opcao invalida.")
                continue
except Exception as e:
    print(f"nao foi possivel inserir a nova chave: {e}.")
    
