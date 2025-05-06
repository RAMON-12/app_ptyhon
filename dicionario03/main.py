#bliblioteca
import os

# dicionario 
dados = {
    "nome": "denis",
    "idade": 30,
    "cpf": "123456789",
}

# exibir os dados do dicionario

for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}.")

# ususario insere nova chave (email) 

dados["email"] = input("informe o email do usuario: ")

#limpa terminal e re-exibe a lista 

os.system("cls")
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}.")



