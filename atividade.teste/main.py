import os


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
        if prosseguir == "s":
            # perguntar se o usuario quer continuar
            continuar = input("Deseja adicionar uma nova chave? (s/n): ")
            if continuar == "s":
                nova_chave = input("\ninforme o nome da nova chave: ")
                dados[nova_chave] = input(f"informe o valor de {nova_chave}: ")
                # calcular imc
                prosseguir = input("deseja calcular o imc? (s/n): ")
        if prosseguir == "s":
            imc_valor = dados["peso"] / (dados["altura"] ** 2)
            print(f"\nSeu IMC é: {imc_valor:.2f}")
            continue
        elif prosseguir == "n":
            break
        else:
            print("opcao invalida.")
            continue
except Exception as e:
    print(f"nao foi possivel inserir a nova chave: {e}.")
    