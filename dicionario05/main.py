chaves = ("nome","idade","cpf","email","profissao","telefone")
usuario = {
    chaves[0]: "denis",
    chaves[1]: 33,
    chaves[2]: "123456789",
    chaves[3]: "denis@example.com",
    chaves[4]: "programador",
    chaves[5]: "999999999",
}
for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}")
