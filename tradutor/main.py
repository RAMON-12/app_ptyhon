from deep_translator import GoogleTranslator

try:
    # declaração de variáveis
    tradutor = GoogleTranslator(source="auto", target="pt")

    # laço de repetição
    while True:
        # declaração de variáveis
        texto = input("Digite o texto a ser traduzido em qualquer idioma: ")
        texto_traduzido = tradutor.translate(texto)  

        # exibe o texto traduzido
        print(f'Texto traduzido: "{texto_traduzido}"')

        # informa se deseja traduzir outro texto
        encerrar = input("Deseja traduzir outro texto? (s/n): ")
        match encerrar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")

except Exception as e:
    print(f"Não foi possível traduzir. Erro: {e}.")