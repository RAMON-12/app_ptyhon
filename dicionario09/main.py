import os 

pessoas = []

try:
    while True:
        cadastrar = input("Deseja cadastrar nova pessoa? (s/n): ")
        match cadastrar:
            case "s":
                pessoa = {}

                pessoa["nome"] = input("informe nome da pessoa: ")
                pessoa["email"] = input("informe o email da pessoa: ")
                pessoa["cpf"] = input("informe o cpf da pessoa: ")

                pessoas.append(pessoa)

                os.system("cls")
                print(f"{pessoa.get('nome')} cadastrado com sucesso!")

                for pessoa in pessoas:
                    print(f"\n{'-'*20}\n")
                    for chave in pessoa:
                        print(f"{chave.title()}: {pessoa.get(chave)}.")
                continue

                
            case "n":
                break
            case _:
                print("opcao invalida")
                continue

except Exception as e:
    print(f"Nao foi possivel cadastrar a pessoa: {e}.")