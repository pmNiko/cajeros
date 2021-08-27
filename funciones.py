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

