# [17:18, 22/8/2021] Martin ( Programador ): Ejercicio de pago de sueldos de cajeros.
# Se debe realizar un sistema que permita gestionar el pago de sueldos para los empleados encargados de atender la caja. Los empleados trabajan una determinada cantidad de horas mensuales( horas_trabajadas) la hora tiene un precio en base a la categoría:
# categoría_1 -> $250
# categoría_2 -> $380
# categoría_3 -> $490
# categoría_4 -> $600

# Al finalizar el mes se debe calcular el sueldo correspondiente a cada empleado.

# El sistema debe tener el siguiente menú:

# 1- Dar de alta un cajero,
# 2- cambiar categoria de un cajero,
# 3- eliminar cajero,
# 4- calcular pagos
# 5- subir porcentaje de valores de categorias
# 6- salir del sistema"""

# [17:24, 22/8/2021] Martin ( Programador ): Premisas:
# --- para dar de alta un cajero se debe pedir el nombre y asociarlo por defecto a la categoría_1
# --- cambiar la categoría de un cajero, se debe asociar a la nueva categoría especificada disponible.
# --- cálculo de pago: muestra una tabla con los pagos a realizar a cada cajero.
# --- subir porcentaje de pago, se debe ingresar un porcentaje de aumento para afectar el valor de todas las categorías.

# Implementar funciones en un archivo a parte para luego importarlas y hacer uso en cada opción según corresponda.

'''importancion de modulos'''
from funciones import cambiarCategoria, altaCajero, eliminarCajero, calculoDePagos, subaPorcentaje


# Coleccion de categorias
categorias = {
    "categoria 1": 250,
    "categoria 2": 380,
    "categoria 3": 490,
    "categoria 4": 600
}

# Coleccion de cajeros
cajeros = {"tomas": "categoria 1", "carlos": "categoria 2", "alex": "categoria 4"}

# Opciones del menu
menu = """
      Menu
  1- Dar de alta un cajero
  2- Cambiar categoria de un cajero
  3- Eliminar cajero
  4- Calcular pagos
  5- Subir porcentaje de valores de categorias
  6- Salir del sistema
"""

print(menu)

# Bandera de corte del bucle while
bandera = True
# Bucle de iteracion while
while bandera:
    
    # Seleccion de opcion 
    opcion = int(input("Ingrese una opcion: "))

    # Alta de cajero
    if opcion == 1:
        altaCajero(cajeros)   

    # Cambiar categoria
    elif opcion == 2:
        cambiarCategoria(categorias, cajeros)       

    # Eliminar cajero  
    elif opcion == 3:
        eliminarCajero(cajeros)
        
    # Calculo de pagos   
    elif opcion == 4:
        calculoDePagos(cajeros, categorias)
        
    # Suba de porcentaje   
    elif opcion == 5:
         subaPorcentaje(categorias)
           
    # Opcion de fin del bucle
    elif opcion == 6:
        print("Saliendo del sistema.")
        bandera = False
        
    # Opcion no contenida por nuestro menu
    else:
        print("Opcion invalida.")
