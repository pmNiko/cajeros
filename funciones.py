""" funcion calculo de pago """
def calculoDePagos(cajeros, categorias):
    horas_trabajadas = 60
    print("\tNombre de cajero \tSueldo a cobrar")
    for nombre, categoria in cajeros.items():
        valor_hora = categorias[categoria]
        sueldo_a_pagar = valor_hora * horas_trabajadas
        print(f"\t{nombre.capitalize()} \t\t\t$ {sueldo_a_pagar}")