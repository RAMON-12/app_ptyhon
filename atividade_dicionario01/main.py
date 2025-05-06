#crie um programa que inicializa um dicionario zerado eo ususuario adcionae ensere os seguinte dados:
#nome , data de nascimento, cpf, e mail genero , telefone, alttura , peso m tipo sanguineo,
# ao final o program exibe os dados do ususrio informa seu imc .
# o ususario devera informar o valor apenas dessa chave
# e o programa devera exibir os dado em uma linha diferente
# o resultado do imc devera ser arredondado para duas 2 casas decimais
# mostro o diagnstio do usuario  de acorido com o valor do imc
dados = {
    "nome": "denis",
    "data_nascimento": "12/01/1990",
    "cpf": "123456789",
    "email": "alunosenai@exemplo.com",
    "genero": "masculino",
    "telefone": "6299999999",
    "altura": 1.62,
    "peso": 72.0,
    "tipo_sanguineo": "O+"
}

try:
    while True:
        # exibir dados do usuario
        print("Dados do usuário:")
        for chave in dados:
            print(f"{chave.title()}: {dados.get(chave)}.")

        prosseguir = input("deseja calcular o imc? (s/n): ")
        match prosseguir:
            case "s":
                # calcular imc
                imc_valor = dados["peso"] / (dados["altura"] ** 2)
                print(f"\nSeu IMC é: {imc_valor:.2f}")
                
                # perguntar se o usuario quer continuar
                continuar = input("Deseja adicionar uma nova chave? (s/n): ")
                if continuar == "s":
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
    
    
        
        
        
