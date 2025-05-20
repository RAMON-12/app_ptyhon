def fazer_deposito(saldo,valot):
    saldo += valor
    return saldo

def fazer_saque(saldo, valor):
    saldo -= valor
    return saldo

def consultar_dados(titular):
    print(f"{'_'*20} dados da conta {'_'*20}\n")
    print(f"titular: {titular.get('nome')}")
    print(f"cpf: {titular.get('cpf')}")
    print(f"agencia do titular: {titular.get('agencia')}")
    print(f"numero da conta do titular: {titular.get('num_conta')}")
    print(f"saldo da conta do titular: {titular.get('saldo'):.2f}")
    
