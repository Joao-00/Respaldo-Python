#slicing


#cadena = "programando en python con G-Talent"
#cadena [0:11]
#print(cadena)
#investigar

#cadenas de caracteres - metodos


#sintaxis para el uso de los metodos
#id_variable_cadena.nombre_metodo()

#capitalize()

cadena = "programando en python"
print(cadena.capitalize())

#count(subcadena[,inicio[,final]])

cadena = "programando en python".capitalize()
print(cadena.count("o"))

#find(subcadena[,inicio[,final]])

cadena = "programando en python".capitalize()
print(cadena.find("en"))
#si no la encuentra retorna -1

#format()

texto = "la suma de {0} + {1} es {2}".format(1,2,1+2)
print (texto)

texto = "{2} se genera de {0} + {1}".format(1,2,1+2)
print (texto)

#si no posee numeros se ordenara por orden defecto

texto = "las frutas mas sabrosas son las {} y las {}".format("fresas", "manzanas")
print(texto)

texto = "las frutas mas sabrosas son las {F2} y las {F1}".format(F1="fresas", F2="manzanas")
print(texto)

#index(subcadena[,inicio[,final]])
print(cadena.index("en"))

#replace(sub a reemplazar, sub nueva)

text = "programando en visual"
print(text)
text.replace("visual", "python")
print(text)
#investigar


#split("separador")

groupwords = "programing in python"
print(groupwords.split(" "))


#join(iterable)

formato_numero_factura = "N°0000-0", "-0000(ID: ", ")"
numero = "275"
numero_factura = numero.join(formato_numero_factura)
print(numero_factura)

#lower()retorna la cadena en minuscula
cadena = "programando en python"
cadena.upper()
print(cadena)
cadena.lower()
print(cadena)
#upper() retorna la cadena en mayuscula

#partition("separador")

url = "http://www.g-talent.net"
url.partition("www.")
print(url)
protocol, separator, domain = url.partition("www.")
print("Protocolo:{0}\nDominio:{1}".format(protocol,domain))


