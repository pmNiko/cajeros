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



from funciones import calculoDePagos, subaPorcentaje


categorias = {
    "categoria 1": 250,
    "categoria 2": 380,
    "categoria 3": 490,
    "categoria 4": 600
}

cajeros = {"tomas": "categoria 1", "carlos": "categoria 2", "alex": "categoria 4"}

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

    #opcion para dar de alta un cajero
    if opcion == 1:
        nombre = input("Ingrese el nombre del cajero: ")
        cajeros[nombre] = "categoria 1"
        print(cajeros)

    #opcion cambiar categoria
    elif opcion == 2:
        cajero_a_cambiar = input("ingresar nombre del cajero: ")
        print("seleccione la categoria ")

        i = 1
        for key in categorias:
            print(f"\t{i}- {key}")
            i += 1
        cat = int(input("ingresar categoria: "))
        if cat > 0 and cat <= len(categorias):          
        
            cat_list = list(categorias)
            print(cat_list)
            categoria_asignar = cat_list[cat-1]
            print(categoria_asignar)

            cajeros[cajero_a_cambiar] = categoria_asignar
            print(cajeros)
        else:
            print('opcion incorrecta')       

    # ELIMINAR CAJERO.   
    elif opcion == 3:
        cajero_a_eliminar = input("ingresar nombre del cajero a eliminar: ")
        elemento = cajeros.pop(cajero_a_eliminar, "no existe")
        if elemento == "no existe":
            print("el cajero seleccionado no existe.")
        print(cajeros)
    # CALCULO DE PAGO    
    elif opcion == 4:
        calculoDePagos(cajeros, categorias)
    # SUBA DE PROCENTAJE    
    elif opcion == 5:
         subaPorcentaje(categorias)  
    # OPCION SALIR
    elif opcion == 6:
        print("Saliendo del sistema.")
        bandera = False
    else:
        print("Opcion invalida.")
