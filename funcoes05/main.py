# importa modulo
from funcoes import calcular_quadrilatero, calcular_triangulo, calcular_trapezio

if __name__ == "__main__":

    try:
        print("escolha a figura da qaul deseja calacular a area: \n")
        print("1 - quadrilatero")
        print("2 - triangulo")
        print("3 - trapezio")
        opcao = input("opcao desejada: ")
        if opcao == "1" or opcao == "2" or opcao == "3":
             b = float(input("informe o valor da base: ").replace(",", "."))
             h = float(input("informe o valor da altura: ").replace(",", "."))
             
             match opcao:
                 case "1":
                     resultado = calcular_quadrilatero(b, h)
                     print(f" area do quadrilatero : {resultado}.")
                 case 2:
                     resultado = calcular_triangulo(b, h)
                     print(f" area do triangulo : {resultado}.")
                 case 3:
                     resultado = calcular_trapezio(b, B, h)
                     print(f" area do trapezio : {resultado}.")          
        else:
            print("opcao invalida, progrma encerrado.")
    except Exception as e:
        print(f"nao foi possivel executar  a operacao: {e}.")