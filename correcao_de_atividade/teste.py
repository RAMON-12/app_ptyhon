def calcular_1_grau(a, b, x):
    return a * x + b * x

def calcular_2_grau(a, b, c, x):
    return a * x**2 + b * x + c

if __name__ == "__main__":
    while True:
        try:
            print("Escolha a equação que deseja calcular:")
            print("1 - Equação de 1º grau")
            print("2 - Equação de 2º grau")
            opcao = input("Opção desejada (1 ou 2, outra para sair): ")
            if opcao == "1":
                x = float(input("Informe o valor de x: ").replace(",", "."))
                a = float(input("Informe o valor de a: ").replace(",", "."))
                b = float(input("Informe o valor de b: ").replace(",", "."))
                resultado = calcular_1_grau(a, b, x)
                print(f"Resultado da equação de 1º grau: {resultado}\n")
            elif opcao == "2":
                x = float(input("Informe o valor de x: ").replace(",", "."))
                a = float(input("Informe o valor de a: ").replace(",", "."))
                b = float(input("Informe o valor de b: ").replace(",", "."))
                c = float(input("Informe o valor de c: ").replace(",", "."))
                resultado = calcular_2_grau(a, b, c, x)
                print(f"Resultado da equação de 2º grau: {resultado}\n")
            else:
                print("Opção inválida. Programa encerrado.")
                break
        except Exception as e:
            print(f"Não foi possível executar a operação: {e}\n")

            # atividade

#crie um programa onde o usuario podera escolher se deseja calcular a equação de 1º grau oi a equalao do 2º grau, eo progra, reorna o sulrado da eqiavlao 
# o prodram devera ser exeultado em loop 