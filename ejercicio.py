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

categorias = {
    "categoria 1": 250,
    "categoria 2": 380,
    "categoria 3": 490,
    "categoria 1": 250
}

cajeros = {}

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

bandera = True

while bandera:
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        bandera = False
    else:
        print("Opcion invalida.")
