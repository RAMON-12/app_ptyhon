import os

chaves = ("nome", "idade", "cpf", "email", "profissao", "telefone")
usuario = {
    chaves[0]: "denis",
    chaves[1]: 33,
    chaves[2]: "123456789",
    chaves[3]: "denis@example.com",
    chaves[4]: "programador",
    chaves[5]: "999999999",
}

try:
    while True:
        for chave in usuario:
            print(f"{chave.title()}: {usuario.get(chave)}")
        
        prosseguir = input("deseja alterar o dado de alguma chave? (s/n): ")
        match prosseguir:
            case "s":
                chave_escolhida = input("informe o nome da chave que deseja alterar: ")
                if chave_escolhida in usuario:
                    usuario[chave_escolhida] = input("informe o novo valor da chave escolhida: ")
                    os.system("cls")
                else:
                    os.system("cls")
                    print(f"'{chave_escolhida}' não existe.")
            case "n":
                break
            case _:
                print("opção inválida")
except Exception as e:
    print(f"não foi possível atualizar os dados: {e}.")
