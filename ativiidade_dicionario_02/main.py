# TODO
...
#crie um crud, ou seja, um programa que:
#cadastro
#lista
#altere 
#exlua
# o prorama devera cadastrar pessoas com os seguintes dados:
#nome,cpf, e-mail, telefone , data de nascimento, genero.
...
#note o usuario podera cadastrar quantos pessoa quiser,
#o programa devera fornecer um menu com as opções de cadastro, lista, alterar, excluir e sair do programa.
import os

pessoas = []

try:
    while True:
        print("Menu:")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Alterar pessoa")
        print("4. Excluir pessoa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                pessoa = {}
                pessoa["nome"] = input("Informe o nome da pessoa: ")
                pessoa["cpf"] = input("Informe o CPF da pessoa: ")
                pessoa["email"] = input("Informe o email da pessoa: ")
                pessoa["telefone"] = input("Informe o telefone da pessoa: ")
                pessoa["data_nascimento"] = input("Informe a data de nascimento da pessoa: ")
                pessoa["genero"] = input("Informe o gênero da pessoa: ")

                pessoas.append(pessoa)
                os.system("cls")
                print(f"{pessoa.get('nome')} cadastrado com sucesso!")
                continue
            case "2":
                os.system("cls")
                if not pessoas:
                    print("Nenhuma pessoa cadastrada.")
                else:
                    for pessoa in pessoas:
                        print(f"\n{'-'*20}\n")
                        for chave in pessoa:
                            print(f"{chave.title()}: {pessoa.get(chave)}.")
                continue
            case "3":
                os.system("cls")
                if not pessoas:
                    print("Nenhuma pessoa cadastrada.")
                else:
                    cpf_alterar = input("Informe o CPF da pessoa que deseja alterar: ")
                    for pessoa in pessoas:
                        if pessoa["cpf"] == cpf_alterar:
                            print(f"Pessoa encontrada: {pessoa['nome']}")
                            pessoa["nome"] = input("Novo nome: ")
                            pessoa["email"] = input("Novo email: ")
                            pessoa["telefone"] = input("Novo telefone: ")
                            pessoa["data_nascimento"] = input("Nova data de nascimento: ")
                            pessoa["genero"] = input("Novo gênero: ")
                            print(f"{pessoa['nome']} alterado com sucesso!")
                            break
                    else:
                        print("Pessoa não encontrada.")
                continue
            case "4":   
                os.system("cls")
                if not pessoas:
                    print("Nenhuma pessoa cadastrada.")
                else:
                    cpf_excluir = input("Informe o CPF da pessoa que deseja excluir: ")
                    for pessoa in pessoas:
                        if pessoa["cpf"] == cpf_excluir:
                            pessoas.remove(pessoa)
                            print(f"{pessoa['nome']} excluído com sucesso!")
                            break
                    else:
                        print("Pessoa não encontrada.")
                continue
            case "5":
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue
except Exception as e:
    print(f"Não foi possível realizar a operação: {e}.")

            
