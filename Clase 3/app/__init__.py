# Programa para aprender la sintaxis basica de Python

while True:
    nombre = input("NOMBRE: ")
    edad = int(input("EDAD: "))

    print("Bienvenido, " + nombre + ". Tienes " + str(edad) + " anios.")

    if (edad < 18):
        print("\nEstas castigado")
    elif (edad == 18):
        print("\nPuedes salir\t...\tPero ven temprano")
    else:
        print("\nLarga a trabajar")

    salida = input("\nDesea continuar(S/N): ")
    if salida.upper() != "S":
        break

print('\nCiao!')
