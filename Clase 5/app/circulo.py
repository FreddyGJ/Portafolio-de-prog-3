def calcular_area(r):
    return 3.1416 * r ** 2

def calcular_circunferencia(r):
    return 2 * 3.1416 * r

def imprimir_resultado(a, c):
    print("El area es %.2f cm2" % a)
    print("La circunferencia es %.2f cm" % c)

#if __name__ == '__main__':
#   print("CALCULADORA DEL CIRCULO")
#   radio = float(input("Radio: "))
#   imprimir_resultado(calcular_area(radio), calcular_circunferencia(radio))