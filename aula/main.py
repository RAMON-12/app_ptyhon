import os
import math


def calcular_1_grau(a, b):
    
    x = -b / a
    return x
def calcular_2_grau(a, b, c):
    if a is not 0:
        delta = (b**2) - 4*a*c
        if delta > 0:
            x1 =(-b+math.sqrt(delta)) / (2 * a)
            x2 =(-b-math.sqrt(delta)) / (2 * a)
            yield f"x' = {x1}"
            yield f'x" = {x2}'
        elif delta == 0:
            x = -b / 2 * a
            yield f"x = {x}"
        else:
            yield "a equação não possui raízes reais."

    else:
        yield "o valor de 'a' e zero, e portanto nao e uma equação de 2 grau."



if __name__ == "__main__":
   try:
       while True:
            print("1 - calcular equação de 1 grau")
            print("2 - calcular equação de 2 grau")
            print("3 - sair do programa")
            opcao = input("informe a opcao desejada: ")
            match opcao:
                case "1":
                    os.system("cls")
                    a = float(input("informe o valor de a: ").replace(",", "."))
                    b = float(input("informe o valor de b: ").replace(",", "."))

                    print("ovalo de x em{a}x+{b}=0 e:{result}.")
                    continue

                case "2":
                    os.system("cls")
                    a = float(input("informe o valor de a: ").replace(",", "."))
                    b = float(input("informe o valor de b: ").replace(",", "."))
                    c = float(input("informe o valor de c: ").replace(",", "."))
                    result = calcular_2_grau(a, b, c)

                    for x in result:
                        print(x)

                    continue
                case "3":
                    print("programa encerrado com sucesso.")
                    
                    break
                case _:
                    print("opcao invalida, tente novamente.")
                    continue
   except Exception as e:
       print(f"nao foi possivel fazer o calculo: {e}.")
