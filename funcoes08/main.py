import math 

#funçao normal

calcular_area_circulo = lambda r: math.pi * (r ** 2)

if __name__ == "__main__":
    try:
        r = float(input("informe o raio do círculo: "))
        result = calcular_area_circulo(r)

        print(f"A área do círculo é: {result}")
    except Exception as e:
        print(f"nao foi possivel  calcaular a area do circulo: {e}")

