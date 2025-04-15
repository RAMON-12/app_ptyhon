# declaraçao de variaveis
nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))

# operador ternario
result = "e maior de idade" if idade >= 18 else " e menor de idade"

#exibindo o resultado na tela   
print (f" {nome} {result}.")
