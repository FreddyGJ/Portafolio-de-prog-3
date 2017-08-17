def imprimir_lista(x):
    print("\nMi lista de supermercado...")
    for a in x:
        print(str((int(x.index(a)+1))) + ". " + a)

def imprimir_lista(x):
    print("\nMi lista de supermercado...")
    for a in x:
        print(str((int(x.index(a)+1))) + ". " + a)

def imprimir_diccionario(w):
    print("\nMi lista de supermercado...")
    for art, cant in w.items():
        print("Articulo: " + str(art) + " (cantidad: " + str(cant) + ")")



if __name__== "__main__":
    #lista = []
    diccionario = {}

    while True:
        print("\n\nLista de supermercado")
        print("1. Agregar elemento")
        print("2. Quitar elemento")
        print("3. Ver lista")
        print("4. Guardar en TXT")
        print("5. Salir")
        try:
            opc = int(input("Opcion: "))
        except ValueError:
            opc = 0

        if opc == 1:
            print("\nVamos a ingresar un articulo a la lista...")
            artInsertar = input("Articulo: ")
            #if artInsertar not in lista:
            if artInsertar not in diccionario:
                #lista.append(artInsertar)
                diccionario[artInsertar] = 1
            else:
                #print("Articulo ya en la lista")
                diccionario[artInsertar] += 1
        elif opc == 2:
            print("\nVamos a quitar un articulo de la lista...")
            #imprimir_lista(lista)
            while True:
                imprimir_diccionario(diccionario)
                artBorrar = input("Articulo: ")
                if artBorrar in diccionario:
                    try:
                        op = int(input("1. Borrar todo\n2. Borrar cantidad exacta"))
                    except:
                        op = 0

                    if op == 1:
                        del diccionario[artBorrar]
                        break
                    elif op == 2:
                        while True:
                            try:
                                c = int(input("Cantidad: "))
                            except ValueError:
                                print("Cantidad invalida")
                            if c > 0 and c < int(diccionario[artBorrar]):
                                diccionario[artBorrar] -= c
                                break
                            elif c == int(diccionario[artBorrar]):
                                del diccionario[artBorrar]
                                break
                            else:
                                print("Cantidad invalida")
                    else:
                        print("Opcion invalida. Intente nuevamente.")
                break
            #if artBorrar in lista:
            #      lista.remove(artBorrar)
            #else:
            #    print("Lo siento. Articulo no encontrado. ")
        elif opc  == 3:
            print ("\nMi lista de supermercado...")
            #imprimir_lista(lista)
            imprimir_diccionario(diccionario)
        elif opc == 4:
            archivo = open("lista.txt", "w")
            for art, cant in diccionario.items():
                archivo.write("Articulo: " + str(art) + " (" + str(cant) + ")\n")
            archivo.close()
        elif opc == 5:
            break
        else:
            print("ERROR: :opcion no valida")
    print("Hasta luego")