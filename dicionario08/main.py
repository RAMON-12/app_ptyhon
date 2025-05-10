#lista de dicionarios
pessoas = [
    {
        'nome': "fulano de tal",
        'idade': 20,
        'email': "fulanodetal@gmail.com"
    },
    {
        'nome': "cicrano de souza   ",
        'idade': 25,
        'email': "cicrano2gmail.com"
    },
    {
        'nome': "beltrano da silva",
        'idade': 30,
        'email': "beltrano@gmail.com"
    }
]

for pessoa in pessoas:
    print(f"\n{'-'*20}\n")
    for chave in pessoa:
        print(f"{chave.title()}: {pessoa.get(chave)}.")