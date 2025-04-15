#declaraçao de varxiaveis
x = float(input("informe o valor de x: "))
y = float(input("informe o valor de y: "))

# mostra o menu 
print("escolha a operacao desejada:")
print("1 - soma")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")
print("5 - restoda divisao")

# usuario escolhe a operacao
operador = input("informe o numero da operacao desejada: ")

# etrutura metch
match operador:
    case "1":
        print(f"resultado da soma: {x+y}.")
    case "2":
        print(f"resultado da subtração: {x-y}.")
    case "3":
        print(f"resultado da multiplicação: {x*y}.")
    case "4":
        print(f"resultado da divisão: {x/y}.")
    case "5":
        print(f"resultado da divisão: {x%y}.")
    case _:
        print("operacao invalida.")