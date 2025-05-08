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
        
        prosseguir = input("deseja excluir  alguma chave? (s/n): ")
        match prosseguir:
            case "s":
                chave_escolhida = input("informe o nome da chave que deseja excluir: ")
                if chave_escolhida in usuario:
                    usuario.pop(chave_escolhida, nome)
                    
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print(f"'{chave_escolhida}' não existe.")
                    continue
            case "n":
                break
            case _:
                print("opção inválida")
                continue
except Exception as e:
    print(f"não foi possível atualizar os dados: {e}.")
