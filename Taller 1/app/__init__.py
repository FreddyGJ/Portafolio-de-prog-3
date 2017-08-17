def mayor_cuota(w):
    print("\nEl que tuvo mas ventas.")
    for nom, cta in w.items():
        print("Nombre: " + str(nom) + "\nCuota: " + str(cta))

def menor_cuota(q):
    print("\nEl que tuvo menos ventas.")
    for nom, cta in q.items():
        print("Nombre: " + str(nom) + "\nCuota: " + str(cta))

if __name__ == "__main__":
    empleados = {}

    while True:
        print("\nCUOTA MENSUAL DE LA EMPRESA ABC")
        print("1. Agregar cuota de usuario.")
        print("2. Mostrar vendedor con mayor cuota.")
        print("3. Mostrar vendedor con menor cuota.")
        print("4. Mostrar total mensual.")
        print("5. Salir")
        try:
            opc = int(input("\nOpcion: "))
        except ValueError:
            opc = 0

        may = -99999
        men = 99999999
        vt = 0

        if opc == 1:
            print("\nIngrese su nombre y apellido: ")
            emInsertar = input("> ")
            print("\nIngrese la cuota realizada: ")
            empleados[emInsertar] = input("> ")
            if emInsertar > str(may):
                may = emInsertar

            if emInsertar < str(men):
                men = emInsertar

        elif opc == 2:
            print("\nLa mayor cuota fue: ", may)
        elif opc == 3:
            print("\nLa menor cuota fue: ", men)
        elif opc == 4:
            print("\nEste es total de ganancias del mes")
            print("Las ganacias fueron: ", vt)
            print(empleados[x])
        elif opc == 5:
            break
    print("Hasta Luego!")