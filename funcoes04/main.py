#declaraçao de função
def calculando_triangulo(b,h):
    area = (b*h)/2
    return area

#algoritomo principal
try:
    b = float(input("Informe o valor da base").replace(",","."))
    h = float(input("Informe o valor da altura").replace(",","."))
    area = calculando_triangulo(b,h)

    print(f"o valor da area do triangulo é {area}.")
except Exception as e:
    print(f" nao foi possivel calcular a area do triangulo. {e}.")
