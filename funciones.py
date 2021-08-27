""" funcion para dar de alta un cajero """

def altaCajero(coleccion_cajeros): 

    nombre = input("Ingrese el nombre del cajero: ")
    coleccion_cajeros[nombre] = "categoria 1"
    print(coleccion_cajeros)