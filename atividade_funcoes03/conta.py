def criar_conta(titular, saldo_inicial):
    return {
        "titular": titular,
        "saldo": saldo_inicial
    }

def alterar_dados(conta, novo_titular):
    conta["titular"] = novo_titular
    return conta

def excluir_conta(conta):
    return None
def fazer_saque(conta, valor):
    if conta["saldo"] >= valor:
        conta["saldo"] -= valor
        return True
    else:
        return False
def fazer_deposito(conta, valor):
    conta["saldo"] += valor
    return conta
def consultar_dados(conta):
    return conta
def gerar_numero_conta():
    import random
    return random.randint(1000, 9999)
def gerar_agencia():
    return 1010
def gerar_cpf():
    import random
    return str(random.randint(100000000, 999999999))    
def gerar_nome():
    import random
    nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
    return random.choice(nomes)
def criar_conta_aleatoria():
    nome = gerar_nome()
    cpf = gerar_cpf()
    agencia = gerar_agencia()
    numero_conta = gerar_numero_conta()
    saldo_inicial = 0
    conta = criar_conta(nome, saldo_inicial)
    conta["cpf"] = cpf
    conta["agencia"] = agencia
    conta["numero_conta"] = numero_conta
    return conta
