#ejercicio 1 cambio de divisas

#datos de entrada:
#   tipo de moneda que tienes - PCHL USA EU
#   monto a cambiar
#   tipo de moneda que deseas - USA EU

#proceso:
#   cambio = monto_moneda_tiene / valor_moneda_cambio
#   dolar= {'PCHL': 809.95, 'EU': 0.86}
#   euro= {'PCHL': 939.18, 'USA': 1.16}

#salida:
#   imprimir el monto obtenido en el cambio y la moneda


def EU(*Change):
    euro= {'PCHL': 939.18, 'USA': 1.16}
    return Change[1]/euro[Change[0].upper()]

def USA(*Change):
    dolar= {'PCHL': 809.95, 'EU': 0.86}
    return Change[1]/dolar[Change[0].upper()]

def Captura_datos():
    monedatiene = input("¿Cual moneda tienes? -> PCHL - peso chileno, USA - dolares, EU - euros: ")
    montocambiar = float(input("Indique el monto a cambiar: "))
    monedacambiar = input("Moneda a cambiar -> USA o EU: ")
    return monedatiene, montocambiar, monedacambiar

def imprime(montocambiado, monedacambio):
    print("Su cambio es {:.3}".format(montocambiado), monedacambio)

def Cambio():
    datos = Captura_datos()
    if datos[2].upper() == "USA":
        montocambiado = USA(datos[0], datos[1])
    else:
        montocambiado = EU(datos[0], datos[1])
    imprime(montocambiado, datos[2])

Cambio()    
