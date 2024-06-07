from biblioteca import *

opciones_habilitadas = False
while True:
    opcion = menu_principal()
    print("")
    if opcion == "1":
            nombre_archivo = input("Ingrese el nombre del archivo JSON: ")
            lista = leer_json("primer_parcial\data (1).json", nombre_archivo)
            if lista:
                opciones_habilitadas = True
                print("Lista obtenida")

    elif opciones_habilitadas == False:
            print("Debe cargar un archivo para acceder al menú. Ingrese '1'")

    elif opcion == "2":
        mostrar_servicios(lista)

    elif opcion == "3":
        pass

    elif opcion == "4":
        tipo_seleccionado = input("Ingrese el tipo que qquiere filtrar: ")
        servicios_filtrados = filtrar_por_tipo(lista, tipo_seleccionado)
        print(servicios_filtrados)
        guardar_json(servicios_filtrados, "primer_parcial/nuevo_archivo.json")

    elif opcion == "5":
        pass

    elif opcion == "6":
        pass
    elif opcion == "7":
        print("Saliendo del programa")
        break
    else:
        print("Ingrese una opción válida")
