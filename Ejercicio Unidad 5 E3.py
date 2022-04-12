#ejercicio 3
#agregar personajes a una lista

#personajes de la pelicula el señor de los anillos
#nombre: Aragorn, clase: Guerrero, raza: Dunaban del norte
#nombre: Gandalf, clase: Mago, raza: Istar
#nombre: Legolas, clase: Arquero, raza: Elfo Sindar

#en una lista podemos tener diccionarios, tuplas e inclusive otras listas
personajes = []

p={'nombre': 'Aragorn', 'clase': 'Guerrero', 'raza': 'Dunaban del norte'}
personajes.append(p)
p={'nombre': 'Gandalf', 'clase': 'Mago', 'raza': 'Istar'}
personajes.append(p)
p={'nombre': 'Legolas', 'clase': 'Arquero', 'raza': 'Elfo Sindar'}
personajes.append(p)

print(personajes)
