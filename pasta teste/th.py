import random

def criar_conta(nome_titular, saldo_inicial):
    return {"titular": nome_titular, "saldo": saldo_inicial}

def alterar_dados(conta, novo_titular):
    if conta is not None:
        conta["titular"] = novo_titular
    return conta

def excluir_conta(conta):
    return None

def fazer_saque(conta, valor):
    if conta is not None and conta["saldo"] >= valor:
        conta["saldo"] -= valor
        return True
    return False

def fazer_deposito(conta, valor):
    if conta is not None:
        conta["saldo"] += valor
    return conta

def consultar_dados(conta):
    return conta if conta is not None else "Conta inexistente"

def gerar_numero_conta():
    return str(random.randint(10000, 99999))

def gerar_agencia():
    return str(random.randint(1000, 9999))

def gerar_cpf():
    return f"{random.randint(100,999)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(10,99)}"

def gerar_nome():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"]
    return random.choice(nomes)

def criar_conta_aleatoria():
    return criar_conta(gerar_nome(), random.uniform(0, 10000))

if __name__ == "__main__":
    conta = None
    try:
        while True:
            print("1 - Criar conta")
            print("2 - Alterar dados da conta")
            print("3 - Excluir conta")
            print("4 - Fazer saque")
            print("5 - Fazer depósito")
            print("6 - Consultar dados da conta")
            print("7 - Gerar número da conta")
            print("8 - Gerar agência")
            print("9 - Gerar CPF")
            print("10 - Gerar nome")
            print("11 - Criar conta aleatória")
            print("12 - Sair do programa")
            opcao = input("Informe a opção desejada: ")
            match opcao:
                case "1":
                    nome_titular = input("Informe o nome do titular: ")
                    saldo_inicial = float(input("Informe o saldo inicial: "))
                    conta = criar_conta(nome_titular, saldo_inicial)
                    print(f"Conta criada com sucesso! Titular: {conta['titular']}, Saldo: {conta['saldo']}")
                case "2":
                    if conta is not None:
                        novo_titular = input("Informe o novo nome do titular: ")
                        conta = alterar_dados(conta, novo_titular)
                        print(f"Dados alterados com sucesso! Novo titular: {conta['titular']}")
                    else:
                        print("Nenhuma conta existente para alterar.")
                case "3":
                    if conta is not None:
                        conta = excluir_conta(conta)
                        print("Conta excluída com sucesso!")
                    else:
                        print("Nenhuma conta existente para excluir.")
                case "4":
                    if conta is not None:
                        valor_saque = float(input("Informe o valor do saque: "))
                        if fazer_saque(conta, valor_saque):
                            print(f"Saque de {valor_saque} realizado com sucesso! Saldo atual: {conta['saldo']}")
                        else:
                            print("Saldo insuficiente para realizar o saque.")
                    else:
                        print("Nenhuma conta existente para saque.")
                case "5":
                    if conta is not None:
                        valor_deposito = float(input("Informe o valor do depósito: "))
                        conta = fazer_deposito(conta, valor_deposito)
                        print(f"Depósito de {valor_deposito} realizado com sucesso! Saldo atual: {conta['saldo']}")
                    else:
                        print("Nenhuma conta existente para depósito.")
                case "6":
                    if conta is not None:
                        dados_conta = consultar_dados(conta)
                        print(f"Dados da conta: {dados_conta}")
                    else:
                        print("Nenhuma conta existente para consultar.")
                case "7":
                    numero_conta = gerar_numero_conta()
                    print(f"Número da conta gerado: {numero_conta}")
                case "8":
                    agencia = gerar_agencia()
                    print(f"Agência gerada: {agencia}")
                case "9":
                    cpf = gerar_cpf()
                    print(f"CPF gerado: {cpf}")
                case "10":
                    nome = gerar_nome()
                    print(f"Nome gerado: {nome}")
                case "11":
                    conta_aleatoria = criar_conta_aleatoria()
                    print(f"Conta aleatória criada com sucesso! Titular: {conta_aleatoria['titular']}, Saldo: {conta_aleatoria['saldo']}")
                case "12":
                    print("Saindo do programa...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
