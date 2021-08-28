""" funcion para dar de alta un cajero """

def altaCajero(coleccion_cajeros): 

    nombre = input("Ingrese el nombre del cajero: ")
    coleccion_cajeros[nombre] = "categoria 1"
    print(coleccion_cajeros)
    

""" Fn eliminar cajero """

def eliminarCajero(coleccion_cajeros):
    cajero_a_eliminar = input("ingresar nombre del cajero a eliminar: ")
    elemento = coleccion_cajeros.pop(cajero_a_eliminar, "no existe")
    if elemento == "no existe":
        print("el cajero seleccionado no existe.")
    print(coleccion_cajeros)