#ejercicios Unidad 5
#Eliminar elementos duplicados de una lista

lista = [5,5,5,7,8,8,8,9,12,12,5,5,9,9,4,4,1,1]

nueva = []

for ele in lista:
    if not ele in nueva:
        nueva.append(ele)

print(nueva)

#otra forma
#convierte la lista en un conjunto, los conjuntos no tienen elementos repetidos
lnew = set(lista) #lnew = list(set(lista))
lnew = list(lnew) #se elimina este comando
print(lnew)


        
