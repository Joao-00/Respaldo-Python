#ciclo while
#while <condicion>:
#   accion 1
#
#
#   accion N


#se cumple mientras la condición siempre sea verdadera

#suma de cuadrados de los N primeros numeros
n = int(input("Ingrese la cantidad de numeros: "))
s = 0
i = 1
while i <= n:
    c = i**2
    s += c
    i += 1 #contador

print("la suma es: ",s)    


#otro ejemplo

edad=0
while edad < 18:
    edad = edad + 1
    print("felicidades, tienes", edad)

#otro ejemplo

promedio, total, contar = 0.0, 0, 0
sigo = true:
    while sigo:
        notadef= float(input("introduzca la nota de un estudiante: "))
        total = total + notadef
        contar = contar + 1
        print("procesar otro estudiante:(s-si, n-no): ")
        resp = input()
        if resp == "n": sigo = false
promedio = total / contar
print("promedio de notas del curso es: " + str(promedio))
        
