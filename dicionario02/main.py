# dicionario 
usuario = dict(nome="fulano de tal", idade=18, email="fulanotal@example.com")

#exibindo os dados do dicionário
for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}.")
