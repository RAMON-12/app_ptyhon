try:
    while True:
        # Declaração de variáveis
        nome = input("Informe o seu nome: ")
        idade = input("Informe sua idade: ")

        # Verifica se a idade é um número válido
        if not idade.isdigit():
            print("Idade inválida. Digite apenas números.")
            continue
        
        idade = int(idade)

        # Exibe opções de sala
        print("\nEscolha a sala de cinema:")
        print("1 - Sala 1 (filme para maiores de 18 anos)")
        print("2 - Sala 2 (filme para maiores de 18 anos)")
        print("3 - Sala 3")
        print("4 - Sala 4")
        print("5 - Sala 5")

        # Decisão
        sala = input("Informe o número da sala que deseja assistir (ou 'sair' para encerrar): ")
        
        if sala.lower() == "sair":
            break

        match sala:
            case "1" | "2":
                if idade >= 18:
                    print(f"{nome}, você escolheu a Sala {sala}. Aproveite o filme!")
                else:
                    print(f"{nome}, você não tem idade suficiente para assistir ao filme na Sala {sala}. Escolha outra sala.")
            case "3" | "4" | "5":
                print(f"{nome}, você escolheu a Sala {sala}. Aproveite o filme!")
            case _:
                print("Sala inválida. Tente novamente.")
        
        print("\n")  # Espaço visual entre repetições

except Exception as e:
    print(f"nao foi possivel executar a operação. {e}.")
finally:
    print("Programa encerrado.")
