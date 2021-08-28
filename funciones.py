
""" funcion calculo de pago """
def calculoDePagos(cajeros, categorias):
    horas_trabajadas = 60
    print("\tNombre de cajero \tSueldo a cobrar")
    for nombre, categoria in cajeros.items():
        valor_hora = categorias[categoria]
        sueldo_a_pagar = valor_hora * horas_trabajadas
        print(f"\t{nombre.capitalize()} \t\t\t$ {sueldo_a_pagar}")
        
        
def subaPorcentaje(categorias):
    porcentaje = int(input('ingrese el porcentaje: '))
    for key in categorias:
        valor_hora_1 = categorias[key] 
        valor = (valor_hora_1 * porcentaje) / 100
        nuevo_valor = valor_hora_1 + valor
        categorias[key] = nuevo_valor
    print(categorias) 


'''funcion cambiar categoria'''

def cambiarCategoria(categorias1, cajeros1):
    cajero_a_cambiar = input("ingresar nombre del cajero: ")
    print("seleccione la categoria ")

    i = 1
    for key in categorias1:
        print(f"\t{i}- {key}")
        i += 1
    cat = int(input("ingresar categoria: "))
    if cat > 0 and cat <= len(categorias1):          
    
        cat_list = list(categorias1)
        print(cat_list)
        categoria_asignar = cat_list[cat-1]
        print(categoria_asignar)

        cajeros1[cajero_a_cambiar] = categoria_asignar
        print(cajeros1)
    else:
        print('opcion incorrecta')


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


