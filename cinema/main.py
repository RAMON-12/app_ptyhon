try:
    # Declaração de variáveis
    nome = input("Informe o seu nome: ")
    idade = int(input("Informe sua idade: "))
    
    # Laços de repetição
    while True:
        print(f"{'-' * 20} Lista de Filmes {'-' * 20}\n")
        print("Sala 1 - A Roda Quadrada - Livre")
        print("Sala 2 - A Volta dos que Não Foram - 12 anos")
        print("Sala 3 - As Tranças do Rei Careca - 14 anos")
        print("Sala 4 - Poeira em Alto Mar - 16 anos")
        print("Sala 5 - A Vingança do Peixe Frito - 18 anos")

        # Recebe a sala desejada pelo usuário
        sala = input("\nInforme o número da sala: ")

        # Verifica a sala escolhida
        match sala:
            case "1":
                idade_minima = 0
            case "2":
                idade_minima = 12
            case "3":
                idade_minima = 14
            case "4":
                idade_minima = 16
            case "5":
                idade_minima = 18
            case _:
                
                idade_minima = idade + 1

        # Verifica se tem idade mínima para assistir ao filme
        if idade >= idade_minima:
            print(f"Sala {sala} escolhida. Tenha um bom filme.")
            break
        else:
            print(f"{nome}, você não possui idade para ver o filme.")
            print("Favor selecionar outro filme.")
            continue

except Exception as e:
    print(f"Não foi possível executar a operação. {e}.")
finally:
    print("Programa encerrado.")


    
