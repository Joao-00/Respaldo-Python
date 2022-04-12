#ejercicio 4
#crear agenda con diccionarios


agenda = {}

cantidad = int(input("Indique la cantidad de contactos a agendar: "))
if cantidad > 0:
    print("--- AGENDA ---")
    for c in range(0,cantidad):
        nombre = input("Nombre de contacto: ")
        if nombre in agenda:
            print("{} ya registrado, su numero {}".format(nombre,agenda[nombre]))
        else:
            agenda[nombre] = input("Indique el numero telefonico: ")

    print("\nListado de contactos")
    for nombre, numero in agenda.items():
        print(nombre, " --> ", numero)
else:
    print("la cantidad de contactos debe ser positiva")


#probar en PyScripter
