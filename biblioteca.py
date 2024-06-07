import json


def menu_principal()-> int:
    """Esta funcion valida que el usuario haya ingresado un numero valido, retorna el numero casteado"""
    res = input("""
1 - Cargar archivo\n2 - Imprimir lista\n3 - Asignar totales
4 - Filtrar por tipo\n5 - Mostrar servicios\n6 - Guardar servicios\n7 - Salir\n
""")
    return res

def leer_json(ruta_archivo: str, nombre_lista: str):
    """Esta funcion recibe una ruta de un archivo JSON y retorna su contenido como una lista,
    Retorna False si el archivo no se encuentra o hay un error"""
    try:
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            return data
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo")
        return False
    except Exception as e:
        print(f"Error desconocido al crear el archivo")
        return False
    
def mostrar_servicios(servicios, id_servicio=True, descripcion=True, tipo=True, precioUnitario=True, cantidad=True,
                      totalServicio=True):
    """Esta funcion recibe una lista y un booleano por cada key en los diccionarios de cada servicio, muestra cada dato de cada servicio
    segun el valor que reciba"""
    if not servicios:
        print("La lista está vacía")
        return

    encabezado = ""
    if id_servicio: encabezado += "{:<12}|".format("id servicio")
    if descripcion: encabezado += "{:<22}|".format("descripcion")
    if tipo: encabezado += "{:<5}|".format("tipo")
    if precioUnitario: encabezado += "{:<14}|".format("precio unitario")
    if cantidad: encabezado += "{:<8}|".format("cantidad")
    if totalServicio: encabezado += "{:<14}|".format("total sevicio")

    print(encabezado)
    print("-" * len(encabezado))

    for servicio in servicios:
        fila = ""
        if id_servicio: fila += "{:<12}|".format(servicio.get("id_servicio", ""))
        if descripcion: fila += "{:<22}|".format(servicio.get("descripcion", ""))
        if tipo: fila += "{:<5}|".format(servicio.get("tipo", ""))
        if precioUnitario: fila += "{:<14}|".format(servicio.get("precioUnitario", ""))
        if cantidad: fila += "{:<8}|".format(servicio.get("cantidad", ""))
        if totalServicio: fila += "{:<14}|".format(servicio.get("totalServicio", ""))

        print(fila)
        print("-" * len(encabezado))

def guardar_json(servicios:list, ruta_archivo:str):
    """Esta funcion recibe una lista y una ruta, guarda los datos proporcionados en un archivo JSON en la ruta"""
    try:
        with open(ruta_archivo, 'w') as archivo:
            json.dump(servicios, archivo, indent=4)
    except Exception as e:
        print(f"Error desconocido al guardar el archivo")

def filtrar_por_tipo(servicios:list, tipo_seleccionado:str):
    """Esta funcion recibe una lista y un key se tipo, filtra los servicios por el tipo seleccionado
    y retorna la nueva lista"""
    servicios_filtrados = []
    for servicio in servicios:
        if servicio["tipo"] == tipo_seleccionado:
            servicios_filtrados.append(servicio)

    return servicios_filtrados
