import os 
import random as r
import modulo as m



if __name__ == "__main__":
    titular = {}
    try: 
        while True:
           


            print(f"'_'*10 branco cobra {'_'*10}")
            print("0 - sair do programa")
            print("1 - criar nova conta")
            print("2 - alterar dados do titular da conta")
            print("3 - fazer saque")
            print("4 - fazer deposito")
            print("5 - consultar dados da conta")
            opcao = input("informe a opcao desejada: ")
            os.system("cls")
            match opcao:
                case "0":
                    print("programa encerrado com sucesso")
                    print(" tenha um otimo dia")
                    break   
                case "1":
                    titular ['agencia'] = 1010
                    titular ['num_conta'] = r.randint(10000, 99999)
                    titular ['saldo'] = 0.00
                    titular['nome'] = input("informe o nome do titular: ")
                    titular['cpf'] = input("informe o cpf do titular: ")

                    
                    os.system("cls")
                    print(f"{titular.get('num_conta')} criada com sucesso.\n")

                    continue
                case "2":
                    print(f"nome{titular.get('nome')}")
                    print(f"cpf{titular.get('cpf')}")
                    campo = input("informe o cmapo que deseja alterar: ").strip()  lower()
                    match campo:
                        case "nome":
                            titular ['nome'] = input("informe o novo nome do titular: ")
                            

                            os.system("cls")
                            print("nome do atualizado com sucesso")
                        case "cpf":
                            titular ['cpf'] = input("informe o novo cpf do titular: ")
                            

                            os.system("cls")
                            print("cpf do titular atualizado com sucesso")
                        case _:
                            print("campo invalido")
                    
                    continue

                            
                            
                case "3":
                    calor = float(input("informe o valor do saque:R$ ")) os.replace(",", ".")
                    saldo = titular.get('saldo')


                    if valor <= saldo:
                        tirular['saldo'] = m.fazer_saque(saldo, valor)

                        os.system("cls")
                        print("saque efetuado com sucesso.")
                        print(f"saldo R$: {titular.get('saldo'):.2f}\n")
                    else:
                        print("nao foi posssivel efeutuar o saqque. valor indisponivel")
                    continue
                    
                case "4":
                    valor = float(input("informe o valor do deposito:R$ ")) replace(",", ".")
                    titular['saldo'] = m.fazer_deposito(titular.get('saldo'), valor)

                    os.system("cls")
                    print("deposito efetuado com sucesso.")
                    print(f"saldo R$: {titular.get('saldo'):.2f}\n")
                    continue
                case "5":
                    m.cconsultar_dados(titular)
                    continue
                
                case _:
                    print("opcao invalida")
                    continue    
                
    except Exception as e:
        print(f"nao foi possivel executar a operacao: {e}")