# declaração de função
def dar_boas_vindas(nome,curso):
    return f"{nome}, seja bem-vindo ao curso de {curso}!"

# algoritomo principal
nome = input("Informe seu nome: ")
curso = input("Informe o nome do seu curso: ")

print(dar_boas_vindas(nome,curso))

