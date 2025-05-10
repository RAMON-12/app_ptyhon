usuario = {}



try:
    # entrada de dados 
    usuario["nome"] = input("informe o nome: ")
    usuario["data de nascimento"] = input("informe a data de nascimento: ")
    usuario["cpf"] = input("informe o cpf: ")
    usuario["email"] = input("informe o email: ")
    usuario["genero"] = input("informe o genero: ")
    usuario["telefone"] = input("informe o telefone: ")
    usuario["peso"] = float(input("informe o peso em kg: ").replace(',', '.'))
    usuario["altura"] = float(input("informe altura em metros: ").replace(',', '.'))
    usuario["tipo sanguineo"] = input("informe o tipo sanguineo: ")

    # exibir os dados do usuario
    for chave in usuario:
        print(f"{chave.title()}: {usuario.get(chave)}")

    # calcular o valor do imc do usuario
    imc = usuario.get("peso") / usuario.get("altura") ** 2

    # exibir valor do imc do usuario
    new_func(usuario, imc)

    # exibir o diagnóstico do usuário com base no valor do imc
    if imc <= 18.5:
        print(f"{usuario.get('nome')} está abaixo do peso.")
    elif imc < 25:
        print(f"{usuario.get('nome')} está no peso ideal. PARABÉNS!!!")
    elif imc < 30:
        print(f"{usuario.get('nome')} está acima do peso ideal.")
    elif imc < 35:
        print(f"{usuario.get('nome')} está obeso.")
    elif imc < 40:
        print(f"{usuario.get('nome')} está com obesidade grau II!")
    else:
        print(f"{usuario.get('nome')} está com obesidade mórbida. PROCURE UM MÉDICO!!!")

except Exception as e:
    print(f"Não foi possível inserir os dados. Erro: {e}")
