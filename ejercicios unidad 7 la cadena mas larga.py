#ejercicio la cadena mas larga unidad 7

cadena = "maria tenia un corderito llamado pepe"

listapal = cadena.split(" ")

maslarga=""

for pal in listapal:
    if len(pal)>len(maslarga):
        maslarga = pal
print(maslarga)        
