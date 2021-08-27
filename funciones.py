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