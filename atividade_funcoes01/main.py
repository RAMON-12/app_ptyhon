
import time

import modelo as m 

if __name__ == "__main__":
    while True:
        try:
            print("escolha a equação que deseja calcular: \n")
            print("1 - equação de 1º grau")
            print("2 - equação de 2º grau")
            opcao = input("opcao desejada: ")
            if opcao == "1" or opcao == "2":
                x = float(input("informe o valor de x: ").replace(",", "."))
                a = float(input("informe o valor de a: ").replace(",", "."))
                b = float(input("informe o valor de b: ").replace(",", "."))
                
                match opcao:
                    case "1":
                        resultado = m.calcular_1_grau(a, b, x)
                        print(f" resultado da equação de 1º grau : {resultado}.")
                    case "2":
                        c = float(input("informe o valor de c: ").replace(",", "."))
                        resultado = m.calcular_2_grau(a, b, c, x)
                        print(f" resultado da equação de 2º grau : {resultado}.") 
                    
                        
            else:
                print("opcao invalida, programa encerrado.")
                
        except Exception as e:
            print(f"nao foi possivel executar  a operacao: {e}.")