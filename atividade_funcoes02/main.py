#crie um orograma que calcule um numero informado pelo usuario da swquealencia de fibonacci
#utilizar funçoes recursivas
# Função recursiva para calcular o número de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar ao usuário o número de Fibonacci que ele deseja calcular
numero = int(input("Digite o número de Fibonacci que você deseja calcular: "))

# Calcular o número de Fibonacci e exibir o resultado
resultado = fibo2nacci(numero)
print(f"O número de Fibonacci de {numero} é: {resultado}")
