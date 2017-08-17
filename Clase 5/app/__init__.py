from app.circulo import *

if __name__ == '__main__':
    print("CALCULADORA DEL CIRCULO")
    radio = float(input("Radio: "))
    imprimir_resultado(calcular_area(radio), calcular_circunferencia(radio))