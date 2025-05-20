#crie um program onde o usuario das um exolhe  uma dessa opçoes de menu 
# o sair do programa
# 1 cria nova conta
# 2 alterar dados do titular da conta
# 3 exluir conta
# 4 fazer saque 
# 5 fazer deposito
# 6 consulta dados da conta
#  dados do titular da conta
# - nome 
# - cpf
# -  agencia (1010)
# - numero da cora (numeor aleatorio)
# - saldo (sempre vai ser 0)

# cnsultat daos da conta envolver consulta sida da conta 
# para numero da conra ise a blibliotea random
import random
import conta as m 

if __name__ == "__main__":
    conta = None
    while True:
        try:
            print("escolha a opção desejada: \n")
            print("1 - criar nova conta")
            print("2 - alterar dados do titular da conta")
            print("3 - excluir conta")
            print("4 - fazer saque")
            print("5 - fazer deposito")
            print("6 - consultar dados da conta")
            print("7 - sair do programa")
            opcao = input("opcao desejada: ")
            
            if opcao == "1":
                nome = input("informe o nome do titular: ")
                cpf = m.gerar_cpf()
                agencia = m.gerar_agencia()
                numero_conta = m.gerar_numero_conta()
                saldo_inicial = 0
                conta = m.criar_conta(nome, saldo_inicial)
                conta["cpf"] = cpf
                conta["agencia"] = agencia
                conta["numero_conta"] = numero_conta
                print(f"Conta criada com sucesso! Dados da conta: {conta}")
                
            elif opcao == "2":
                novo_titular = input("informe o novo nome do titular: ")
                conta = m.alterar_dados(conta, novo_titular)
            elif opcao == "2":
                if conta is not None:
                    novo_titular = input("informe o novo nome do titular: ")
                    conta = m.alterar_dados(conta, novo_titular)
                    print(f"Dados da conta alterados com sucesso! Novos dados: {conta}")
                else:
                    print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
            elif opcao == "3":
                if conta is not None:
                    conta = m.excluir_conta(conta)
                    print(f"Conta excluída com sucesso! Dados da conta: {conta}")
                else:
                    print("Nenhuma conta cadastrada para excluir.")
            elif opcao == "4":
                if conta is not None:
                    valor = float(input("informe o valor do saque: "))
                    if m.fazer_saque(conta, valor):
                        print(f"Saque de {valor} realizado com sucesso! Saldo atual: {conta['saldo']}")
                    else:
                        print("Saldo insuficiente para realizar o saque.")
                else:
                    print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
            elif opcao == "5":
                if conta is not None:
                    valor = float(input("informe o valor do deposito: "))
                    conta = m.fazer_deposito(conta, valor)
                    print(f"Depósito de {valor} realizado com sucesso! Saldo atual: {conta['saldo']}")
                else:
                    print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
            elif opcao == "6":
                if conta is not None:
                    conta = m.consultar_dados(conta)
                    print(f"Dados da conta: {conta}")
                else:
                    print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
            elif opcao == "7":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida, tente novamente.")
        except Exception as e:
            print(f"Não foi possível executar a operação: {e}.")